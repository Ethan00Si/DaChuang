# 字典

## entities consists of：
- teachers：教师
  * 属性有：职称、职务
- departments：各个学院
  * 属性有：地点
- meetings：会议、讲座等老师参加的活动（**待处理，命名实体抽取，即识别出会议和参与会议的教师；关系抽取，即识别出“参与会议这个关系”**）
- majors：各个学院的专业
- orgnazations：各种组织
- labs：老师的实验室
- activities：学生活动

## dictionary(/data/语料/dictionary.txt) consisits of:
- names：教师姓名
- majors：教师专业
- departments：学院、部门名称
- meetings（**不完全**）：会议
- labs：老师的实验室
- positions：职称和职务
- anouncements：重要通知
- activities：学生活动
- locations：地点
- student_orgnazations:学生组织

## 出现就直接推送
- activitis：学生活动（**待处理，实现自动识别**）
- announcements：重要通知

## TO DO
- 自动化实体识别
- 自动化实体分类
- 实体分类和之后的应用之间的关系