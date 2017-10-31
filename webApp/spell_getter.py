import gensim
import csv
from nltk.tokenize import word_tokenize as tokenize

def readCSV():

    spellSet = {}

    reader = csv.DictReader(open('../data/datasets/Spells.csv'))

    for row in reader:
        for column, value in row.iteritems():
            spellSet.setdefault(column, []).append(value)


    return spellSet


def collectDocs():
    
    spellSet = readCSV()
    
    spellDocs = spellSet['Descriptions']
    
    print('Number of documents: ', len(spellDocs))
    
    return spellDocs


def tokenizeDocs():
    
    spellDocs = collectDocs()
    
    gen_docs = [[w.lower() for w in tokenize(text)] for text in spellDocs]
    
    return gen_docs


def main():
    docs = tokenizeDocs()
    dictionary = gensim.corpora.Dictionary(docs)
    corpus = [dictionary.doc2bow(docs) for docs in docs]
    tf_idf = gensim.models.TfidfModel(corpus)
    s = 0
    
    for i in corpus:
        s += len(i)
        
    sims = gensim.similarities.Similarity(tf_idf[corpus])
    return sims
    
    
def search(searchInput)
    query_doc = [w.lower() for w in tokenize(searchInput)]
    query_doc_bow = dictionary.doc2bow(query_doc)
    query_doc_tf_idf = tf_idf[query_doc_bow]
    sims = main()
    sortedSimilar = sorted(sims[query_doc_tf_idf])
    mostSimilar = sortedSimilar[:-5]
    return mostSimilar
        