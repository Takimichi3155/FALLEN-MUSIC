from os import getenv
from dotenv import load_dotenv

load_dotenv()

get_queue = {}


API_ID = int(getenv("API_ID", "26977508"))
API_HASH = getenv("API_HASH", "396589629e6705c592bc7fe891dc6e37")

ASS_HANDLER = list(getenv("ASS_HANDLER", ".").split())
BOT_TOKEN = getenv("BOT_TOKEN", "6891505280:AAHC-b3eZuYgqw2ZgbWFC1afLYGPZ8bS9xY")

DURATION_LIMIT = int(getenv("DURATION_LIMIT", "900"))
LOGGER_ID = int(getenv("LOGGER_ID", "-1001806464233"))
MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://Obito:YWntQsn1DF3nTyIA@cluster0.amvgyo6.mongodb.net/?retryWrites=true&w=majority")
OWNER_ID = list(map(int, getenv("OWNER_ID", "1962673406").split()))

PING_IMG = getenv("PING_IMG", "https://telegra.ph/file/4cd4f1b11f6ee4f52d117.jpg")
START_IMG = getenv("START_IMG", "https://telegra.ph/file/7e69b99a9545900aef33e.jpg")

SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/Dare_Devils_01")
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", " https://t.me/Seista_Updates")

STRING_SESSION = getenv("STRING_SESSION", "BQGbpOQAJLLflnB6DZNoh6-1YMtnS-gtpULXqsVNoYvTu_p6dRnV6n9h0ZcFwfD4aAiZc7ZAxcWr1uXMM_JkbtqL24x3eC46CkKIoqbVMGCheghyd86E1lKqETzPLgDxrqGt8W-sjFunl_kmYe1xfejxb8NPu3cqKaHOa3TPgXjECVGoYg_SokpAgl75IGKO9VFN_DTvfqDvRyxZjid_yLAYY0ToWjf6unehRrKeXCDzdXS4LNxSU1vLLdjR26fjE03QiQXdhn48PVyTRh-VUI17lKMBzrwibF6wHdkqM59RO6EkVl9fxg8mXQV3p0LnCLhw4NKcGs13vr64-oGrpoG5RFQU6AAAAAGa5dquAA")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "0").split()))
