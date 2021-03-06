import scrapy
import re
import time
import json
import random
from kashgari.utils import load_model
from scrapy.loader import ItemLoader
from teacher.items import TeacherItem 

def cleanSpace(string):
    if string:
        return re.sub('\s','',string)
    else:
        return None

class Teacher(scrapy.Spider):
    name = 'teacher'
    def __init__(self):
        super().__init__()

        self.refer_dict = {'电话':'phone','办公电话':'phone','个人主页':'homepage','电子邮箱':'email','邮箱':'email','地址':'office','办公室':'office','传真':'fax','系别':'major','职称':'title','职务':'position'}
        with open('../configs/config_%s.json' % input("department:"),'r',encoding='utf-8') as f:
            self.config = json.load(f)
            #self.file = re.search('(.*?).json',f.name).group(1)
        
        self.model = load_model(r'D:\Ubuntu\rootfs\home\pt\models\bert_epoch_20_new')

    def start_requests(self):
        for url in list(self.config.keys()):
            yield scrapy.Request(url = url,callback=self.parse,meta={'url':url})

    def parse_homepage(self,response):
        
        item = response.meta['item']
        config = response.meta['config']

        item['url'] = response.url

        if not config['refer_dict']:
            properties_detail = config['properties_detail']
            for prop in list(config['properties_detail'].keys()):
                
                prop_dict = properties_detail[prop]
                try:
                    if prop_dict['getall'] == True:
                        entry = prop_dict['entry']
                        value = response.xpath(entry[0]).getall()
                        
                        item[prop] = value

                except KeyError:
                    value = ''
                    for index,entry in enumerate(prop_dict['entry']):
                        
                        try:
                            segment = response.xpath(entry).get().strip()
                            
                        except:
        
                            continue

                        pattern = prop_dict['pattern']
                        if pattern == []:
                            value += segment
                        else:
                            segment = re.search(pattern[index][0],segment).group(pattern[index][1])
                            value += segment

                if value != '':    
                    item[prop] = value

            yield item

        else:
            details = response.xpath(config['detail_entry'])
            refer_dict = self.refer_dict
            pattern = re.compile(config['pattern_further'])

            for text in details.getall():
                
                text = re.sub('\s','',text)
                try:
                    key = pattern.search(text).group(1)
                    value = pattern.search(text).group(2)
                except AttributeError:
                    #处理有些字段为空
                    continue
                if value:
                    try:
                        item[refer_dict[key]] = value
                        
                    except:
                        continue

            if config['extra_info']:
                #each entry correspond with one prop
                properties_extra = config['properties_extra']

                for prop in list(properties_extra.keys()):
                    prop_dict = properties_extra[prop]
                    
                    try:
                        values = response.xpath(prop_dict['entry']).getall()
                        item[prop] = []
                    except:
                        continue
                     
                    for each in values:
                        try:
                            value = re.search(prop_dict['pattern'][0],cleanSpace(each)).group(prop_dict['pattern'][1])
                        except:
                            value = cleanSpace(each)
                                            
                        item[prop].append(value)
                        
                yield item

            else:
                yield item

    def parse(self,response):
        #time.sleep(2)

        url = response.meta['url']
        config = self.config[url]
        properties = config['properties']
        
        for each in response.xpath(config['brief_entry']):
            item = TeacherItem()
            #item_loader = ItemLoader(item=item)
            #item_loader.add_value('department',config['department'])
            item['department'] = config['department']
            
            for prop in list(properties.keys()):
            
                prop_dict = properties[prop]

                try:
                    value = each.xpath(prop_dict['entry']).get()
                    value = cleanSpace(value)
                except:
                    continue
                
                try:
                    value= re.search(prop_dict['pattern'][0],value).group(prop_dict['pattern'][1])
                except:
                    #同一个Field有的需要处理，有的不需要
                    pass

                item[prop] = value
                

            if config['further_explore']:
                each_url = each.xpath(config['href_entry']).get()
                try:
                    time.sleep(random.randrange(config['sleep'][0],config['sleep'][1]))
                except:
                    pass
                #time.sleep(5)
                yield scrapy.Request(response.urljoin(each_url),callback=self.parse_homepage,meta={'item':item,'config':config})
            
            else:
                yield item#item_loader.load_item()
        
        if config['next_entry']:
            next_page = response.xpath(config['next_entry']).get()
        else:
            next_page = None
        
        if next_page is not None:
            yield response.follow(next_page,callback=self.parse,meta={'config':config,'url':url})