import os
import time

target = os.getenv('TARGET_HOST')
# รันแค่ 1 นาทีเพื่อทดสอบก่อน
timeout = time.time() + 60 

print(f"Testing connection to {target}...")

while time.time() < timeout:
    # ส่ง ping แค่ครั้งเดียว และรอการตอบกลับ 2 วินาที
    os.system(f"ping -c 1 -W 2 {target}")
    # เว้นระยะห่าง 2 วินาที ให้ Router หายเหนื่อย
    time.sleep(2)
