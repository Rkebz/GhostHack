import requests
import threading

# Function to send request and print the response code
def send_request(url, headers):
    try:
        response = requests.get(url, headers=headers, timeout=5)
        if response.status_code == 200:
            print(f"[SUCCESS] Status: {response.status_code} (OK) - URL: {url}")
        elif response.status_code == 503:
            print(f"[ERROR] Server overloaded: {response.status_code} - URL: {url}")
        else:
            print(f"[INFO] Status: {response.status_code} - URL: {url}")
    except requests.exceptions.RequestException as e:
        print(f"[ERROR] Request failed: {e}")
