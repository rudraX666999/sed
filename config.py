import os

API_ID = API_ID = 9741228

API_HASH = os.environ.get("API_HASH", "6f339e8fa827a5147fa2ff03898d610c")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "6287684948:AAFl1ZfAC6McttYkYwYXNf277zu0VrazEDM")

PASS_DB = int(os.environ.get("PASS_DB", "721"))

OWNER = int(os.environ.get("OWNER", 809150135))

LOG = -992473338

try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "809150135").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")
ADMINS.append(OWNER)


