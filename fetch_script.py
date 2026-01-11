import httpx
import os

# Proxy and URL configuration
PROXY_URL = "http://sony:bypass123@80.225.242.97:3128"
TARGET_URL = "https://hotstarlive.delta-cloud.workers.dev/?token=240bb9-374e2e-3c13f0-4a7xz5"

def fetch_playlist():
    # Browser-like headers to avoid YouTube redirect
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36",
        "Accept": "*/*",
        "Host": "hotstarlive.delta-cloud.workers.dev"
    }
    
    proxies = {"all://": PROXY_URL}

    try:
        with httpx.Client(proxies=proxies, headers=headers, timeout=30.0, follow_redirects=True) as client:
            response = client.get(TARGET_URL)
            
            if "#EXTM3U" in response.text:
                with open("playlist.m3u", "w", encoding="utf-8") as f:
                    f.write(response.text)
                print("SUCCESS: Playlist fetched via Oracle Proxy!")
            else:
                print("FAILURE: Still getting redirected or invalid data.")
                print(response.text[:200]) # Debug info
                exit(1)
    except Exception as e:
        print(f"ERROR: {str(e)}")
        exit(1)

if __name__ == "__main__":
    fetch_playlist()
