import tempfile
import os.path

TEMP_FOLDER = tempfile.gettempdir()
print('Folder "{}" will be used to save temporary dictionary and corpus.'.format(TEMP_FOLDER))

from gensim import corpora, models, similarities
if os.path.isfile(os.path.join(TEMP_FOLDER, 'deerwester.dict')):
    dictionary = corpora.Dictionary.load(os.path.join(TEMP_FOLDER, 'deerwester.dict'))
    corpus = corpora.MmCorpus(os.path.join(TEMP_FOLDER, 'deerwester.mm'))
    print("Used files generated from first tutorial")
else:
    print("Please run first tutorial to generate data set")

print(dictionary[0])
print(dictionary[1])
print(dictionary[2])