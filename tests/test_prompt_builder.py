import sys
import os
import json
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))
from dotenv import load_dotenv

# # 1) Load env vars so GROQ_API_KEY is available
load_dotenv()        # make sure this is active

from retrieval import FAQRetriever
from prompt_builder import build_prompt
from generator import generate_answer_sync
def main():
    user_question = "Qual a melhor época para visitar Florianópolis?"
    language = None

    # 2) Load your FAQ JSON
    base_dir = os.path.dirname(os.path.abspath(__file__))
    faq_path = os.path.join(base_dir, "..","data", "faq.json")
    with open(faq_path, "r", encoding="utf-8") as f:
        faq_texts = json.load(f)

    # 3) Retrieve
    retriever = FAQRetriever(faq_texts=faq_texts, language=language)
    results = retriever.retrieve(user_question, top_k=1)
    if not results:
        print("No FAQ match found.")
        return

    # 4) Build prompt
    faq_item = results[0]
    new_prompt = build_prompt(user_question, faq_item)
    print( "Prompt:\n", new_prompt, "\n", "#" * 40, "\n")

    # 5) Generate answer (must await!)
    ans =  generate_answer_sync(new_prompt)

    # 6) Print result
    print("Model’s answer:\n", ans, "\n(Type:", type(ans), ")")

if __name__ == "__main__":
    #asyncio.run(main())
    main()
