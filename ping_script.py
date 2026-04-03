import os
import time

# ดึงค่า DDNS จากระบบความลับของ GitHub
target = os.getenv('TARGET_HOST')

if not target:
    print("Error: TARGET_HOST not found!")
    exit(1)

print(f"Starting High-Frequency Heartbeat to {target}...")

# รันวนลูป 5 นาทีต่อรอบ
timeout = time.time() + 60 * 4.8 

while time.time() < timeout:
    # ยิงรัว 5 ครั้ง ทุก 0.2 วินาที (ไฟกระพริบถี่ยิบแต่ปลอดภัย)
    os.system(f"ping -c 5 -i 0.2 {target}")
    time.sleep(1) # พัก 1 วินาทีแล้วยิงต่อ
