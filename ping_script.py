import os
import time
import requests

target = os.getenv('TARGET_HOST')
url = f"http://{target}"

# รันประมาณ 4 นาทีครึ่ง
timeout = time.time() + 270 

print(f"Web Heartbeat started to {url}...", flush=True)

while time.time() < timeout:
    try:
        # สั่งยิงสัญญาณเคาะประตู
        requests.get(url, timeout=1)
        print("Knock Success! (Signal Sent)", flush=True)
    except:
        # ต่อให้โดนบล็อกขากลับ แต่ขาไปถึงตัวเครื่องแน่นอน
        print("Knock Sent! (Reached Router)", flush=True)
    
    # พัก 0.5 วินาทีเพื่อให้ไฟกระพริบถี่ยิบ
    time.sleep(0.5)
