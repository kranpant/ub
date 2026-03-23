from os import getenv, path
from dotenv import load_dotenv
from data import THE_SHUKLA

if path.exists(".env"):
    load_dotenv(".env")

# ------------------------------ REQUIRED ------------------------------ #

API_ID = int(getenv("API_ID", "27433131"))
API_HASH = getenv("API_HASH", "7f8d967471ccadf83df1f199769b43e7")
SESSION1 = getenv("SESSION1", "BQIXARUABg05Bpcj9b50oLkmolwsFUtoEWQinQpexSWKy9xzrGt-cP5RXfStvTqhcV2uMmBhoZ7DJTuwm2m3CSfISnz3kVFKcPeIp48k9SjoBXotP3it0ezAJOuC2cGSPTn8PtFoUv5mGtycBCH64-hNxnI7xyXINx8eW5d4npLw20um6R6AR0bF0VRA5rnxz_HgwQqYFah2Gyj2-qOPYiZ11vayjBgpvwI4V4F2ASlTA6kFig5iZSGrm19uLdvhaqsv-5kC4g7If_2fq9BswX_Cqq0MIpBiHJgRSHc4x1kAgwyQkRViFmEJB_Upn2C4JzXON1fXrW54I-SbORdOaIFfP3_saAAAAAGVFGUPAA")
BOT_TOKEN = getenv("BOT_TOKEN", "6513440724:AAHPn5TU4o6z5i5q5EtXpY79vv5aO7e951M")

OWNER_ID = list(
    map(int, getenv("OWNER_ID", "6796109071").split())
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
    map(int, getenv("SUDO_USERS", "6796109071").split())
)

for y in OWNER_ID:
    SUDO_USERS.append(y)

for x in THE_SHUKLA:
    SUDO_USERS.append(x)

LOAD = []
NO_LOAD = []
HELPABLE = {}
