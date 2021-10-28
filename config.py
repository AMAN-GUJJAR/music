from os import getenv

from dotenv import load_dotenv

load_dotenv()
que = {}
SESSION_NAME = getenv("SESSION_NAME", "session")
BOT_TOKEN = getenv("BOT_TOKEN", "")
BOT_NAME = getenv("BOT_NAME", "")
admins = {}
API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH", "")
SUPPORT_GROUP = getenv("SUPPORT_GROUP", "")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "")
OWNER_NAME = getenv("OWNER_NAME", "")

BOT_USERNAME = int(getenv("BOT_USERNAME"))

DURATION_LIMIT = int(getenv("DURATION_LIMIT", "10"))

COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ !").split())

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "").split()))
