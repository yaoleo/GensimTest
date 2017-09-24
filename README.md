虽然还没通过考核，还是整理一下这周进度。

## 任务完成：

先检索了一下关键词，觉得学一下框架应该很快就能完成，而且框架非常友好。接着快速的学了一下框架。参考：

官方文档：https://radimrehurek.com/gensim/tutorial.html

翻译文档：https://radimrehurek.com/gensim/tutorial.html

实践的时候发现对算法原理不清楚，对怎么用数据集有点迷糊，重读了lsi的原理，笔记：
http://nbviewer.jupyter.org/github/yaoleo/GensimTest/blob/master/LSI_Learn1.ipynb

### 一些记录

![TF-IDF](/NoteImg/TF-IDF.png)
![SVD1.png](/NoteImg/SVD1.png)
![SVD2.png](/NoteImg/SVD2.png)
![BYES1](/NoteImg/BYES1.png)
![BYES2](/NoteImg/BYES2.png)

过程中遇到中英文符号处理和字符编码等一些问题。

终于完成了实践部分：
具体实现的时候只用了数据集中的一个xml：2016G20文件，然后按Content标签分，分成1002行好像。然后预处理，保留中文，分词，stoplist，onceword等。
lsi降到维度100 测试与其中第100篇文章相似度最高的文章分别是哪些？

lsi，lda，tf-idf算法的文档相似度计算基本完成（如果对测试数据集的使用方式理解没错误的话）。
代码在这里：http://nbviewer.jupyter.org/github/yaoleo/GensimTest/blob/master/LSI_Learn2.ipynb

## 任务待完成/改进：
+ 中文的停止词 出现进一次的 进一步过滤
+ lda算法原理还没看完，涉及的原理里：朴素贝叶斯看了，几个分布原理还没看（有点忘） 
+ doc2vec simhash原理还没看 实现上应该难度比较小一点了 因为处理流程比较清楚一点了 可能主要就是函数和参数的不同

## 任务之前：
说一下这周做任务之前在做的事情：
因为有一个作业是计算任意两个实体名词的距离到0-1之间，老师讲的关键词主要是语义网，rdf等。最开始想法是爬百度百科，觉得可能太复杂，爬知乎话题树好像是有向无环图，可能更简单一点。反正是爬数据。就学了一点scrapy，还是非常好用的。但是有验证码的登录问题没搞定，cookie也没搞定。


## 疑惑
+ 要求是不是分析一个xml里不同文章的相似性呀？我最开始以为是测试不同xml文件的相似度，那这样应该只能把一个文件处理成一行，然后用这个算法分析九个超长的文档，即9*n矩阵n超大，一个超扁的矩阵用这个算法就不太合适，降维空间没有了呀，不知道理解的对不对。
+ 算法的原理大概应该了解到什么深度才行呀？lsi明明已经看很基础的数学了，我还是觉得很抽象，为什么SVD把矩阵降维之后，左奇异矩阵和右奇异矩阵就能算出词义和文档等之间的关系呀？
