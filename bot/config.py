from dotenv import load_dotenv
import os

load_dotenv("config.env")

class Telegram:
    API_ID = int(os.getenv("API_ID", "29982493"))
    API_HASH = os.getenv("API_HASH", "3a64a81221c7e35ae16bfc3f236fe4fe")
    BOT_TOKEN = os.getenv("BOT_TOKEN", "7161102507:AAE3fnLw1sfRvuj7IGHS26cfVkpxdgQ1n9M")
    SESSION_STRING = os.getenv("SESSION_STRING", "AQA-i3IABAbGNzHfamlKZnq8weutVtjcP5OSg5a_lr68q2Q7PXZaYKtc0AYStaw_SqOuce4vKNDN3mKqCRKsvbVV3lFWFz5szPM2CYxEmxBGfI0cdK2XjOhcHwBtT8Q0VLM9ziyPETWby3wyvxyM3R7AO17fh6syRh8wOj30Jqs-VVhO1aR4HTNZvleDKKMHRpmMOnDKWRz-sEUo_R8NFiifraJNVJScz7-kp1qnAIOxLzR1taODCMiHev-a80AryLmKTZYd1Y_fyCIwlGe3bmBSwJccagnp2cpFbejIGfXvJoX6-GDI9t3m3AWpRPUE1ddUoIr2PEx_NeE9hk90OOq6UOqC3wAAAAFFv7YAAA")
    PORT = os.getenv("PORT", "8080")
    BASE_URL = os.getenv("BASE_URL", "https://csinexxx-0a017d796f24.herokuapp.com")
    AUTH_CHANNEL = os.getenv("AUTH_CHANNEL", "-1002035410968 -1001944298664").split(", ")
    THEME = os.getenv("THEME", "flatly")
    USERNAME = os.getenv("USERNAME", "admin")
    PASSWORD = os.getenv("PASSWORD", "admin")
    SLEEP_THRESHOLD = int(os.getenv("SLEEP_THRESHOLD", "60"))
    WORKERS = int(os.getenv("WORKERS", "10"))
    MULTI_CLIENT = os.getenv("MULTI_CLIENT", "False").lower() == "true"
