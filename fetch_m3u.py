import requests
import os

# Get proxy and token from GitHub Secrets/Environment Variables
PROXY_URL = os.getenv("INDIAN_PROXY") # Format: http://username:password@host:port
TOKEN = "240bb9-374e2e-3c13f0-4a7xz5" # From your screenshot

url = f"https://hotstarlive.delta-cloud.workers.dev/?token={TOKEN}"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; rv:78.0) Gecko/20100101 Firefox/78.0",
    "Accept": "*/*",
    "Connection": "keep-alive",
}

proxies = {
    "http": PROXY_URL,
    "https": PROXY_URL
}

try:
    response = requests.get(url, headers=headers, proxies=proxies, timeout=30)
    if response.status_code == 200:
        with open("playlist.m3u", "w", encoding="utf-8") as f:
            f.write(response.text)
        print("M3U file fetched successfully.")
    else:
        print(f"Failed to fetch. Status code: {response.status_code}")
except Exception as e:
    print(f"Error: {e}")

