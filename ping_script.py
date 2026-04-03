import os
import time
import requests # เราจะใช้ตัวนี้แทน

target = os.getenv('TARGET_HOST')
# ใส่ http:// นำหน้า IP หรือ DDNS ของคุณ
url = f"http://{target}" 

timeout = time.time() + 60 * 4.8
print(f"Web Heartbeat started to {url}")

while time.time() < timeout:
    try:
        # พยายามเรียกไปที่หน้ากาก Router (ใส่ timeout สั้นๆ)
        requests.get(url, timeout=2)
        print("Knock! Knock! (Packet Sent)")
    except:
        # ถึงจะ Error (เพราะเราไม่ได้ Login) แต่ Packet ก็วิ่งไปถึง Router แล้ว
        print("Signal Sent (Router Reached)")
    
    time.sleep(1) # กระพริบวินาทีละครั้ง
