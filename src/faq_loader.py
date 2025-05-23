#class FAQLoader:
#    def __init__(self, filepath):
#        self.filepath = filepath
#
#    def load(self):
#        import json
#        with open(self.filepath, 'r', encoding='utf-8') as f:
#            raw_data = json.load(f)
#        return self._process(raw_data)
#
#    def _process(self, raw_data):
#        faqs = []
#        for entry in raw_data:
#            faq = {
#                "id": entry.get("id"),
#                "question_pt": entry.get("question_pt", ""),
#                "answer_pt": entry.get("answer_pt", ""),
#                "question_en": entry.get("question_en", ""),
#                "answer_en": entry.get("answer_en", "")
#            }
#            faqs.append(faq)
#        return faqs
#

def standardize_faq_keys(faq_texts):
    standardized = []
    for item in faq_texts:
        standardized.append({
            "id": item.get("id", ""),
            "question_pt": item.get("pergunta_pt", ""),
            "answer_pt": item.get("resposta_pt", ""),
            "question_en": item.get("pergunta_en", ""),
            "answer_en": item.get("resposta_en", "")
        })
    return standardized
