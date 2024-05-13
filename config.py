import os

API_ID = API_ID = 24932123

API_HASH = os.environ.get("API_HASH", "112c5df5cf965ab22a7f8460a5026794")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "6923773907:AAGk99eIe-RkraiB_0497uIHZkXSjGIsy8E")

PASS_DB = int(os.environ.get("PASS_DB", "721"))

OWNER = int(os.environ.get("OWNER", 6940485320))

LOG = -1002087087781

try:
  GROUPS =[]
  for x in (os.environ.get('GROUPS', '-1002032524765').split()):
    GROUPS.append(int(x))
except ValueError:
    raise Exception("Your AUTH GROUPS list does not contain valid integers.")    

try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "5570749629").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")
ADMINS.append(OWNER)


