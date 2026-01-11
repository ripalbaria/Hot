import requests
import os
import sys

# Get proxy from your GitHub Secrets
PROXY_URL = os.getenv("INDIAN_PROXY") 

# Using the token from your screenshot
TOKEN = "240bb9-347e2e-3c13f0-4a7xz5" 
url = f"https://hotstarlive.delta-cloud.workers.dev/?token={TOKEN}"

# EXACT headers from your screenshot
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; rv:78.0) Gecko/20100101 Firefox/78.0",
    "cache-control": "no-cache, no-store",
    "accept": "*/*",
    "Host": "hotstarlive.delta-cloud.workers.dev",
    "Connection": "Keep-Alive",
    "Accept-Encoding": "gzip"
}

proxies = {
    "http": PROXY_URL,
    "https": PROXY_URL
}

try:
    # Use a session to maintain the Keep-Alive connection seen in your screenshot
    session = requests.Session()
    
    # We disable automatic redirects (allow_redirects=False) to ensure 
    # we aren't being quietly sent to the YouTube page.
    response = session.get(url, headers=headers, proxies=proxies, timeout=30, allow_redirects=False)
    
    # Check if we got a redirect (301/302) instead of the file
    if response.status_code in [301, 302]:
        location = response.headers.get('Location', '')
        print(f"Server tried to redirect to: {location}")
        if "youtube.com" in location:
            print("The worker is blocking this request and redirecting to YouTube.")
        sys.exit(1)

    # Check for the M3U content signature
    if "#EXTM3U" in response.text:
        with open("playlist.m3u", "w", encoding="utf-8") as f:
            f.write(response.text)
        print("M3U file fetched successfully.")
    else:
        print("Error: Received unexpected content (likely HTML).")
        # Log the start of the response to see what we actually got
        print(f"Content preview: {response.text[:100]}")
        sys.exit(1)

except Exception as e:
    print(f"Request failed: {e}")
    sys.exit(1)
