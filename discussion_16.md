## 知识抽取
1. **实体识别NER**
   - 作为序列标注问题
   - 隐马尔科夫模型HMM
   - 条件随机场CRF
   - 神经网络
2. 术语抽取
   - 多个单词组成的相关术语，比如深度神经网络、大数据分析、面向硬件的数据库研究
   - 暂时将其和实体识别划等号
3. *实体链接*
   - 链接搜索引擎，吸纳外部数据
   - 现阶段不重要
4. **关系抽取**
   - 基于模板,eg:
     - **老婆**：姚明**老婆**叶莉，徐峥**老婆**陶虹->A老婆B
   - 基于依存关系
   - 基于监督学习
     - 预先定义关系的类别
     - 人工标注一些数据
     - 设计特征表示
     - 选择分类方法
     - 评估
   - 基于半监督
     - 远程监督
       1. 从知识库中抽取存在关系的实体对，一旦识别到知识库中实体，则实体之间的关系即为知识库中的关系（**实体对齐**）
       2. *从文本中抽取含有实体对的句子作为训练样例*
       3. 我觉得不太可行，因为没有现成的知识库能够使用
     - BootStraping
       1. 识别实体之间的pattern
       2. pattern与文档集匹配
       3. 得到种子集
   - pipeline方法
     - 将实体识别、关系抽取作为独立的任务，先进行实体识别，再抽取关系，缺点是误差会逐层传递
   - end-to-end方法
     - 将两者放在一个模型中完成

   - **特征工程**，难顶，因为特征很多，比如词性、词中每个字、词的上下文，难以抽象
   - 解决办法：**利用深度学习自动生成特征，再根据特征得到结果，endo-to-end**
5. 事件抽取
  - terms
    - Agent施事者，Patient受事者，Pred谓词，theme客体，experiencer经验者，beneficiary受益者，instrument工具，location处所，goal目标，source来源；
    - NP名词短语，PP介词短语（mainly about），VP动词短语，CP补语
    - B：语块开始，I：语块中间部分，O语块结束
  - 浅层语义识别

## 任务
zpt：实体识别跑模型，看效果
xyq：关系抽取找相关内容
szh：实现改进版tf-idf

## 8.10讨论