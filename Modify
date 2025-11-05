from telegram.ext import Updater, MessageHandler, Filters
import re

def clean_x_link(link):
    # Remove everything after '?' in link
    clean_link = link.split('?')[0]
    return clean_link

def handle_message(update, context):
    message = update.message.text
    if message:
        links = re.findall(r'https?://[^\s]+', message)
        sent_clean_link = False
        for link in links:
            if "x.com" in link and '?' in link:
                # If tracker exists, clean it & delete old msg
                clean_link = clean_x_link(link)
                update.message.delete()
                # Send clean link, mention user
                context.bot.send_message(
                    chat_id=update.effective_chat.id,
                    text=f"@{update.message.from_user.username} shared a clean link:\n{clean_link}"
                )
                sent_clean_link = True
        # If no tracked X link was found, do nothing

def main():
    # Replace YOUR_BOT_TOKEN here
    updater = Updater("7111823055:AAEV2Mclf1vIE0MG7nOj1ctTdx8vjwvWsCI", use_context=True)
    dp = updater.dispatcher

    dp.add_handler(MessageHandler(Filters.text & Filters.group, handle_message))

    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
