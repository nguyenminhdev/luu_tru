import json
import os,time
import cloudscraper
import requests
import socket
import subprocess
from time import strftime
from time import sleep
from datetime import datetime, timedelta
from bs4 import BeautifulSoup
import time
from colorama import Fore, init
import sys

scraper = cloudscraper.create_scraper()

banner = f"""
{Fore.YELLOW}╔══════════════════════════════════════════════════╗
{Fore.YELLOW}║                                                  {Fore.YELLOW}║
{Fore.YELLOW}║    \033[38;2;0;120;255m ███╗      ███╗            \033[38;2;0;150;100m███╗     ███╗  {Fore.YELLOW}    ║
{Fore.YELLOW}║    \033[38;2;0;120;255m ████╗    ████║            \033[38;2;0;160;100m███║     ███║  {Fore.YELLOW}    ║
{Fore.YELLOW}║    \033[38;2;0;140;255m █████╗  █████║            \033[38;2;0;160;100m███║     ███║  {Fore.YELLOW}    ║
{Fore.YELLOW}║    \033[38;2;0;160;255m ███╔█████╔███║   \033[37m█████╗\033[38;2;0;180;100m   ████████████║  {Fore.YELLOW}    ║
{Fore.YELLOW}║    \033[38;2;0;180;255m ███║╚███╔╝███║   \033[37m╚════╝\033[38;2;0;200;100m   ███╔═════███║  {Fore.YELLOW}    ║
{Fore.YELLOW}║    \033[38;2;0;200;255m ███║ ╚══╝ ███║            \033[38;2;0;230;100m███║     ███║  {Fore.YELLOW}    ║
{Fore.YELLOW}║    \033[38;2;0;220;255m ███║      ███║            \033[38;2;0;230;100m███║     ███║  {Fore.YELLOW}    ║
{Fore.YELLOW}║    \033[38;2;0;220;255m ╚══╝      ╚══╝            \033[38;2;0;230;100m╚══╝     ╚══╝ {Fore.YELLOW}     ║
{Fore.YELLOW}╚══════════════════════════════════════════════════╝
{Fore.WHITE}════════════════════════════════════════════════════
{Fore.RED}  © COPY RIGHT BY M-H    {Fore.WHITE}Phiên Bản: {Fore.YELLOW}GOLIKE SNAPCHAT
{Fore.WHITE}════════════════════════════════════════════════════
{Fore.WHITE}[{Fore.RED}⚡{Fore.WHITE}]{Fore.WHITE} Admin{Fore.WHITE}: \033[38;2;0;220;255mNguyễn Hữu Minh
{Fore.WHITE}[{Fore.RED}⚡{Fore.WHITE}]{Fore.WHITE} Nhóm Zalo{Fore.WHITE}: \033[38;2;0;220;255mhttps://zalo.me/g/axtnqv555
{Fore.WHITE}[{Fore.RED}⚡{Fore.WHITE}]{Fore.WHITE} TikTok{Fore.WHITE}: \033[38;2;0;220;255mhttps://www.tiktok.com/@mh_tool_free
{Fore.WHITE}[{Fore.RED}⚡{Fore.WHITE}]{Fore.WHITE} Youtube{Fore.WHITE}: \033[38;2;0;220;255mhttps://www.youtube.com/@mh_tool_free
{Fore.WHITE}════════════════════════════════════════════════════
"""

os.system('cls' if os.name== 'nt' else 'clear')
print(banner)
print("\033[1;35m╔═════════════════════════════════╗")
print("\033[1;35m║     \033[1;33m🚀 ĐĂNG NHẬP GOLIKE 🚀      \033[1;35m║")
print("\033[1;35m╚═════════════════════════════════╝") 

    # Nhập auth
try:
  Authorization = open("Authorization.txt","x")
  t = open("token.txt","x")
except:
  pass
Authorization = open("Authorization.txt","r")
t = open("token.txt","r")
author = Authorization.read()
token = t.read()
if author == "":
  author = input("\033[1;32m🚀 NHẬP AUTHORIZATION : \033[1;33m")
  token = input("\033[1;32m🚀 NHẬP T : \033[1;33m")
  Authorization = open("Authorization.txt","w")
  t = open("token.txt","w")
  Authorization.write(author)
  t.write(token)
else:
  print(f"\033[1;32m     ⚡ Nhấn Enter để vào TOOL")
  print(f"\033[38;2;0;220;255m               HOẶC ")
  select = input(f"\033[1;32m⚡ Nhập AUTHORIZATION {Fore.RED}(tại đây) \033[1;32mđể vào acc khác: \033[1;33m")

  if select != "":
    author = select
    token = input("\033[1;32m🚀 Nhập T : \033[1;33m")
    Authorization = open("Authorization.txt","w")
    t = open("token.txt","w")
    Authorization.write(author)
    t.write(token)
Authorization.close()
t.close()
os.system('cls' if os.name== 'nt' else 'clear')
print(banner)
print("\033[1;35m╔═════════════════════════════════╗")
print("\033[1;35m║   \033[1;33m🚀 DANH SÁCH ACC SNAPCHAT 🚀  \033[1;35m║")
print("\033[1;35m╚═════════════════════════════════╝") 
print(F"{Fore.RED}🚨 làm tầm 5 job TIKTOK để có thể lấy job SNAPCHAT") 
headers = {
    'Accept': 'application/json, text/plain, */*',
    'Content-Type': 'application/json;charset=utf-8',
    'Authorization': author,
    't': token,
    'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
    'Referer': 'https://app.golike.net/account/manager/fb',
}


def chonacc():
    json_data = {}
    response = scraper.get(
        'https://gateway.golike.net/api/fb-account?limit=200',
        headers=headers,
        json=json_data
    ).json()
    return response

def nhannv(account_id):
    try:
        params = {
            'account_id': account_id,
            'data': 'null',
        }

        response = scraper.get(
            'https://gateway.golike.net/api/advertising/publishers/facebook/jobs',
            headers=headers,
            params=params,
            json={}
        )
        return response.json()
    except Exception as e:
        print()
        return {}

def hoanthanh(ads_id, account_id):
    try:
        json_data = {
            'ads_id': ads_id,
            'account_id': account_id,
            'async': True,
            'data': None,
        }

        response = scraper.post(
            'https://gateway.golike.net/api/advertising/publishers/fb/complete-jobs',
            headers=headers,
            json=json_data,
            timeout=6
        )
        return response.json()
    except Exception as e:
        print()
        return {}

def baoloi(ads_id, object_id, account_id, loai):
    try:
        json_data1 = {
            'description': 'Tôi đã làm Job này rồi',
            'users_advertising_id': ads_id,
            'type': 'ads',
            'provider': 'fb',
            'fb_id': account_id,
            'error_type': 6,
        }

        scraper.post('https://gateway.golike.net/api/report/send', headers=headers, json=json_data1)

        json_data2 = {
            'ads_id': ads_id,
            'object_id': object_id,
            'account_id': account_id,
            'type': loai,
        }

        scraper.post(
            'https://gateway.golike.net/api/advertising/publishers/fb/skip-jobs',
            headers=headers,
            json=json_data2,
        )
    except Exception as e:
        print()

# Gọi chọn tài khoản một lần và xử lý lỗi nếu có
chontkSNAPCHAT = chonacc()

def dsacc():
    if chontkSNAPCHAT.get("status") != 200:
        print("\033[1;31m🚀 Authorization hoặc Token sai 🚀")
        quit()

    # Truy cập đúng danh sách tài khoản nếu bị lồng
    data = chontkSNAPCHAT.get("data", {}).get("data", [])

    if not data:
        print("\033[1;33mKhông có tài khoản SNAPCHAT nào được tìm thấy.")
        return

    for i, acc in enumerate(data):
        try:
            nickname = acc.get("fb_name", "Không rõ")
            print(f'\033[1;36m[{i+1}]\033[1;93m {nickname} \033[1;97m|\033[1;31m✅\033[1;32m Hoạt Động')
        except Exception as e:
            print(f"\033[1;31m❌ Lỗi xử lý tài khoản thứ {i+1}: {e}")
dsacc()
print(f"{Fore.MAGENTA}═══════════════════════════════════")

# Danh sách tài khoản thực nằm ở đây:
accounts = chontkSNAPCHAT.get("data", {}).get("data", [])

while True:
    try:
        luachon = int(input("\033[1;32m🚀 Chọn tài khoản SNAPCHAT: \033[1;33m"))
        while luachon < 1 or luachon > len(accounts):
            luachon = int(input("\033[1;31m🚀 Acc Này Không Có Trong Danh Sách, Hãy Nhập Lại : \033[1;33m"))
        acc_selected = accounts[luachon - 1]
        account_id = acc_selected["id"]
        break
    except Exception as e:
        print("\033[1;31m🚀 Sai Định Dạng 🚀")
        print("⛔ Lỗi chi tiết:", e)
while True:
  try:
    delay = int(input(f"\033[1;32m🚀 Delay: \033[1;33m"))
    break
  except:
    print("\033[1;31m🚀 Sai Định Dạng 🚀")
while True:
  try: 
    doiacc = int(input(f"\033[1;32m🚀 Thất bại bao nhiêu lần thì đổi acc: \033[1;33m"))
    break
  except:
    print("\033[1;31m🚀 Nhập Vào 1 Số 🚀")  
print("\033[1;35m╔═════════════════════════════════╗")
print("\033[1;35m║     \033[1;33m🚀 CHỌN LOẠI NHIỆM VỤ 🚀    \033[1;35m║")
print("\033[1;35m╚═════════════════════════════════╝")
print("\033[1;36m[1] Follow")

while True:
    try:
        loai_nhiem_vu = int(input("\033[1;32m🚀 Chọn loại nhiệm vụ: \033[1;33m"))
        if loai_nhiem_vu in [1]:
            break
        else:
            print("\033[1;31mVui lòng chọn số từ 1 đến 3!")
    except:
        print("\033[1;31mSai định dạng! Vui lòng nhập số.")  

x_follow, y_follow = None, None
print("\033[1;35m╔═════════════════════════════════╗")
print("\033[1;35m║       \033[1;33m🚀 ADB tự động 🚀         \033[1;35m║")
print("\033[1;35m╚═════════════════════════════════╝")
print(f"\033[1;36m[1] Có")
print(f"\033[1;36m[2] Không")
adbyn = input(f"\033[1;32m🚀 Nhập lựa chọn: \033[1;33m")

if adbyn == "1":
    def setup_adb():
      config_file = "adb_config.txt"
      follow_coords_file = "toa_do_follow.txt"

    # Nhập IP và port ADB
      print(f"{Fore.MAGENTA}═══════════════════════════════════")
      print("\033[1;33mBạn có thể xem video hướng dẫn kết nối ADB")
      print("\033[1;33mLink video: \033[38;2;0;220;255mhttps://youtu.be/vcWNzu2XRSE?si=_jFVm9nhSkNGBK_-\033[0m")
      ip = input("\033[1;32mNhập IP của thiết bị ví dụ (192.168.1.2): \033[1;33m")
      adb_port = input("\033[1;32mNhập port của thiết bị ví dụ (39327): \033[1;33m")

      # Kiểm tra và đọc tọa độ từ file nếu tồn tại
      x_follow, y_follow = None, None
    
      if os.path.exists(follow_coords_file):
          with open(follow_coords_file, "r") as f:
               coords = f.read().split("|")
               if len(coords) == 2:
                   x_follow, y_follow = coords
                   print(f"\033[1;32mĐã tìm thấy tọa độ nút follow: X={x_follow}, Y={y_follow}")
      if not os.path.exists(config_file):
           print("\033[1;36mLần đầu chạy, nhập mã ghép nối (6 SỐ) và port ghép nối.\033[0m")
           pair_code = input("\033[1;32mNhập mã ghép nối 6 số ví dụ (322763): \033[1;33m")
           pair_port = input("\033[1;32mNhập port ghép nối ví dụ (44832): \033[1;33m")

           with open(config_file, "w") as f:
               f.write(f"{pair_code}|{pair_port}")
      else:
          with open(config_file, "r") as f:
               pair_code, pair_port = [s.strip() for s in f.read().split("|")]
  
      print("\n\033[1;36m🚀 Đang ghép nối với thiết bị\033[0m")
      os.system(f"adb pair {ip}:{pair_port} {pair_code}")
      time.sleep(2)
  
      print("\033[1;36m🚀 Đang kết nối ADB\033[0m")
      os.system(f"adb connect {ip}:{adb_port}")
      time.sleep(2)
  
      devices = os.popen("adb devices").read()
      if ip not in devices:
        print(f"{Fore.RED}🚀 Kết nối thất bại{Fore.WHITE}")
        exit()
    

       # Yêu cầu nhập tọa độ nếu chưa có
      print("\033[1;35m╔═════════════════════════════════╗")
      print("\033[1;35m║     \033[1;33m🚀 NHẬP TỌA ĐỘ NÚT 🚀       \033[1;35m║")
      print("\033[1;35m╚═════════════════════════════════╝")
    
      if loai_nhiem_vu in [1, 3] and (x_follow is None or y_follow is None):
           x_follow = input("\033[1;32mNhập tọa độ X của nút follow: \033[1;33m")
           y_follow = input("\033[1;32mNhập tọa độ Y của nút follow: \033[1;33m")
           with open(follow_coords_file, "w") as f:
               f.write(f"{x_follow}|{y_follow}")

      return x_follow, y_follow

# Khi gọi hàm setup_adb()
    x_follow, y_follow = setup_adb()
elif adbyn == "2":
    pass
# Thêm phần chọn loại nhiệm vụ sau khi chọn tài khoản và trước khi bắt đầu làm nhiệm vụ
   
dem = 0
tong = 0
checkdoiacc = 0
dsaccloi = []
accloi = ""
os.system('cls' if os.name== 'nt' else 'clear')

print(banner)
print("\033[1;35m╔═════════════════════════════════╗")
print("\033[1;35m║     \033[1;33m🚀 Bắt Đầu Kiếm Tiền 🚀     \033[1;35m║")
print("\033[1;35m╚═════════════════════════════════╝")

while True:
    if checkdoiacc == doiacc:
        dsaccloi.append(chontkSNAPCHAT["data"][luachon - 1]["nickname"])
        print(f"{Fore.WHITE}════════════════════════════════════════════════════")
        print(f"\033[1;31m🚨 Acc SNAPCHAT {dsaccloi} gặp vấn đề 🚨")
        print(f"{Fore.WHITE}════════════════════════════════════════════════════")
        dsacc()
        while True:
            try:
                print(f"{Fore.WHITE}════════════════════════════════════════════════════")
                luachon = int(input("\033[1;32m🚀 Chọn tài khoản mới: \033[1;33m"))
                while luachon > len((chontkSNAPCHAT)["data"]):
                    luachon = int(input("\033[1;31m🚀 Acc Này Không Có Trong Danh Sách, Hãy Nhập Lại : \033[1;33m"))
                account_id = chontkSNAPCHAT["data"][luachon - 1]["id"]
                checkdoiacc = 0
                os.system('cls' if os.name== 'nt' else 'clear')
                for h in banner:
                    print(h,end = "")
                break  
            except:
                print("\033[1;31m🚀 Sai Định Dạng !!!")
    print('\033[1;33m🚀 Đang chuyển job', end="\r")
    max_retries = 3
    retry_count = 0
    nhanjob = None

    while retry_count < max_retries:
        try:
           nhanjob = nhannv(account_id)
           print(f"👉 [DEBUG] Lần thử {retry_count+1}: {nhanjob}")  # ✅ in ra nội dung trả về

           if nhanjob and nhanjob.get("status") == 200:
              data = nhanjob.get("data", {})
              if isinstance(data, dict) and data.get("link") and data.get("object_id"):
                break
              else:
                print("⚠️ Không có job hợp lệ (thiếu link hoặc object_id)")
           else:
               print("⚠️ nhanjob không hợp lệ hoặc status != 200")
           retry_count += 1
           time.sleep(2)

        except Exception as e:
          print(f"❌ Lỗi khi nhận job (lần {retry_count+1}): {e}")
          retry_count += 1
          time.sleep(1)

    if not nhanjob or retry_count >= max_retries:
        continue

    ads_id = nhanjob["data"]["id"]
    link = nhanjob["data"]["link"]
    object_id = nhanjob["data"]["object_id"]
    job_type = nhanjob["data"]["type"]
    (job_type not in ["like"])
    baoloi(ads_id, object_id, account_id, job_type)

    # Mở link và kiểm tra lỗi
    try:
        if adbyn == "1":
            os.system(f'adb shell am start -a android.intent.action.VIEW -d "{link}" > /dev/null 2>&1')
        else:
            subprocess.run(["termux-open-url", link])
        
        for remaining in range(3, 0, -1):
            time.sleep(1)
        print("\r" + " " * 30 + "\r", end="")

    except Exception as e:
        baoloi(ads_id, object_id, account_id, job_type)
        continue

    # Thực hiện thao tác ADB
    if job_type == "follow" and adbyn == "1" and x_follow and y_follow:
        os.system(f"adb shell input tap {x_follow} {y_follow}")

    # Đếm ngược delay
    for remaining_time in range(delay, -1, -1):
        color = "\033[1;36m" if remaining_time % 2 == 0 else "\033[1;33m"
        print(f"\r{color}🚀 M-H |TOOL-v1| {remaining_time}s           ", end="")
        time.sleep(1)
    
    print("\r                          \r", end="") 
    print("\033[1;36m🚀 Đang Nhận Tiền    ",end = "\r")

    # Hoàn thành job
    max_attempts = 2
    attempts = 0
    nhantien = None
    while attempts < max_attempts:
        try:
            nhantien = hoanthanh(ads_id, account_id)
            if nhantien and nhantien.get("status") == 200:
                break
        except:
            pass  
        attempts += 1

    if nhantien and nhantien.get("status") == 200:
        dem += 1
        tien = nhantien["data"]["prices"]
        tong += tien
        local_time = time.localtime()
        hour = local_time.tm_hour
        minute = local_time.tm_min
        second = local_time.tm_sec
        h = hour
        m = minute
        s = second
        if hour < 10:
            h = "0" + str(hour)
        if minute < 10:
            m = "0" + str(minute)
        if second < 10:
            s = "0" + str(second)
                                      
        chuoi = (f"\033[1;35m[\033[1;31m{dem}\033[1;35m]"
                f" \033[1;35m[\033[1;32mDone\033[1;35m]"
                f" \033[1;35m[\033[38;2;0;180;255m{job_type}\033[1;35m]"
                f" \033[1;35m[\033[1;33m+{tien}\033[1;35m]"
                f" \033[1;35m[\033[1;33mTổng: {tong}\033[1;35m]"
                f" \033[1;35m[\033[1;37mTime: {h}:{m}:{s}\033[1;35m]")

        print("                                                    ", end="\r")
        print(chuoi)
        time.sleep(0.7)
        checkdoiacc = 0
    else:
        try:
            baoloi(ads_id, object_id, account_id, nhanjob["data"]["type"])
            print("                                              ", end="\r")
            print("\033[1;31m🚀 Bỏ qua nhiệm vụ ", end="\r")
            sleep(1)
            checkdoiacc += 1
        except:
            pass


while True:
        try:
            devices = subprocess.check_output("adb devices", shell=True, timeout=5).decode()
            if "device" not in devices:
                print(f"{Fore.RED}⚠ Không tìm thấy thiết bị ADB")
                choice = input("Bạn muốn kết nối qua WiFi? (y/n): ").lower()
                if choice == 'y':
                    ip = input("Nhập địa chỉ IP điện thoại: ")
                    subprocess.run(f"adb connect {ip}:5555", shell=True, timeout=5)
                else:
                    print("Vui lòng kết nối thiết bị và thử lại")
                    time.sleep(2)
                    continue
            else:
                break
        except subprocess.TimeoutExpired:
            print(f"{Fore.RED}⏳ Quá thời gian chờ kết nối ADB")
        except Exception as e:
            print(f"{Fore.RED}❌ Lỗi ADB: {str(e)}")
            sys.exit()