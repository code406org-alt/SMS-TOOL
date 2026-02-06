# import requests as req
from os import path, system
import subprocess
import webbrowser
import time
import socket
from datetime import datetime
import requests

def check_internet():
    try:
        System.Clear()
        print(f"{Fore.WHITE}Connecting to GitHub...")
        time.sleep(1)
        requests.get("https://github.com", timeout=5)
        return True
    except:
        System.Clear()
        print(f"{Fore.RED}No Internet Connection!")
        print(f"{Fore.WHITE}Please check your connection and try again.")
        time.sleep(2)
        return False

def get_ip():
    try:
        response = requests.get('https://api.ipify.org', timeout=5)
        return response.text
    except:
        return "Unknown"

def get_user_id():
    return "76932C6C"

def animate_text(text, delay=0.03):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

if path.exists("./requirements.txt"):
    with open("./requirements.txt") as file:
        libs = [i.split("==")[0] for i in file.readlines()]
    
    for lib in libs:
        print(lib)
        try:
            __import__(lib)
        except ModuleNotFoundError:
            system("pip install "+lib)

from pystyle import Col, Center, System
from Plugins.api_list import handler
from colorama import Fore
from Plugins.functions import Functions

r, g = Fore.LIGHTGREEN_EX, Fore.LIGHTYELLOW_EX

if __name__ == "__main__":
    # Check internet connection
    if not check_internet():
        exit()
    
    System.Clear()
    
    # New ASCII Art in Blue
    new_logo = f'''
{Fore.BLUE}@@@@@@   @@@@@@@@@@    @@@@@@              @@@@@@@   @@@@@@    @@@@@@   @@@       
{Fore.BLUE}@@@@@@@   @@@@@@@@@@@  @@@@@@@              @@@@@@@  @@@@@@@@  @@@@@@@@  @@@       
{Fore.BLUE}!@@       @@! @@! @@!  !@@                    @@!    @@!  @@@  @@!  @@@  @@!       
{Fore.BLUE}!@!       !@! !@! !@!  !@!                    !@!    !@!  @!@  !@!  @!@  !@!       
{Fore.BLUE}!!@@!!    @!! !!@ @!@  !!@@!!    @!@!@!@!@    @!!    @!@  !@!  @!@  !@!  @!!       
{Fore.BLUE} !!@!!!   !@!   ! !@!   !!@!!!   !!!@!@!!!    !!!    !@!  !!!  !@!  !!!  !!!       
{Fore.BLUE}     !:!  !!:     !!:       !:!               !!:    !!:  !!!  !!:  !!!  !!:       
{Fore.BLUE}    !:!   :!:     :!:      !:!                :!:    :!:  !:!  :!:  !:!   :!:      
{Fore.BLUE}:::: ::   :::     ::   :::: ::                 ::    ::::: ::  ::::: ::   :: ::::  
{Fore.BLUE}:: : :     :      :    :: : :                  :      : :  :    : :  :   : :: : :{Fore.WHITE}
--------------------------------------------------------------------------------------
--------------------------------------------------------------------------------------
'''
    
    print(new_logo)
    print(f"{Fore.GREEN}[>] connected ✓{Fore.WHITE}")
    
    # Animated info display
    info_lines = [
        f"[>] LOGIN TIME : {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
        f"[>] YOUR IP    : {get_ip()}",
        f"[>] USER ID    : {get_user_id()}",
        "[>] Mode by : MOSTAFA",
        "[>] Author  : git-blackhub and MOSTAFA",
        "[>] GitHub  : https://github.com/code406org-alt",
        "[>] Choices:",
        "[>] 1_call Bomber",
        "[>] 2_Sms Bomber",
        "[>] Enter your choices :"
    ]
    
    for line in info_lines:
        animate_text(line)
        time.sleep(0.1)
    
    input(f"{Fore.WHITE}")
    
    while True:
        try:
            proxy_state = Fore.GREEN + "Enabled" if Functions.proxy_state() else Fore.RED + "Disabled"
            choices = {
                "1": "call",
                "2": "sms"
            }
            
            System.Clear()
            print(Center.XCenter(new_logo))
            print(f"{Fore.GREEN}[>] connected ✓{Fore.WHITE}")
            print(f"{Fore.WHITE}[!] Proxies are {proxy_state}")
            print()
            
            for ch in choices:
                print(f"{Fore.WHITE}   [{Fore.GREEN}{ch}{Fore.WHITE}] {choices[ch].replace('call', 'Call Bomber').replace('sms', 'SMS Bomber')}")
            
            print()
            choice = Functions.get_input(f"{Fore.WHITE}[=] Enter Your Choice: ", lambda x: x in [str(i) for i in choices])
            number = Functions.get_input(f"{Fore.WHITE}[=] Enter the phone number [9xxxxxxxxx]: ", checker=lambda x: x != "" and x.isnumeric() and x.startswith("9") and len(x) == 10)
            count = Functions.get_input(f"{Fore.WHITE}[=] Enter spam count: ", lambda x: x.isnumeric() and int(x) >= 0)

            Functions.start(choices[choice], number, int(count))
            
            # Open YouTube link after execution
            webbrowser.open('https://youtube.com')
            
            # Ask to restart
            System.Clear()
            print(f"{Fore.WHITE}Script completed!")
            input(f"{Fore.WHITE}Press Enter to restart script... (Ctrl+C to exit)")
            
        except KeyboardInterrupt:
            print(f"\n{Fore.BLUE}Exiting...")
            exit()
