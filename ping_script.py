import os
import time

target = os.getenv('TARGET_HOST')
timeout = time.time() + 60 * 4.8 

print(f"Heartbeat started to {target}")

while time.time() < timeout:
    # ส่ง ping แค่ 1 ครั้ง (เพื่อให้ Router ไม่มองว่าเป็น Flood)
    os.system(f"ping -c 1 {target}")
    
    # พัก 1 วินาที (เพื่อให้ไฟกระพริบเป็นจังหวะสม่ำเสมอ)
    time.sleep(1)
