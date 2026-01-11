from curl_cffi import requests
import sys

# Oracle Proxy configuration
PROXY = "http://sony:bypass123@80.225.242.97:3128"
URL = "https://hotstarlive.delta-cloud.workers.dev/?token=240bb9-374e2e-3c13f0-4a7xz5"

def fetch():
    proxies = {"http": PROXY, "https": PROXY}
    
    try:
        print(f"Connecting via Oracle Stealth Proxy...")
        # impersonate="chrome110" asli browser ka TLS fingerprint bhejta hai
        response = requests.get(
            URL, 
            proxies=proxies, 
            impersonate="chrome110", 
            timeout=30
        )
        
        if "#EXTM3U" in response.text:
            with open("playlist.m3u", "w", encoding="utf-8") as f:
                f.write(response.text)
            print("SUCCESS: Stealth fetch successful with Oracle!")
        else:
            print("FAILURE: Redirected to YouTube even with Stealth.")
            print(f"Response Preview: {response.text[:100]}")
            sys.exit(1)
            
    except Exception as e:
        print(f"CONNECTION ERROR: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    fetch()
