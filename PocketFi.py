import os
import sys
import time
import requests
from colorama import Fore, Style, init

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def art():
    print("\033[1;91m" + r""" ______  _               _    
 | ___ \| |             | |   
 | |_/ /| |  __ _   ___ | | __
 | ___ \| | / _` | / __|| |/ /
 | |_/ /| || (_| || (__ |   < 
 \____/ |_| \__,_| \___||_|\_\
""" + "\033[0m" + "\033[1;92m" + r""" ______                                   
 |  _  \                                  
 | | | | _ __   __ _   __ _   ___   _ __  
 | | | || '__| / _` | / _` | / _ \ | '_ \ 
 | |/ / | |   | (_| || (_| || (_) || | | |
 |___/  |_|    \__,_| \__, | \___/ |_| |_|
                       __/ |              
                      |___/               
""" + "\033[0m" + "\033[1;93m" + r"""  _   _               _                
 | | | |             | |               
 | |_| |  __ _   ___ | | __  ___  _ __ 
 |  _  | / _` | / __|| |/ / / _ \| '__|
 | | | || (_| || (__ |   < |  __/| |   
 \_| |_/ \__,_| \___||_|\_\ \___||_| 
""" + "\033[0m\n\033[1;96m---------------------------------------\033[0m\n\033[1;93mScript created by: Black Dragon Hacker\033[0m\n\033[1;92mJoin Telegram: \nhttps://t.me/BlackDragonHacker007\033[0m\n\033[1;91mVisit my GitHub: \nhttps://github.com/BlackDragonHacker\033[0m\n\033[1;96m---------------------------------------\033[0m\n\033[1;38;2;139;69;19;48;2;173;216;230m--------------[PocketFi Bot]--------------\033[0m\n\033[1;96m---------------------------------------\033[0m")

def countdown_timer(seconds):
    while seconds > 0:
        mins, secs = divmod(seconds, 60)
        hours, mins = divmod(mins, 60)
        print(f"{Fore.CYAN + Style.BRIGHT}Wait {hours:02}:{mins:02}:{secs:02}", end='\r')
        time.sleep(1)
        seconds -= 1
    print("Wait 00:00:00          ", end='\r')

def load_tokens(filename):
    with open(filename, 'r') as file:
        return [line.strip() for line in file if line.strip()]

def load_proxies(filename):
    with open(filename, 'r') as file:
        return [line.strip() for line in file if line.strip()]

def get_headers(token, proxy=None):
    return {
        "accept": "*/*",
   	 "accept-language": "en-US,en;q=0.9",
   	 "sec-ch-ua": "\"Chromium\";v=\"111\", \"Not(A:Brand\";v=\"8\"",
    	"sec-ch-ua-mobile": "?1",
    	"sec-ch-ua-platform": "\"Android\"",
    	"sec-fetch-dest": "empty",
    	"sec-fetch-mode": "cors",
    	"sec-fetch-site": "cross-site",
    	"telegramrawdata": token,
    	"x-paf-t": "Abvx2NzMTM=="
    }

def login(token, proxy=None):
    url = "https://pocketfi.app/mining?tgWebAppStartParam=ref-5496274031-alliance-sftearning_squad"
    headers = {
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "accept-language": "en-US,en;q=0.9",
        "sec-ch-ua": "\"Chromium\";v=\"111\", \"Not(A:Brand\";v=\"8\"",
        "sec-ch-ua-mobile": "?1",
        "sec-ch-ua-platform": "\"Android\"",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "navigate",
        "sec-fetch-site": "cross-site",
        "upgrade-insecure-requests": "1"
    }

    try:
        response = requests.get(url, headers=headers, proxies=proxy, allow_redirects=True)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"{Fore.RED + Style.BRIGHT}Request failed: {e}")
    except ValueError as ve:
        print(f"{Fore.RED + Style.BRIGHT}JSON parsing failed: {ve}")

def user_data(token, proxy=None):
    url_1 = "https://gm.pocketfi.org/mining/getUserMining"
    url_2 = "https://prod-api.bigpump.app/api/v1/users/me"
    
    headers = get_headers(token, proxy)
    
    try:
        response_1 = requests.get(url_1, headers=headers, proxies=proxy, allow_redirects=True)
        response_2 = requests.get(url_2, headers=headers, proxies=proxy, allow_redirects=True)
        response_1.raise_for_status()
        response_2.raise_for_status()
        
        data_1 = response_1.json()
        data_2 = response_2.json()
        
        user = data_1.get("userMining")
        
        user_id = user.get("userId")        
        balance = user.get("gotAmount")
        mining_amount = user.get("miningAmount")
        m_s = user.get("speed")
        alliance = user.get("alliance")
        
        print(f"{Fore.MAGENTA+ Style.BRIGHT}ID: {Fore.WHITE + Style.BRIGHT}{user_id}")
        print(f"{Fore.GREEN + Style.BRIGHT}Balance: {Fore.WHITE + Style.BRIGHT}{balance:.2f} | Mining Speed: {m_s:.4f}")
        print(f"{Fore.CYAN + Style.BRIGHT}Mining Amount: {Fore.WHITE + Style.BRIGHT}{mining_amount:.6f}")
        
        target_alliance = "sftearning_squad"
        
        if alliance not in user or alliance != target_alliance:
            url_set_alliance = f"https://gm.pocketfi.org/mining/alliances/set?alliance={target_alliance}"
            response_set_alliance = requests.post(url_set_alliance, headers=headers, proxies=proxy, allow_redirects=True)
            if response_set_alliance.status_code == 200:
                target_alliance = "sftearning_squad"
                url_alliance_info = f"https://gm.pocketfi.org/mining/alliances/{target_alliance}"
                response_alliance_info = requests.get(url_alliance_info, headers=headers, proxies=proxy, allow_redirects=True)
                if response_alliance_info.status_code == 200:
                	data_a = response_alliance_info.json()
                	title = data_a.get("title")
                	rank = data_a.get("userRank")
                	users = data_a.get("users")
                	print(f"{Fore.YELLOW + Style.BRIGHT}Alliance: {Fore.WHITE + Style.BRIGHT}{title} | {Fore.GREEN + Style.BRIGHT}Total Member: {Fore.WHITE + Style.BRIGHT}{users}")
                	print(f"{Fore.BLUE + Style.BRIGHT}My Alliance Rank: {Fore.WHITE + Style.BRIGHT}{rank}")
            else:
                url_alliance_info = f"https://gm.pocketfi.org/mining/alliances/{target_alliance}"
                response_alliance_info = requests.get(url_alliance_info, headers=headers, proxies=proxy, allow_redirects=True)
                if response_alliance_info.status_code == 200:
                	data_a = response_alliance_info.json()
                	title = data_a.get("title")
                	rank = data_a.get("userRank")
                	users = data_a.get("users")
                	print(f"Alliance: {title} | Total Member: {users}")
                	print(f"My Alliance Rank: {rank}")

    except requests.exceptions.RequestException as e:
        print(f"{Fore.RED + Style.BRIGHT}Request failed: {e}")
    except ValueError as ve:
        print(f"{Fore.RED + Style.BRIGHT}JSON parsing failed: {ve}")

def claim(token, proxy=None):
    url = "https://gm.pocketfi.org/mining/claimMining"
    
    headers = get_headers(token, proxy)
    
    try:
        response = requests.post(url, headers=headers, proxies=proxy, allow_redirects=True)
        response.raise_for_status()
        data = response.json()
        
        n_b = data.get("userMining", {}).get("gotAmount")
        dttm_claim_deadline = data.get("userMining", {}).get("dttmClaimDeadline")
        
        if n_b is not None:
            print(f"{Fore.MAGENTA + Style.BRIGHT}New Balance: {Fore.WHITE + Style.BRIGHT}{n_b:.2f}")
        else:
            print("{Fore.YELOOW + Style.BRIGHT}New Balance: Not available")
        
        return dttm_claim_deadline

    except requests.exceptions.RequestException as e:
        print(f"{Fore.RED + Style.BRIGHT}Request failed: {e}")
        return None
    except ValueError as ve:
        print(f"{Fore.RED + Style.BRIGHT}JSON parsing failed: {ve}")
        return None

def get_fibonacci_series():
    return [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]

def daily_bonus(token, proxy=None):
    url = "https://rubot.pocketfi.org/boost/activateDailyBoost"
    
    headers = get_headers(token, proxy)
    
    try:
        response = requests.post(url, headers=headers, proxies=proxy, allow_redirects=True)
        response.raise_for_status()
        data = response.json()
        
        updated_for_day = data.get('updatedForDay')
        fibonacci_series = get_fibonacci_series()
        
        if updated_for_day is None:
            print(f"{Fore.YELLOW + Style.BRIGHT}Daily Bonus Already Claimed")
        elif 0 <= updated_for_day < len(fibonacci_series):
            reward_value = fibonacci_series[updated_for_day]
            print(f"{Fore.RED + Style.BRIGHT}Daily Reward Claimed: {reward_value}")
        else:
            print(f"{Fore.RED + Style.BRIGHT}Invalid value for updatedForDay")

    except requests.exceptions.RequestException as e:
        print(f"{Fore.RED + Style.BRIGHT}Request failed: {e}")
    except ValueError as ve:
        print(f"{Fore.RED + Style.BRIGHT}JSON parsing failed: {ve}")

def main():
    clear_terminal()
    art()
    
    tokens = load_tokens('data.txt')
    proxies = load_proxies('proxy.txt') if os.path.exists('proxy.txt') else None
    
    total_accounts = len(tokens)
    use_proxy = input(f"{Fore.CYAN}Do you want to use a proxy? (y/n): ").strip().lower()
    clear_terminal()
    art()
    
    
    remaining_times = []
    
    while True:
        # Print total accounts before processing each account
        print(f"{Fore.MAGENTA + Style.BRIGHT}Total Accounts: {Fore.WHITE + Style.BRIGHT}{total_accounts}{Style.RESET_ALL}\n")
        
        for i, token in enumerate(tokens, start=1):
            print(f"{Fore.CYAN + Style.BRIGHT}------Account No.{i}------{Style.RESET_ALL}")
            proxy = None
            
            if use_proxy == 'y' and proxies:
                proxy = {
                    "http": f"http://{proxies[i % len(proxies)]}",
                    "https": f"http://{proxies[i % len(proxies)]}"
                }
                # Format the proxy display
                proxy_parts = proxy['http'].split('@')[-1].split(':')  # Split to get the IP and port
                formatted_proxy = f"{proxy_parts[0][:4]}.....{proxy_parts[1]}"
                print(f"{Fore.YELLOW + Style.BRIGHT}Using Proxy: {formatted_proxy}{Style.RESET_ALL}")
    
            try:
                login(token, proxy)
                user_data(token, proxy)
                next_claim = claim(token, proxy)
                if next_claim:
                    remaining_times.append(next_claim)
                daily_bonus(token, proxy)
    
            except Exception as e:
                print(f"Error processing account {i}: {e}")
                continue
            
        if remaining_times:
            shortest_time = min(remaining_times)
            now = time.time() * 1000
            diffe = shortest_time - now
            seco = int(diffe / 1000)
    
        countdown_timer(seco)
        clear_terminal()
        art()        

if __name__ == "__main__":
    init()
    main()      
