def build_prompt(user_question: str, faq_item: dict) -> str:
    lang = faq_item.get('language', 'en')

    if lang == 'pt':
        prompt = f"""
Você é um assistente que responde perguntas sobre Florianópolis.
Você precisa considerar o contexto para gerar a resposta. 

Contexto:
Pergunta FAQ: {faq_item['question']}
Resposta FAQ: {faq_item['answer']}

Você precisa também considerar a pergunta do usúario.

Pergunta do usuário: {user_question}

Com base no contexto, responda de forma clara e completa:
"""
    else:
        prompt = f"""
You are an assistant answering questions about Florianópolis.

Context:
FAQ Question: {faq_item['question']}
FAQ Answer: {faq_item['answer']}

User question: {user_question}

Based on the context, provide a clear and complete answer:
"""
    return prompt.strip()

