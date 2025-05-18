from retrieval import *
#from src.embeddings import *
import os
import json 

# Example FAQs

base_dir = os.path.dirname(os.path.abspath(__file__))
faq_path = os.path.join(base_dir, "..", "data", "faq.json")
with open(faq_path, "r", encoding="utf-8") as f:
    faq_texts = json.load(f)

language = None
#etriever = FAQRetriever(faq_texts,language = language)
retriever_tf =  FAQRetrieverTFIDF(faq_texts,language = None)  

query = "O que fazer em lagoa da conceição?"

print("Pergunta:", query)
results = retriever_tf.retrieve(query) 
if results:
    for result in results:
        print(result)
        print("----------------")
