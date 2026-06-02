import joblib, os, re
from nltk.corpus import stopwords
import nltk
nltk.download('stopwords', quiet=True)

BASE    = os.path.join(os.path.dirname(__file__), '..', 'models')
tfidf   = joblib.load(os.path.join(BASE, 'tfidf_vectorizer.pkl'))
lr      = joblib.load(os.path.join(BASE, 'lr_model.pkl'))

LABELS  = ['none', 'mild', 'moderate', 'severe']

STOP_WORDS = set(stopwords.words('english')) - {'no', 'not', 'nor', 'never'}

SLANG_MAP = {
    'wanna':'want to','gonna':'going to','gotta':'got to',
    'idk':'i do not know','tbh':'to be honest','ngl':'not gonna lie',
    'fr':'for real','rn':'right now','smh':'shaking my head',
}

def preprocess(text):
    text = str(text).lower()
    text = re.sub(r'http\S+|www\S+', '', text)
    text = re.sub(r'@\w+', '', text)
    text = re.sub(r'#\w+', '', text)
    text = re.sub(r'[^a-z\s]', ' ', text)
    tokens = text.split()
    tokens = [SLANG_MAP.get(t, t) for t in tokens]
    tokens = [t for t in tokens if t not in STOP_WORDS]
    return ' '.join(tokens)

def predict(text):
    clean = preprocess(text)
    vec   = tfidf.transform([clean])
    probs = lr.predict_proba(vec)[0].tolist()
    label = LABELS[probs.index(max(probs))]
    return {
        'label': label,
        'probs': dict(zip(LABELS, [round(p, 4) for p in probs]))
    }