import json
import os,time
import cloudscraper
import requests
import socket
import subprocess
import uiautomator2 as u2
from time import strftime
from time import sleep
from datetime import datetime, timedelta
from bs4 import BeautifulSoup
import time
from colorama import Fore, init
import sys

init(autoreset=True)

def xoa():
   os.system('cls' if os.name== 'nt' else 'clear')
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
{Fore.RED}  © COPY RIGHT BY M-H   {Fore.WHITE}Phiên Bản: {Fore.YELLOW}GOLIKE TIKTOK PC
{Fore.WHITE}════════════════════════════════════════════════════
{Fore.WHITE}[{Fore.RED}⚡{Fore.WHITE}]{Fore.WHITE} Admin{Fore.WHITE}: \033[38;2;0;220;255mNguyễn Hữu Minh
{Fore.WHITE}[{Fore.RED}⚡{Fore.WHITE}]{Fore.WHITE} Nhóm Zalo{Fore.WHITE}: \033[38;2;0;220;255mhttps://zalo.me/g/axtnqv555
{Fore.WHITE}[{Fore.RED}⚡{Fore.WHITE}]{Fore.WHITE} TikTok{Fore.WHITE}: \033[38;2;0;220;255mhttps://www.tiktok.com/@mh_tool_free
{Fore.WHITE}[{Fore.RED}⚡{Fore.WHITE}]{Fore.WHITE} Youtube{Fore.WHITE}: \033[38;2;0;220;255mhttps://www.youtube.com/@mh_tool_free
{Fore.WHITE}════════════════════════════════════════════════════
"""
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
  kiem_tra_mang()
  if select != "":
    author = select
    token = input("\033[1;32m🚀 Nhập T : \033[1;33m")
    Authorization = open("Authorization.txt","w")
    t = open("token.txt","w")
    Authorization.write(author)
    t.write(token)
Authorization.close()
t.close()
xoa()
print(banner)
print("\033[1;35m╔═════════════════════════════════╗")
print("\033[1;35m║   \033[1;33m🚀 DANH SÁCH ACC TIKTOK 🚀    \033[1;35m║")
print("\033[1;35m╚═════════════════════════════════╝")  
headers = {
    'Accept': 'application/json, text/plain, */*',
    'Content-Type': 'application/json;charset=utf-8',
    'Authorization': author,
    't': token,
    'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
    'Referer': 'https://app.golike.net/account/manager/tiktok',
}

scraper = cloudscraper.create_scraper()
def chonacc():
    json_data = {}
    response = scraper.get(
        'https://gateway.golike.net/api/tiktok-account',
    
        headers=headers,
        json=json_data
     ).json()
    return response
def nhannv(account_id):
        params = {
            'account_id': account_id,
            'data': 'null',
        }
   
        response = scraper.get(
            'https://gateway.golike.net/api/advertising/publishers/tiktok/jobs',
            headers=headers,
            params=params,
            json={}
        )
        return response.json()
def hoanthanh(ads_id, account_id):
        json_data = {
            'ads_id': ads_id,
            'account_id': account_id,
            'async': True,
            'data': None,
        }

        response = scraper.post(
            'https://gateway.golike.net/api/advertising/publishers/tiktok/complete-jobs',
            headers=headers,
            json=json_data,
            timeout=12
        )
        return response.json()

def process_job(link, job_type):
    try:
        devices = subprocess.check_output("adb devices", shell=True).decode()
        if "device" not in devices:
            print(f"{Fore.RED}Mất kết nối ADB! Vui lòng kiểm tra lại.")
            return False

        subprocess.run(f"adb shell am start -a android.intent.action.VIEW -d \"{link}\"", 
                      shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)
        time.sleep(2)

        if job_type in ["like", "follow"]:
            return nhan_nut_theo_text(job_type)
        else:
            return False
    except subprocess.CalledProcessError as e:
       error_output = e.stderr.decode() if e.stderr else "Không có thông tin lỗi chi tiết."
       print("Vui lòng kiểm tra lại kết nối ADB và thiết bị.")
       return False
    except Exception as e:
        return False

def baoloi(ads_id, object_id, account_id, loai):
        json_data1 = {
            'description': 'Tôi đã làm Job này rồi',
            'users_advertising_id': ads_id,
            'type': 'ads',
            'provider': 'tiktok',
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
            'https://gateway.golike.net/api/advertising/publishers/tiktok/skip-jobs',
            headers=headers,
            json=json_data2,
        )

# Gọi chọn tài khoản một lần và xử lý lỗi nếu có
chontktiktok = chonacc()

def dsacc():
  if chontktiktok.get("status") != 200:  
    print("\033[1;31m🚀 Authorization hoăc T sai 🚀")
    quit()
  for i in range(len(chontktiktok["data"])):
    print(f'\033[1;36m[{i+1}]\033[1;93m {chontktiktok["data"][i]["nickname"]} \033[1;97m|\033[1;31m✅\033[1;32m Hoạt Động')
dsacc() 
print(f"{Fore.MAGENTA}═══════════════════════════════════")
while True:
  try:
    luachon = int(input("\033[1;32m🚀 Chọn tài khoản TIKTOK: \033[1;33m"))
    while luachon > len((chontktiktok)["data"]):
      luachon = int(input("\033[1;32m🚀 Acc Này Không Có Trong Danh Sách , Nhập Lại : \033[1;33m"))
    account_id = chontktiktok["data"][luachon - 1]["id"]
    break  
  except:
    print("\033[1;31m🚀 Sai Định Dạng 🚀") 
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
print("\033[1;36m[2] Like")
print("\033[1;36m[3] Cả hai (Follow và Like)")

while True:
    try:
        loai_nhiem_vu = int(input("\033[1;32m🚀 Chọn loại nhiệm vụ: \033[1;33m"))
        if loai_nhiem_vu in [1, 2, 3]:
            break
        else:
            print("\033[1;31mVui lòng chọn số từ 1 đến 3!")
    except:
        print("\033[1;31mSai định dạng! Vui lòng nhập số.")  


d = u2.connect()  # Kết nối thiết bị Android qua Wi-Fi hoặc USB
def nhan_nut_theo_text(job_type):
    text_map = {
        'like': ['Like', 'Thích'],
        'follow': ['Follow', 'Theo dõi']
    }

    if job_type not in text_map:
        return False

    for text in text_map[job_type]:
        if d(text=text).exists(timeout=2):
            d(text=text).click()
            return True
    return False
    
dem = 0
tong = 0
checkdoiacc = 0
dsaccloi = []
accloi = ""


xoa()
print(banner)
print("\033[1;35m╔═════════════════════════════════╗")
print("\033[1;35m║     \033[1;33m🚀 Bắt Đầu Kiếm Tiền 🚀     \033[1;35m║")
print("\033[1;35m╚═════════════════════════════════╝")

while True:
    if checkdoiacc == doiacc:
        dsaccloi.append(chontktiktok["data"][luachon - 1]["nickname"])
        print(f"{Fore.WHITE}════════════════════════════════════════════════════")
        print(f"\033[1;31m🚨 Acc Tiktok {chontktiktok['data'][luachon - 1]['nickname']} gặp vấn đề, chuyển sang acc khác 🚨")
        print(f"{Fore.WHITE}════════════════════════════════════════════════════")
        dsacc()
        while True:
            try:
                print(f"{Fore.WHITE}════════════════════════════════════════════════════")
                luachon = int(input("\033[1;32m🚀 Chọn tài khoản mới: \033[1;33m"))
                while luachon > len((chontktiktok)["data"]):
                    luachon = int(input("\033[1;31m🚀 Acc Này Không Có Trong Danh Sách, Hãy Nhập Lại : \033[1;33m"))
                account_id = chontktiktok["data"][luachon - 1]["id"]
                checkdoiacc = 0
                xoa()
                print(banner) # In lại banner sau khi clear màn hình
                print("\033[1;35m╔═════════════════════════════════╗")
                print("\033[1;35m║     \033[1;33m🚀 Bắt Đầu Kiếm Tiền 🚀     \033[1;35m║")
                print("\033[1;35m╚═════════════════════════════════╝")
                break  
            except ValueError:
                print("\033[1;31m🚀 Sai Định Dạng !!! Vui lòng nhập số.")

    print('\033[1;33m🔄 Đang tìm job...', end='\r')
    try:
        nhanjob = nhannv(account_id)
        #if nhanjob and nhanjob.get("status") == 200:
           #data = nhanjob.get("data", {})
           #print("\n📦 DỮ LIỆU JOB:")
           #print(json.dumps(nhanjob, indent=2, ensure_ascii=False))  # <-- In ra full JSON trả về từ GoLike
        if not nhanjob or nhanjob.get("status") != 200:
            time.sleep(2)
            continue
        ads_id = nhanjob["data"]["id"]
        link = nhanjob["data"]["link"]
        object_id = nhanjob["data"]["object_id"]
        job_type = nhanjob["data"]["type"]

        if job_type == "follow":
           data = nhanjob["data"]
        if data["count_success"] <= 10 and data["count_is_run"] <= 10 and data["viewer"] < 50:
           baoloi(ads_id, object_id, account_id, job_type)
           time.sleep(0.5)
           continue
        
        # Kiểm tra loại job có phù hợp không với lựa chọn của người dùng
        if (loai_nhiem_vu == 1 and job_type != "follow") or \
           (loai_nhiem_vu == 2 and job_type != "like") or \
           (loai_nhiem_vu == 3 and job_type not in ["follow", "like"]):
            baoloi(ads_id, object_id, account_id, job_type)
            continue
            
    except Exception as e:
        time.sleep(2)
        continue
    
    job_processed_successfully = process_job(link, job_type, )
    
    if job_processed_successfully:
        # Đếm ngược delay
        for remaining_time in range(delay, -1, -1):
           color = "\033[1;36m" if remaining_time % 2 == 0 else "\033[1;33m"
           print(f"\r{color}🚀 M-H |TOOL-v1| {remaining_time}s           ", end="")
           time.sleep(1)
    
        print("\r                          \r", end="") 
        print("\033[1;36m🚀 Đang Nhận Tiền    ",end = "\r")
        try:
           nhantien = hoanthanh(ads_id, account_id)
        except requests.exceptions.ReadTimeout:
           baoloi(ads_id, object_id, account_id, job_type)
           checkdoiacc += 1
           time.sleep(1)
           continue
        except Exception as e:
           baoloi(ads_id, object_id, account_id, job_type)
           checkdoiacc += 1
           time.sleep(1)
           continue
        
        if nhantien and nhantien.get("status") == 200:
            dem += 1
            tien = nhantien["data"]["prices"]
            tong += tien
            current_time = time.strftime("%H:%M:%S")
            
            chuoi = (f"\033[1;35m[\033[1;31m{dem}\033[1;35m]"
                f" \033[1;35m[\033[1;32mDone\033[1;35m]"
                f" \033[1;35m[\033[38;2;0;180;255m{job_type}\033[1;35m]"
                f" \033[1;35m[\033[1;33m+{tien}\033[1;35m]"
                f" \033[1;35m[\033[1;33mTổng: {tong}\033[1;35m]"
                f" \033[1;35m[\033[1;37mTime: {current_time}\033[1;35m]")

            print("                                                    ", end="\r") # Xóa dòng đếm ngược
            print(chuoi)
            time.sleep(0.7)
            checkdoiacc = 0  # Reset counter lỗi     
        else:
            baoloi(ads_id, object_id, account_id, job_type)
            checkdoiacc += 1
            time.sleep(1)
            
    else:
        baoloi(ads_id, object_id, account_id, job_type)
        checkdoiacc += 1
        time.sleep(1)
