from os import getenv, path
from dotenv import load_dotenv
from data import THE_SHUKLA

if path.exists(".env"):
    load_dotenv(".env")

# ------------------------------ REQUIRED ------------------------------ #

API_ID = int(getenv("API_ID", "38551072"))
API_HASH = getenv("API_HASH", "8bbac8430f33a258d0b650f019b76f6d")
SESSION1 = getenv("SESSION1", "BQFwyZ4AKb6IsaUfdM8e_hk2C1qTdHV5pLv8ZAO9QhxxG3mXGc_kT8vdXXPeV4PYgwWdcRK9adhwg4fAU8YzFQSq2bZV7pdDv9Ibylgzrn2of7WNqDAhx0C_4ZZN-XFiw0TXBKe4c1NcLJXkJs68b0lhUCRaPpCq54yuvJgqtnFYBAJG0Vdox6BE0Wyk9Mxbn9kdZN_0HklRZD09NoLAN3mMqoXvWvX8q4HM5-3s4wstXbtNn0EpqfivBfnwr_OQnrtyGnY4laZk4rQ8vpn7j1DEv7eIgFngJbALuDIWmzwZihAnlY1ebCMDDAjDTEYtXB8_8PTqYdYWxT25VxOZdZ12HxBXdQAAAAHgzaW9AA")
BOT_TOKEN = getenv("BOT_TOKEN", "6513440724:AAHPn5TU4o6z5i5q5EtXpY79vv5aO7e951M")

OWNER_ID = list(
    map(int, getenv("OWNER_ID", "8066540989").split())
)

# ------------------------------ OPTIONAL ------------------------------ #

SESSION2 = getenv("SESSION2", "")
SESSION3 = getenv("SESSION3", "")
SESSION4 = getenv("SESSION4", "")
SESSION5 = getenv("SESSION5", "")

UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://github.com/itzshukla/STRANGER-OPUSERBOT"
)

UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "main")

GIT_TOKEN = getenv("GIT_TOKEN", "")

EXTRA_IMG = getenv(
    "EXTRA_IMG",
    "https://files.catbox.moe/uufiry.jpg"
)

HEROKU_APP_NAME = getenv("HEROKU_APP_NAME", "")
HEROKU_API_KEY = getenv("HEROKU_API_KEY", "")

SUDO_USERS = list(
    map(int, getenv("SUDO_USERS", "5533647702").split())
)

for y in OWNER_ID:
    SUDO_USERS.append(y)

for x in THE_SHUKLA:
    SUDO_USERS.append(x)

LOAD = []
NO_LOAD = []
HELPABLE = {}
