#🇳‌🇮‌🇰‌🇭‌🇮‌🇱‌
# Add your details here and then deploy by clicking on HEROKU Deploy button
import os
from os import environ

API_ID = int(environ.get("API_ID", "24250238"))
API_HASH = environ.get("API_HASH", "cb3f118ce5553dc140127647edcf3720")
BOT_TOKEN = environ.get("BOT_TOKEN", "6234022831:AAGXxnk_pOGRm0dUAFPQHjgF9h2vEtdzGTs")

OWNER = int(environ.get("OWNER", "6175650047"))
CREDIT = environ.get("CREDIT", "𝙎𝘼RGIO")
cookies_file_path = os.getenv("cookies_file_path", "youtube_cookies.txt")

TOTAL_USER = os.environ.get('TOTAL_USERS', '6175650047').split(',')
TOTAL_USERS = [int(user_id) for user_id in TOTAL_USER]

AUTH_USER = os.environ.get('AUTH_USERS', '6175650047').split(',')
AUTH_USERS = [int(user_id) for user_id in AUTH_USER]
if int(OWNER) not in AUTH_USERS:
    AUTH_USERS.append(int(OWNER))
  
#WEBHOOK = True  # Don't change this
#PORT = int(os.environ.get("PORT", 8080))  # Default to 8000 if not set





