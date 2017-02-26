from get_data import Get_data
from nltk.corpus import stopwords
from nltk.stem.wordnet import WordNetLemmatizer
import string

#initialize some preprocessing tools
stop = set(stopwords.words('english'))
exclude = set(string.punctuation)
lemma = WordNetLemmatizer()



def clean(doc):
    stop_free = " ".join([i for i in doc.lower().split() if i not in stop])
    punc_free = ''.join(ch for ch in stop_free if ch not in exclude)
    normalized = " ".join(lemma.lemmatize(word) for word in punc_free.split())
    return normalized

def Get_clean_data(filename):
    doc_complete = Get_data(filename)
    return [clean(doc).split() for doc in doc_complete]