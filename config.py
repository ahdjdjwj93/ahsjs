## What's up Kangers

import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
admins = {}
SESSION_NAME = getenv("SESSION_NAME", "1BJWap1wBuzoIZRcn7e480u8q94qb5ZbaVfa3zPoU5rrF0p7eisg2yvQHKYD_OsCrlkGesKCgzjVfI4TXq__5lkJL9IlWYz-hifidfwxMi_3LIGwbX9VoSGUAyI0nOCDb-uHwv2Lz7KA9vd7hY8kyPUv4Hel05xQPftXiBI0TPcFnsmjrQ6RF2fYM8Ay9m6LK5XXlraZMoRtwRk0JR6aOXcuRY5VcvSRpmLX6zJgBoOhqvyAHBN-iaS59edaa8mshqZQs_P51vc7naJtuZ17j04Zve9gY-vlN9wmspWXra8zdmo0j0ieh_bxYxl3rVjUXT3YkviA18UUn7cuySEbuF0ve7jDel-o=")
BOT_TOKEN = getenv("BOT_TOKEN", "5779969045:AAFRzuKMKPYH_eNlUE88QFBRC2pigLitzMg")
BOT_NAME = getenv("BOT_NAME", "music")
API_ID = int(getenv("API_ID", "19248481"))
API_HASH = getenv("API_HASH", "56cbbcf271f081d7791ce947b4100277")
OWNER_NAME = getenv("OWNER_NAME", "ahmad")
OWNER_USERNAME = getenv("OWNER_USERNAME", "a000aq")
ALIVE_NAME = getenv("ALIVE_NAME", "hamody")
BOT_USERNAME = getenv("BOT_USERNAME", "hamod_12bot")
OWNER_ID = getenv("OWNER_ID", "5482971964")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "hamody")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "mimi12347")
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
HEROKU_API_KEY = getenv("UPDATES_CHANNEL", "mimi12347")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5482971964").split()))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
ALIVE_IMG = getenv("ALIVE_IMG", "https://te.legra.ph/file/407ce4c57a645c11f65c0.jpg")
START_PIC = getenv("START_PIC", "https://te.legra.ph/file/e22e5d1f0ccd57fa5f677.jpg")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "10"))
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/muntazer995/ing")
IMG_1 = getenv("IMG_1", "https://te.legra.ph/file/402c519808f75bd9b1803.jpg")
IMG_2 = getenv("IMG_2", "https://te.legra.ph/file/c74686f70a1b918060b8e.jpg")
IMG_3 = getenv("IMG_3", "https://te.legra.ph/file/90e3b3aeb77e3e598d66d.jpg")
IMG_4 = getenv("IMG_4", "https://te.legra.ph/file/478f9fa85efb2740f2544.jpg")
IMG_5 = getenv("IMG_5", "https://te.legra.ph/file/2a726c634dbc3b9e8f451.jpg")
IMG_6 = getenv("IMG_6", "https://te.legra.ph/file/430dcf25456f2bb38109f.jpg")
