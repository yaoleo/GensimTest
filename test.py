# yaoleo

import os
import tempfile
TEMP_FOLDER = tempfile.gettempdir()
print('Folder "{}" will be used to save temporary dictionary and corpus.'.format(TEMP_FOLDER))

from gensim import corpora, models, similarities


class MyCorpus(object):
    def __iter__(self):
        #for line in open('mycorpus.txt'):
        for line in open('2016G201000_result.txt'):
            #print line
            yield line.lower().split()


Crop = MyCorpus() # doesn't load the corpus into memory!
for i in Crop:
    print i
"""
# remove common words and tokenize
stoplist = set('for a of the and to in / < > br gt p & nbsp = utf - ? xml ( # ! pcdata ) * | element lt ; : tbody tr td'.split())
Crop = [[word for word in document if word not in stoplist]
         for document in Crop]
#for i in range(0,500):
#    print texts[i]
# remove words that appear only once
from collections import defaultdict
frequency = defaultdict(int)
for text in Crop:
    for token in text:
        frequency[token] += 1

texts = [[token for token in text if frequency[token] > 1] for text in Crop]

dictionary = corpora.Dictionary(Crop)
#print dictionary
dictionary.save('/tmp/2016G201000.dict') #
corpus = [dictionary.doc2bow(text) for text in Crop]
#print(corpus)
#for i in corpus:
#    print i
tfidf = models.TfidfModel(corpus)

corpus_tfidf = tfidf[corpus]

corpora.MmCorpus.serialize('/tmp/2016G201000_corpus.mm', corpus)

"""