import subprocess
import sys

required_packages = {
    "requests": "requests",
    "pystyle": "pystyle",
    "colorama": "colorama",
    "rich": "rich",
    "bs4": "beautifulsoup4",
    "cloudscraper": "cloudscraper"
}


missing = False

for module_name, pip_name in required_packages.items():
    try:
        __import__(module_name)
    except ImportError:
        print(f"📦 Đang cài đặt thư viện thiếu: {pip_name} ...")
        try:
            subprocess.check_call([sys.executable, "-m", "pip", "install", pip_name])
            missing = True
        except Exception as e:
            print(f"❌ Cài thư viện {pip_name} thất bại: {e}")
            missing = True

if missing:
    print("\n✅ Đã cài đặt thư viện cần thiết.")
    print("🔁 Vui lòng **chạy lại tool**.")
    sys.exit()

import os
import sys
import json
import base64
import uuid
import time
import socket
import random
import string
from datetime import datetime, timedelta
from random import randint
from time import sleep, strftime

import requests
import cloudscraper
from bs4 import BeautifulSoup
from colorama import Fore, Style, init
from pystyle import Write, Colors
from rich.console import Console
from rich.text import Text

init(autoreset=True)


os.system('cls' if os.name=='nt' else 'clear')
red = "\033[1;31m"
luc = "\033[1;32m"
vang = "\033[1;33m"
cam = "\033[38;5;208m"
tim = "\033[1;35m"
lam = "\033[1;36m"
trang = "\033[1;37m"
listck = []
listjob = []

import socket

def kiem_tra_mang():
    try:
        socket.create_connection(("8.8.8.8", 53), timeout=3)
    except OSError:
        print("Mạng không ổn định hoặc bị mất kết nối. Vui lòng kiểm tra lại mạng.")

kiem_tra_mang()


def banner():
    print(f"""{Fore.YELLOW}╔══════════════════════════════════════════════════╗
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
{Fore.RED}  © COPY RIGHT BY M-H    {Fore.WHITE}Phiên Bản: {Fore.YELLOW}TOOL GỘP 
{Fore.WHITE}════════════════════════════════════════════════════
{Fore.WHITE}[{Fore.RED}⚡{Fore.WHITE}]{Fore.WHITE} Admin{Fore.WHITE}: \033[38;2;0;220;255mNguyễn Hữu Minh
{Fore.WHITE}[{Fore.RED}⚡{Fore.WHITE}]{Fore.WHITE} Nhóm Zalo{Fore.WHITE}: \033[38;2;0;220;255mhttps://zalo.me/g/axtnqv555
{Fore.WHITE}[{Fore.RED}⚡{Fore.WHITE}]{Fore.WHITE} TikTok{Fore.WHITE}: \033[38;2;0;220;255mhttps://www.tiktok.com/@mh_tool_free
{Fore.WHITE}[{Fore.RED}⚡{Fore.WHITE}]{Fore.WHITE} Youtube{Fore.WHITE}: \033[38;2;0;220;255mhttps://www.youtube.com/@mh_tool_free
{Fore.WHITE}════════════════════════════════════════════════════
""")
banner()

console = Console()
def get_shortened_link_yeumoney(url):
    token = "cff2bc188aaf5e58257f801a6954129bc999212b494460c5476c2451210521d2"  # Thay bằng token của bạn
    api_url = f"https://yeumoney.com/QL_api.php?token={token}&format=text&url={url}"

    try:
        response = requests.get(api_url, timeout=5)
        if response.status_code == 200:
            return response.text.strip()  # Lấy link rút gọn
        else:
            return "Lỗi khi kết nối API!"
    except Exception as e:
        return f"Lỗi get link"

# Hàm tạo key ngẫu nhiên
def generate_random_key(length=8):
    """Tạo chuỗi ngẫu nhiên với chữ cái + số."""
    characters = string.ascii_uppercase + string.digits
    return ''.join(random.choices(characters, k=length))

def generate_key(is_admin=False):
    """Tạo key, admin key không hết hạn."""
    if is_admin:
        return "NHM-NTH"  # Key admin không có ngày hết hạn
    else:
        return f"NHM-{generate_random_key(10)}"  # Key user

# Hàm lưu key vào file (chỉ lưu 1 key)
def save_key_to_file(key):
    """Lưu key vào file, ghi đè để chỉ lưu 1 key."""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # Thời gian lưu key
    with open("key.txt", "w") as f:  # Dùng mode "w" để ghi đè
        f.write(f"{key} | {timestamp}\n")

# Hàm kiểm tra và xóa key nếu đã qua 00:00
def clean_expired_key():
    """Xóa key nếu đã qua 00:00 của ngày hôm sau."""
    if not os.path.exists("key.txt"):
        return
    
    updated_lines = []
    current_time = datetime.now()
    current_date = current_time.date()  # Ngày hiện tại
    
    with open("key.txt", "r") as f:
        lines = f.readlines()
        for line in lines:
            try:
                key, timestamp = line.strip().split(" | ")
                key_time = datetime.strptime(timestamp, "%Y-%m-%d %H:%M:%S")
                key_date = key_time.date()  # Ngày tạo key
                # Nếu key không phải admin và đã qua ngày mới (00:00), bỏ qua
                if not key.startswith("NHM-NTH") and key_date == current_date:
                    updated_lines.append(line)
                elif key.startswith("NHM-NTH"):  # Giữ lại key admin
                    updated_lines.append(line)
            except:
                continue
    
    # Ghi lại key còn hiệu lực (nếu không còn key nào thì file sẽ trống)
    with open("key.txt", "w") as f:
        f.writelines(updated_lines)

# Hàm kiểm tra key hợp lệ
def is_valid_key(key, expected_key):
    """Kiểm tra key có hợp lệ không."""
    clean_expired_key()  # Dọn dẹp key hết hạn trước
    
    if key == "NHM-NTH":
        return True  # Key admin hợp lệ mọi lúc
    elif key == expected_key:  # So sánh với key đã tạo
        return True
    return False

# Hàm kiểm tra key đã lưu và còn hạn không
def check_stored_key():
    """Kiểm tra xem có key nào còn hạn trong file không, trả về key nếu hợp lệ."""
    clean_expired_key()  # Dọn dẹp key hết hạn trước
    
    if not os.path.exists("key.txt"):
        return None, None
    
    current_time = datetime.now()
    current_date = current_time.date()  # Ngày hiện tại
    with open("key.txt", "r") as f:
        for line in f:
            try:
                stored_key, timestamp = line.split(" | ")
                stored_key = stored_key.strip()
                key_time = datetime.strptime(timestamp.strip(), "%Y-%m-%d %H:%M:%S")
                key_date = key_time.date()  # Ngày tạo key
                if stored_key == "NHM-NTH":
                    return stored_key, stored_key  # Key admin luôn hợp lệ
                elif stored_key.startswith("NHM-"):
                    if key_date == current_date:  # Key chỉ hợp lệ trong cùng ngày
                        return stored_key, stored_key
            except:
                continue
    return None, None

# ======= Chạy Tool =======
try:
    admin_key = "NHM-NTH"
    
    # Kiểm tra xem có key nào còn hạn trong file không
    stored_key, user_key = check_stored_key()
    
    # Nếu không có key còn hạn, tạo key mới và yêu cầu người dùng vượt link
    if not stored_key:
        user_key = generate_key(is_admin=False)
        # Tạo link YeuMoney chứa key
        link_can_rut = f"https://flowing-silo-450510-e1.web.app/key/?ma={user_key}"  # Thay bằng URL mới của bạn
        short_link = get_shortened_link_yeumoney(link_can_rut)
        console.print(f"[bold red][bold yellow]LINK[/bold yellow] [bold white]|[/bold white][bold magenta]VƯỢT LINK ĐỂ LẤY KEY[/bold magenta][/bold red][bold green]: {short_link}[/bold green]")
        
        while True:
            nhap_key = console.input("[bold blue][[bold red]NHẬP KEY[bold blue]][/bold blue][bold yellow]==>> [/bold yellow]").strip()
            
            if is_valid_key(nhap_key, user_key):
                # Lưu key vừa nhập thành công vào file (ghi đè key cũ)
                save_key_to_file(nhap_key)
                print("\n✅ Key hợp lệ! Đang vào Tool...", end="\r")
                time.sleep(3)  # Chờ 3 giây trước khi vào tool
                print("\033[F\033[K" * 3, end="")  # Xóa 3 dòng vừa in
                break  
            else:
                print("\n❌ Key không hợp lệ. Vui lòng vượt link để lấy key!", end="\r")
                time.sleep(2)
                print("\033[F\033[K" * 2, end="")  # Xóa 2 dòng vừa in
    else:
        # Nếu có key còn hạn, hiển thị link YeuMoney nhưng không yêu cầu nhập lại
        link_can_rut = f"https://flowing-silo-450510-e1.web.app/key/?ma={user_key}"
        short_link = get_shortened_link_yeumoney(link_can_rut)
        console.print(f"[bold green]Key [bold blue]{stored_key}[bold green] còn hạn. Đang vào Tool...[/bold green]")
        time.sleep(2)  # Chờ 3 giây trước khi vào tool
        print("\033[F\033[K" * 4, end="")

except Exception as e:
    console.print(f"[bold red]ErrolKey: {e}[/bold red]")
    sys.exit()
os.system("cls" if os.name == "nt" else "clear")

from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich import box
from colorama import init, Fore
import os, time
banner()
init(autoreset=True)
console = Console()

def clear():
    os.system("clear" if os.name != "nt" else "cls")

def show_menu():
    table = Table(
        title="[bold yellow]🔥 MENU TOOL TỔNG HỢP 2025 🔥[/bold yellow]",
        box=box.ROUNDED,
        show_lines=True,
        title_style="bold bright_magenta"
    )

    table.add_column("STT", style="bold cyan", justify="center")
    table.add_column("    Tên Tool", style="bold green", justify="left")
    table.add_column("      Mô tả", justify="left")

    rows = [
        ("1", "👍 GOLIKE TIKTOK", "[green]ADB or Auto ✅[/green]"),
        ("2", "👻 GOLIKE SNAPCHAT", "[green]ADB or Auto click ✅[/green]"),
        ("3", "🐦 GOLIKE TWITTER", "[green]Cookie ✅[/green]"),
        ("4", "📘 TTC FACEBOOK", "[green]Cookie ✅[/green]"),
        ("5", "🎵 TTC TIKTOK", "[red]ADB or Auto click ❌[/red]"),
        ("6", "📘 TDS FACEBOOK", "[red]Cookie ❌[/red]"),
        ("7", "🎵 TDS TIKTOK", "[green]Auto click ✅[/green]")
    ]

    for i, (stt, name, desc) in enumerate(rows):
        style = "on grey15" if i % 2 == 0 else "on black"
        table.add_row(stt, name, desc, style=style)

    console.print(table)

def main():
    while True:
        clear()
        banner()
        show_menu()
        try:
            choice = input(f"\n\033[1;35m[🚀] Nhập STT: {Fore.CYAN}").strip()
        except KeyboardInterrupt:
            console.print("\n[red]⛔ Thoát...[/]")
            break
        kiem_tra_mang()
        if choice == "1":
            try: 
              kiem_tra_mang()
              code = requests.get('https://raw.githubusercontent.com/nguyenminhdev/luu_tru/main/go_tik.py').text
              exec(code, globals())
            except:
              sys.exit()  
        elif choice == "2":
            try:
              kiem_tra_mang()
              code = requests.get('https://raw.githubusercontent.com/nguyenminhdev/luu_tru/main/go_snap.py').text
              exec(code, globals())
            except:
              sys.exit()
        elif choice == "3":
            try:
              kiem_tra_mang()
              code = requests.get('https://raw.githubusercontent.com/nguyenminhdev/luu_tru/main/go_twitter.py').text
              exec(code, globals())
            except:
              sys.exit()
        elif choice == "4":
            try: 
              kiem_tra_mang()
              code = requests.get('https://raw.githubusercontent.com/nguyenminhdev/luu_tru/main/ttc_fb.py').text
              exec(code, globals())
            except:
              sys.exit()
        elif choice == "5":
            try:
              print(f"{Fore.RED}Chưa cập nhập, vui lòng chọn tool online")
              exit()
              kiem_tra_mang()
              code = requests.get('https://raw.githubusercontent.com/nguyenminhdev/luu_tru/main/ttc_tt.py').text
              exec(code, globals())
            except:
              sys.exit()
        elif choice == "6":
            try:
              print(f"{Fore.RED}Chưa cập nhập, vui lòng chọn tool online")
              exit()
              kiem_tra_mang()
              code = requests.get('https://raw.githubusercontent.com/nguyenminhdev/luu_tru/main/tds_fb.py').text
              exec(code, globals())
            except:
              sys.exit()
        elif choice == "7":
            try:
              kiem_tra_mang()
              code = requests.get('https://raw.githubusercontent.com/nguyenminhdev/luu_tru/main/tds_tik.py').text
              exec(code, globals())
            except:
              sys.exit()
        else:
            console.print("[bold red]Lựa chọn không hợp lệ![/]")
            time.sleep(1)

if __name__ == "__main__":
    main()