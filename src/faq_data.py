import json
from database import insert_faq

def load_faq_from_json(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        faqs = json.load(f)
    return faqs

def save_faqs_to_db(faqs):
    for faq in faqs:
        insert_faq(faq)
