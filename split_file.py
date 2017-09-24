#-*-coding:utf-8-*-
import re
import jieba
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
"""
for line in open('2016G201000.xml'):

    if(re.findall(ur"^<Content>", line.decode("utf-8"))):
        print "0"
    else:
        line = line.strip('\n')
    print line
    #line = line.strip('\n')

    # yield line.lower().split()
"""
f = open('2016G201000.xml')
contents = f.read()
contents = contents.split('<Content>')
#print contents[1]
# 哇 生命短暂要用python
texts = []
for content in contents:
    content = content.replace('\n','')
    content = re.findall(ur"[\u4e00-\u9fa5]+", content.decode("utf-8"))
    content = "".join(content)
    content = jieba.lcut(content, cut_all=False) # 默认也是精确模式 lcut 返回list
    #print content[0]
    texts.append(content)
    #print " ".join(content)
    #print "\n"
#for text in texts:
#    print text

from gensim import corpora, models, similarities
import logging
import jieba
import jieba.posseg as pseg
# 防止乱码
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
# 打印log信息
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)


# 抽取一个bag-of-words，将文档的token映射为id
dictionary = corpora.Dictionary(texts)
#print dictionary.token2id
# 保存词典
dictionary.save('LSI.dict')

# 产生文档向量，将用字符串表示的文档转换为用id和词频表示的文档向量
corpus = [dictionary.doc2bow(text) for text in texts]
corpora.MmCorpus.serialize('LSI.mm', corpus)  # store to disk, for later use
#for c in corpus:
#    print(c)

# 基于这些“训练文档”计算一个TF-IDF模型
tfidf = models.TfidfModel(corpus)

# 转化文档向量，将用词频表示的文档向量表示为一个用tf-idf值表示的文档向量
corpus_tfidf = tfidf[corpus]
#打印一下tfidf模型中的信息：
#print tfidf.dfs #df
print 0
#print tfidf.idfs
# 训练LSI模型 即将训练文档向量组成的矩阵SVD分解，并做一个秩为2的近似SVD分解
lsi = models.LsiModel(corpus_tfidf, id2word=dictionary, num_topics=10)

# 保存模型
#lsi.save('LSI.pkl')
#lsi.print_topics(5)

corpus_lsi = lsi[corpus_tfidf]
for doc in corpus_lsi:
    print doc