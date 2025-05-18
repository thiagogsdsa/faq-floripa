from embeddings import *
from preprocessor import *
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import ENGLISH_STOP_WORDS
from abc import ABC, abstractmethod

class BaseFAQRetriever(ABC):
    @abstractmethod
    def retrieve(self, question: str, top_k: int = 3) -> list:
        """
        Given a question, return the top_k most similar FAQs.
        Each result must be a dictionary containing:
            - 'id': index of the FAQ
            - 'question': original question text
            - 'answer': corresponding answer
            - 'score': similarity score
            - 'language': used language
        """
        pass

class FAQRetriever(BaseFAQRetriever):
    def __init__(self, faq_texts, language= None, model_name='paraphrase-multilingual-MiniLM-L12-v2'):
        # If language is None, use both pt and en
        if language is None:
            self.languages = ('pt', 'en')
        else:
            if isinstance(language, str):
                self.languages = (language,)
            else:
                raise ValueError("language must be 'pt', 'en', or None")

        # Create one FAQEmbedder per language
        self.embedders = {
            lang: FAQEmbedder(faq_texts, lang, model_name)
            for lang in self.languages
        }

    def retrieve(self, question, top_k=3, language=None):
        all_results = []
        langs_to_search = [language] if language else self.languages

        for lang in langs_to_search:
            embedder = self.embedders[lang]
            cleaned_question = embedder.preprocessor.clean(question)
            query_vec = embedder.model.encode([cleaned_question], convert_to_numpy=True)
            faiss.normalize_L2(query_vec)

            scores, indices = embedder.index.search(query_vec, top_k)

            for idx, score in zip(indices[0], scores[0]):
                all_results.append({
                    "id": embedder.ids[idx],
                    "question": embedder.texts[idx],
                    "answer": embedder.answers[idx],
                    "language": lang,
                    "score": float(score)
                })

        all_results.sort(key=lambda x: x['score'], reverse=True)
        return all_results[:top_k]

class FAQRetrieverTFIDF(BaseFAQRetriever):
    def __init__(self, faq_texts, language='pt'):
        self.faq_texts = faq_texts
        self.language = language

        self.preproc_pt = Preprocessor(language='pt')
        self.preproc_en = Preprocessor(language='en')

        self.questions_pt = [self.preproc_pt.clean(faq.get('question_pt', '')) for faq in faq_texts]
        self.questions_en = [self.preproc_en.clean(faq.get('question_en', '')) for faq in faq_texts]

        self.vectorizer_pt = TfidfVectorizer()
        self.vectorizer_en = TfidfVectorizer()

        self.tfidf_matrix_pt = self.vectorizer_pt.fit_transform(self.questions_pt)
        self.tfidf_matrix_en = self.vectorizer_en.fit_transform(self.questions_en)

    def retrieve(self, question, top_k=3):
        def search_in_language(lang):
            preproc = self.preproc_pt if lang == 'pt' else self.preproc_en
            vectorizer = self.vectorizer_pt if lang == 'pt' else self.vectorizer_en
            tfidf_matrix = self.tfidf_matrix_pt if lang == 'pt' else self.tfidf_matrix_en

            cleaned_question = preproc.clean(question)
            question_vec = vectorizer.transform([cleaned_question])
            similarities = cosine_similarity(question_vec, tfidf_matrix).flatten()

            results_lang = []
            for i, score in enumerate(similarities):
                faq = self.faq_texts[i]
                answer = faq.get(f'answer_{lang}', '')
                question_text = faq.get(f'question_{lang}', '')
                results_lang.append({
                    "id": i,
                    "question": question_text,
                    "answer": answer,
                    "score": float(score),
                    "language": lang
                })
            return results_lang

        # Retrieve in both languages and merge
        results_pt = search_in_language('pt')
        results_en = search_in_language('en')
        combined = sorted(results_pt + results_en, key=lambda x: x['score'], reverse=True)[:top_k]

        return combined
