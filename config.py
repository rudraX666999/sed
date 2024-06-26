import os

API_ID = API_ID = 26484988

API_HASH = os.environ.get("API_HASH", "8d6e625fe3e296b4b6bd4817aca39ec5")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "6409607893:AAEgEPIlrpGOfJIKsg9ZENOQwUBARKTDZPA")

PASS_DB = int(os.environ.get("PASS_DB", "721"))

OWNER = int(os.environ.get("OWNER", 7473123628))

LOG = -4275690616

try:
  GROUPS =[]
  for x in (os.environ.get('GROUPS', '-4275690616 -4278144230').split()):
    GROUPS.append(int(x))
except ValueError:
    raise Exception("Your AUTH GROUPS list does not contain valid integers.")    

try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", " 7473123628 6888054311 ").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")
ADMINS.append(OWNER)


