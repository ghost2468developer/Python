import time
from datetime import datetime as dt, timedelta
import os
import logging
import tkinter as tk
from tkinter import messagebox

# Set up logging
logging.basicConfig(filename='blocker.log', level=logging.INFO, format='%(asctime)s - %(message)s')

sites_to_block = [
    "www.facebook.com",
    "facebook.com",
    "www.youtube.com",
    "youtube.com",
    "www.gmail.com",
    "gmail.com",
]

whitelist = [
    "www.google.com",
    "www.stackoverflow.com",
]

Linux_host = "/etc/hosts"
Window_host = r"C:\Windows\System32\drivers\etc\hosts"
default_hoster = Linux_host
redirect = "127.0.0.1"

if os.name == 'posix':
    default_hoster = Linux_host
elif os.name == 'nt':
    default_hoster = Window_host
else:
    print("OS Unknown")
    exit()

def get_user_input():
    start_hour = int(input("Enter the start hour (24-hour format): "))
    duration = int(input("Enter the duration in hours: "))
    return start_hour, duration

def block_websites(start_hour, duration):
    start_time = dt.now().replace(hour=start_hour, minute=0, second=0, microsecond=0)
    end_time = start_time + timedelta(hours=duration)
    while True:
        current_time = dt.now()
        if start_time <= current_time < end_time:
            print("Blocking websites...")
            block_sites()
            logging.info("Websites blocked.")
        else:
            print("Unblocking websites...")
            unblock_sites()
            logging.info("Websites unblocked.")
        time.sleep(3)

def block_sites():
    with open(default_hoster, "r") as hostfile:
        hosts = hostfile.readlines()
    with open(default_hoster, "w") as hostfile:
        for host in hosts:
            if not any(site in host for site in sites_to_block) or site in whitelist:
                hostfile.write(host)
        for site in sites_to_block:
            if site not in whitelist:
                hostfile.write(f"{redirect} {site}\n")

def unblock_sites():
    with open(default_hoster, "r") as hostfile:
        hosts = hostfile.readlines()
    with open(default_hoster, "w") as hostfile:
        for host in hosts:
            if not any(site in host for site in sites_to_block) or site in whitelist:
                hostfile.write(host)

def gui_start():
    root = tk.Tk()
    root.title("Website Blocker")

    def start_blocking():
        start_hour, duration = get_user_input()
        block_websites(start_hour, duration)
        messagebox.showinfo("Info", "Website blocking started.")

    start_button = tk.Button(root, text="Start Blocking", command=start_blocking)
    start_button.pack()

    root.mainloop()

if __name__ == "__main__":
    gui_start()
