from telegram.ext import Updater, MessageHandler, Filters
import re

# ---- Access Control ----
ALLOWED_USERS = [5828315144,6688222645]         
ALLOWED_GROUPS = [-1003272247886]  

def check_and_delete(update, context):
    # --- Access Restriction ---
    user_id = update.effective_user.id
    chat_id = update.effective_chat.id


    if user_id not in ALLOWED_USERS and chat_id not in ALLOWED_GROUPS:
        return

    # --- Main Logic ---
    message = update.message.text
    if message:
        links = re.findall(r'https?://[^\s]+', message)
        for link in links:
            if "x.com" in link:
                if '?' in link.split("x.com")[-1]:
                    try:
                        update.message.delete()
                        context.bot.send_message(
                            chat_id=update.effective_chat.id,
                            text="Please share clean X links only — trackers removed."
                        )
                    except Exception as e:
                        print(f"Error deleting message: {e}")
                    break

def main():
   
    updater = Updater("7829413649:AAEO4DXXIXwsbk21nhSEOTSQKYJEEDBeGmw", use_context=True)
    dp = updater.dispatcher

    dp.add_handler(MessageHandler(Filters.text & Filters.group, check_and_delete))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
