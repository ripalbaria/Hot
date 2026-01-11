import httpx
import sys

# Oracle Proxy configuration
PROXY = "http://sony:bypass123@80.225.242.97:3128"
URL = "https://hotstarlive.delta-cloud.workers.dev/?token=240bb9-374e2e-3c13f0-4a7xz5"

def fetch():
    # Asli browser headers taaki YouTube redirect na mile
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.5",
        "Connection": "keep-alive",
        "Upgrade-Insecure-Requests": "1"
    }

    try:
        # Naye httpx version mein 'proxy' parameter use hota hai
        with httpx.Client(proxy=PROXY, headers=headers, verify=False, timeout=60.0) as client:
            print(f"Connecting via Oracle Proxy: 80.225.242.97...")
            response = client.get(URL, follow_redirects=True)
            
            # Content check
            if "#EXTM3U" in response.text:
                with open("playlist.m3u", "w", encoding="utf-8") as f:
                    f.write(response.text)
                print("SUCCESS: Playlist saved successfully!")
            else:
                print("FAILURE: Worker redirected to YouTube or blocked IP.")
                # Debug ke liye response ka shuruati hissa
                print(f"Response Start: {response.text[:150]}")
                sys.exit(1)
                
    except Exception as e:
        print(f"CONNECTION ERROR: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    fetch()
