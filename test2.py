# yaoleo

import os
import tempfile
TEMP_FOLDER = tempfile.gettempdir()
print('Folder "{}" will be used to save temporary dictionary and corpus.'.format(TEMP_FOLDER))

from gensim import corpora, models, similarities


class MyCorpus(object):
    def __iter__(self):
        #for line in open('mycorpus.txt'):

        file_object = open("2016G201000_result.txt", 'r')  #
        all_the_text = file_object.read()  #
            #print type(all_the_text)
        #print "all_the_text=", all_the_text
        yield all_the_text.lower().split()
        file_object.close()


Crop = MyCorpus() # doesn't load the corpus into memory!

# remove common words and tokenize
stoplist = set('for a of the and to in / < > br gt p & nbsp = utf - ? xml ( # ! pcdata ) * | element lt ; : tbody tr td'.split())
Crop = [[word for word in document if word not in stoplist]
         for document in Crop]

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

