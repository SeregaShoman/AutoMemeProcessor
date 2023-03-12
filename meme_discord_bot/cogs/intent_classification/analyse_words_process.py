import spacy
import pickle
from sklearn import svm
import ru_core_news_lg
from .words_config import train_x, train_y

nlp = spacy.load("ru_core_news_lg")

train_x_words = [text.lower().split() for text in train_x]

docs = [nlp(text) for text in train_x]

train_x_word_vectors = [x.vector for x in docs]

clf_svm_wm = svm.SVC(kernel="linear")
clf_svm_wm.fit(train_x_word_vectors, train_y)

def voice_tag(text: str):
    words = text.lower().split()
    scores = []
    for word in words:
        doc = nlp(word)
        score = clf_svm_wm.predict(doc.vector.reshape(1, -1))[0]
        scores.append(score)
    
    # преобразование типа numpy.str в str
    return [str(score) for score in scores]
