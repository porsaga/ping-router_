import os
import time
import requests

target = os.getenv('TARGET_HOST')
url = f"http://{target}"

# รันประมาณ 4 นาทีครึ่ง
timeout = time.time() + 270 

print(f"--- Starting Web Heartbeat Monitor to {url} ---", flush=True)

while time.time() < timeout:
    try:
        # พยายามส่งสัญญาณ
        response = requests.get(url, timeout=2)
        
        # ถ้าเข้าถึงได้ (แม้จะติดหน้า Login ก็ตาม)
        print(f"[{time.strftime('%H:%M:%S')}] ✅ REACHED: Status {response.status_code}", flush=True)
        
    except requests.exceptions.ConnectionError:
        # ถ้าเชื่อมต่อได้แต่โดนตัดฉับพลัน (มักจะทำให้ไฟกระพริบแรงที่สุด)
        print(f"[{time.strftime('%H:%M:%S')}] ⚡ TOUCHED: Connection Reset (Router Active)", flush=True)
        
    except requests.exceptions.Timeout:
        # ถ้าส่งไปแล้วเงียบหาย (อาจจะโดน Firewall บล็อกขาตอบกลับ)
        print(f"[{time.strftime('%H:%M:%S')}] ⏳ TIMEOUT: Request sent but no reply", flush=True)
        
    except Exception as e:
        print(f"[{time.strftime('%H:%M:%S')}] ❌ ERROR: {str(e)}", flush=True)
    
    # ปรับความเร็วตรงนี้ (0.5 คือ 2 ครั้งต่อวินาที)
    time.sleep(0.5)
