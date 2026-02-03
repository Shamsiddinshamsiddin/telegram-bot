from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import openai

TOKEN = "8555444620:AAHqy1NQgZUWhHua_ZBlQWvR5T0q8ccJi88"
openai.api_key = "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"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Salom! Men AI yordamchi botman 🤖")

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "/start - Botni ishga tushurish\n"
        "/help - Yordam\n"
        "/ask - AI ga savol berish"
    )

async def ask(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not context.args:
        await update.message.reply_text("Savol yozing: /ask Nima bu AI?")
        return

    question = " ".join(context.args)

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": question}]
    )

    answer = response.choices[0].message.content
    await update.message.reply_text(answer)

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("help", help_command))
app.add_handler(CommandHandler("ask", ask))

print("Bot ishga tushdi ✅")
app.run_polling()