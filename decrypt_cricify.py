import base64
import requests
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad

# Configuration
# The domain and path were found in your Reqable capture
DATA_URL = "https://cfyhgdgnkkuvn92.top/cats.txt"
# Hex Key and IV extracted from CryptoUtils.kt Smali
KEY_HEX = "3368487a78594167534749382f68616d"
IV_HEX = "557143766b766a656345497a38343256"

def decrypt_data(encrypted_text):
    key = bytes.fromhex(KEY_HEX)
    iv = bytes.fromhex(IV_HEX)
    # Clean the string exactly like the Kotlin logic
    clean_b64 = encrypted_text.strip().replace("\n", "").replace("\r", "").replace(" ", "").replace("\t", "")
    ciphertext = base64.b64decode(clean_b64)
    
    cipher = AES.new(key, AES.MODE_CBC, iv)
    # Uses PKCS5Padding as specified in the provider code
    decrypted = unpad(cipher.decrypt(ciphertext), AES.block_size)
    return decrypted.decode('utf-8')

def generate_m3u(json_data):
    # This logic follows the ChannelStreamResponse data class structure
    m3u_content = "#EXTM3U\n"
    # Note: You would iterate through the JSON here based on the decrypted structure
    # For now, this prints the raw decrypted JSON for your review
    return json_data

def main():
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"}
    response = requests.get(DATA_URL, headers=headers)
    
    if response.status_code == 200:
        decrypted_json = decrypt_data(response.text)
        with open("playlist.json", "w") as f:
            f.write(decrypted_json)
        print("Success: playlist.json created.")
    else:
        print(f"Failed to fetch data: {response.status_code}")

if __name__ == "__main__":
    main()

