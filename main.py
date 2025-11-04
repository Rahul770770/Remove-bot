from telegram.ext import Updater, MessageHandler, Filters
import re

def check_and_delete(update, context):
    message = update.message.text
    if message:
        links = re.findall(r'https?://[^\s]+', message)
        for link in links:
            if "x.com" in link:
                if '?' in link.split("x.com")[-1]:
                    update.message.delete()
                    context.bot.send_message(
                        chat_id=update.effective_chat.id,
                        text=f"Please share clean X links only — trackers removed."
                    )
                    break

def main():
    updater = Updater("7829413649:AAEO4DXXIXwsbk21nhSEOTSQKYJEEDBeGmw", use_context=True)
    dp = updater.dispatcher
    dp.add_handler(MessageHandler(Filters.text & Filters.group, check_and_delete))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
