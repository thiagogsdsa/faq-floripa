from fastapi import FastAPI, Request, BackgroundTasks
from telegram import Update
from telegram.ext import (
    Application,
    ApplicationBuilder,
    ContextTypes,
    CommandHandler,
    MessageHandler,
    filters,
)

from build_prompt import * 
from retrieval import *
from generator import * 

import os


TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
WEBHOOK_PATH = "/webhook"


app = FastAPI()


base_dir = os.path.dirname(os.path.abspath(__file__))
faq_path = os.path.join(base_dir, "..", "data", "faq.json")
with open(faq_path, "r", encoding="utf-8") as f:
    faq_texts = json.load(f)



# Initialize your retriever (using your actual FAQ dataset)
faq_retriever = FAQRetriever(faq_texts, language=None)

#########################################################


# Async handlers
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hi! Ask me something about Florianópolis.")

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_question = update.message.text
    faqs = faq_retriever.retrieve(user_question, top_k=1)

    if not faqs:
        response = "Sorry, I couldn't find an answer for that."
    else:
        prompt = build_prompt(user_question, faqs[0])
        response = await generate_answer(prompt)

    await update.message.reply_text(response)



# Build the Telegram app with handlers
telegram_app = (
    ApplicationBuilder()
    .token(TELEGRAM_TOKEN)
    .build()
)

telegram_app.add_handler(CommandHandler("start", start))
telegram_app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

# FastAPI webhook route
@app.post(WEBHOOK_PATH)
async def telegram_webhook(request: Request):
    json_data = await request.json()
    update = Update.de_json(json_data, telegram_app.bot)
    await telegram_app.process_update(update)
    return {"ok": True}




curl -F "url=https://webhook.site/958de04c-f5cc-43c7-9f1b-95ea3e83ef6f" https://api.telegram.org/bot$TELEGRAM_TOKEN/setWebhook





{"id":"chatcmpl-6b77f788-464c-47b3-ad3d-baf89e67bc6f","object":"chat.completion","created":1747512940,"model":"meta-llama/llama-4-scout-17b-16e-instruct","choices":




[{"index":0,"message":{"role":"assistant","content":"The answer is 4."},"logprobs":null,"finish_reason":"stop"}],"usage":{"queue_time":0.630466235,"prompt_tokens":13,"prompt_time":0.002560199,"completion_tokens":7,"completion_time":0.013977272,"total_tokens":20,"total_time":0.016537471},"usage_breakdown":{"models":null},"system_fingerprint":"fp_37da608fc1","x_groq":{"id":"req_01jvfy6n35ek69jhnc5ja1hhyx"}}







