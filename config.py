import os

API_ID = API_ID = 20959078

API_HASH = os.environ.get("API_HASH", "b3dd1e7fa169aae46bb0d841519e1ab8")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "6915553639:AAEwtoaGyoZFvzNUGZG6U3JruFvdLli0t5U")

PASS_DB = int(os.environ.get("PASS_DB", "721"))

OWNER = int(os.environ.get("OWNER", 6701527422))

LOG = -1002065884296

try:
  GROUPS =[]
  for x in (os.environ.get('GROUPS', '-1002065884296 -1002014730016').split()):
    GROUPS.append(int(x))
except ValueError:
    raise Exception("Your AUTH GROUPS list does not contain valid integers.")    

try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "6940485320 6224785606").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")
ADMINS.append(OWNER)


