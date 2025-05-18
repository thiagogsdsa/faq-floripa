from retrieval import *
from langdetect import detect
from prompt_builder import build_prompt
from generator import generate_answer_async
import logging
import os   
import asyncio                 
import json 
from telegram import ReplyKeyboardMarkup, Update
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    MessageHandler,
    filters,
    ConversationHandler,
    ContextTypes
)

LANGUAGE, QUESTION = range(2)
threshold = 0 #If score < 0.75 -> print("Sorry, no good answer found.")
#https://web.telegram.org/k/#@floripabot
# Initialize logging

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Please, you can ask about Florianopolis in English or Portuguese.\n"
        "Por favor, você pode perguntar sobre Florianópolis em Inglês ou Português."
    )

async def answer_question(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_question = update.message.text
    print(f"User asked: {user_question}")

    try:
        detected_lang = detect(user_question)
        print(f"Detected language: {detected_lang}")
    except Exception as e:
        print(f"Language detection failed: {e}")
        detected_lang = 'en'  

    user_language = 'pt' if detected_lang.startswith('pt') else 'en'
    retriever = FAQRetrieverTFIDF(faq_texts, language=None)
    results = retriever.retrieve(user_question, top_k=1)
    
    if not results or (len(results) > 0 and results[0].get('score', 0) < threshold):
        if detected_lang == 'en':
            await update.message.reply_text("Sorry, no good answer found.")
        elif detected_lang == 'pt': 
            await update.message.reply_text("Desculpe, não encontrei uma resposta relevante.")
        return 
    best = results[0]
    prompt =  build_prompt(user_question,best)
    #await update.message.reply_text(f"Answer:\n{best['answer']}")
    try:
        gen_response = await generate_answer_async(prompt)
    except Exception as e:
        print("Error in generation: {e}")
    await update.message.reply_text(f"{gen_response}")    
    await update.message.reply_text(
        "You can ask another question or send /start to restart."
        "\nVocê pode fazer outra pergunta ou enviar /start para reiniciar."
    )

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

base_dir = os.path.dirname(os.path.abspath(__file__))
faq_path = os.path.join(base_dir, "..", "data", "faq.json")
with open(faq_path, "r", encoding="utf-8") as f:
    faq_texts = json.load(f)


async def  main():
    bot_token = os.getenv("TELEGRAM_TOKEN")  # Replace with your bot token
    application = ApplicationBuilder().token(bot_token).build()
    await application.bot.delete_webhook(drop_pending_updates=True)

    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, answer_question))

    # application.run_polling()
    await application.initialize()
    await application.start()
    await application.updater.start_polling()
    try:
        await asyncio.Event().wait()
    except (KeyboardInterrupt, SystemExit):
        print("Shutting down bot...")

    await application.updater.stop()
    await application.stop()
    await application.shutdown()

if __name__ == '__main__':
    asyncio.run(main())
