from sentence_transformers import SentenceTransformer
from preprocessor import Preprocessor
import faiss
import numpy as np
import torch 

class FAQEmbedder:
    def __init__(self, faq_list, language='pt', model_name='paraphrase-multilingual-MiniLM-L12-v2',clean_text=False,device ='cpu'),:
        self.language = language
        self.preprocessor = Preprocessor(language)
        self.device = "cuda" if torch.cuda.is_available() else "cpu"
        self.model = SentenceTransformer(model_name, device = device)
        self.faq_list = faq_list
        self.clean_text = clean_text
        # Clean or not questions before encoding
        self.texts = [self._clean_if_needed(f[f"question_{language}"]) for f in faq_list]
        self.answers = [f[f"answer_{language}"] for f in faq_list]
        self.ids = [f["id"] for f in faq_list]
        self.index = self._build_index()

    def _clean_if_needed(self,text):
        if self.clean_text:
            return self.preprocessor.clean(text)
        else:
            return text 
        
    def _build_index(self):
        embeddings = self.model.encode(self.texts, convert_to_numpy=True)
        faiss.normalize_L2(embeddings)
        index = faiss.IndexFlatIP(embeddings.shape[1])
        index.add(embeddings)
        return index
    
    