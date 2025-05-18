import spacy
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import RegexpTokenizer
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import ENGLISH_STOP_WORDS

# Baixar recursos do NLTK
nltk.download('stopwords')
nltk.download('wordnet')

class Preprocessor:
    def __init__(self, language='pt'):
        self.language = language
        self.tokenizer = RegexpTokenizer(r'\w+')

        if language == 'pt':
            self.stopwords = set(stopwords.words('portuguese'))
            self.spacy_model = spacy.load("pt_core_news_sm")
        else:
            self.stopwords = set(ENGLISH_STOP_WORDS)
            self.lemmatizer = WordNetLemmatizer()
            self.spacy_model = spacy.load("en_core_web_sm")

    def clean(self, text):
        text = text.lower() 
        tokens = self.tokenizer.tokenize(text)
        tokens = [t for t in tokens if t not in self.stopwords]

        # Lematização com spaCy
        doc = self.spacy_model(' '.join(tokens))
        lemmatized = [token.lemma_ for token in doc if token.lemma_.isalpha() and token.lemma_ not in self.stopwords]

        return ' '.join(lemmatized)





