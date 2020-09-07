
import os

class Config:
    BOT_TOKEN = os.environ.get("BOT_TOKEN"," ")
    HEROKU_API_KEY = os.environ.get("HEROKU_API_KEY"," ")
    
    try:
        SUDO_USERS = set(
            int(x) for x in os.environ.get("SUDO_USERS", "").split())
            except ValueError:
              raise Exception(     "Your sudo list does not contain valid integers.") 
   try:
      SUPPORT_USRS = set(
            int(x) for x in os.environ.get("SUPPORT_USERS", "").split()
            except ValueError:
              raise Exception(        "Your support list does not contain valid integers.")
    LOG = os.environ.get('LOG', None)
    TG_CHARACTER_LIMIT = 4000 
    HEROKU_APP_NAME = os.environ.get("HEROKU_APP_NAME"," ")