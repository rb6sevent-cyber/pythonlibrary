import requests

BOT_TOKEN = "8704965597:AAHBfgSM0gDgTWLC24kgtAWGJ3ktGD3h0qs"
CHAT_ID = "@re838102999xzjjiqlllxppcwihsaod9"

url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

requests.post(
    url,
    data={"chat_id": CHAT_ID, "text":"test"}
)
