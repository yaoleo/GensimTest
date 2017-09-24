#-*-coding:utf-8-*-
from gensim import corpora,models,similarities

corpus = corpora.MmCorpus('/tmp/2016G201000_corpus.mm')
dictionary = corpora.Dictionary.load('/tmp/2016G201000.dict')
#print corpus

#print(dictionary.token2id)
lsi = models.LsiModel(corpus, id2word=dictionary, num_topics=2)

file_object = open("2016G201000_result.txt", 'r')  #
all_the_text = file_object.read()  #
Crop =  all_the_text.lower().split()

# remove common words and tokenize
stoplist = set('for a of the and to in / < > br gt p & nbsp = utf - ? xml ( # ! pcdata ) * | element lt ; : tbody tr td'.split())
Crop = [word for word in Crop if word not in stoplist]

#for i in Crop:
#    print i
file_object.close()

vec_bow = dictionary.doc2bow(Crop)
vec_lsi = lsi[vec_bow] # convert the query to LSI space
print(vec_lsi)

index = similarities.MatrixSimilarity(lsi[corpus]) # transform corpus to LSI space and index it
sims = index[vec_lsi] # perform a similarity query against the corpus

#print(list(enumerate(sims))) # print (document_number, document_similarity)
sims = sorted(enumerate(sims), key=lambda item: -item[1])
print sims

