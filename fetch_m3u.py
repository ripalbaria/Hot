import requests
import os

# Get proxy from your GitHub Secrets
PROXY_URL = os.getenv("INDIAN_PROXY") 

# IMPORTANT: Ensure this token is fresh from your network logs
TOKEN = "240bb9-374e2e-3c13f0-4a7xz5" 
url = f"https://hotstarlive.delta-cloud.workers.dev/?token={TOKEN}"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Accept": "*/*",
    "Accept-Encoding": "gzip, deflate, br",
    "Host": "hotstarlive.delta-cloud.workers.dev",
    "Connection": "keep-alive",
}

proxies = {
    "http": PROXY_URL,
    "https": PROXY_URL
}

try:
    response = requests.get(url, headers=headers, proxies=proxies, timeout=30)
    
    # Check if the response is M3U content and NOT HTML
    if "#EXTM3U" in response.text:
        with open("playlist.m3u", "w", encoding="utf-8") as f:
            f.write(response.text)
        print("M3U file fetched successfully.")
    else:
        print("Error: Received HTML instead of M3U. The token might be expired or the User-Agent was blocked.")
        # This will prevent the script from overwriting your file with junk HTML
        exit(1) 
            
except Exception as e:
    print(f"Failed to connect: {e}")
    exit(1)
