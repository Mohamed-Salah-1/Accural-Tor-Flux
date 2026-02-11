#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Accural-Tor-Flux
# Copyright (C) 2026 Artiphoria
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

"""
Accural-Tor-Flux
Optimized IP Rotator for Artiphoria & Accural
"""

import time
import os
import subprocess
import sys
import platform

def get_distro():
    """Detects the Linux distribution."""
    try:
        if os.path.exists("/etc/os-release"):
            with open("/etc/os-release") as f:
                lines = f.readlines()
                for line in lines:
                    if line.startswith("ID="):
                        return line.strip().split("=")[1].strip('"')
    except Exception:
        pass
    return platform.system().lower()

def run_command(command, shell=True):
    """Wrapper for subprocess.run to handle commands safely."""
    try:
        result = subprocess.run(command, shell=shell, check=True, capture_output=True, text=True)
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        return None

def check_dependencies():
    """Checks and installs required Python packages."""
    try:
        import requests
    except ImportError:
        print('[+] Installing python3-requests...')
        run_command('pip3 install requests requests[socks]')
        import requests
    return requests

requests = check_dependencies()

def setup_tor():
    """Ensures Tor is installed and running based on the distribution."""
    distro = get_distro()
    
    # Check if tor is installed
    if not run_command('which tor'):
        print(f'[!] Tor is not installed on your {distro} system.')
        print('[+] Attempting automated installation...')
        
        if distro in ['ubuntu', 'debian', 'kali', 'raspbian']:
            run_command('sudo apt update && sudo apt install tor -y')
        elif distro in ['arch', 'manjaro']:
            run_command('sudo pacman -Sy tor --noconfirm')
        elif distro in ['fedora', 'centos', 'rhel']:
            run_command('sudo dnf install tor -y')
        else:
            print('[!] Distro not officially supported for auto-install. Please install Tor manually.')
            sys.exit(1)
            
    # Ensure tor service is running
    status = run_command('service tor status')
    if not status or 'active (running)' not in status.lower():
        print('[+] Starting Tor service...')
        run_command('sudo service tor start')
        time.sleep(2)

def get_current_ip():
    """Fetches the current IP via Tor proxy."""
    url = 'http://checkip.amazonaws.com'
    proxies = {
        'http': 'socks5h://127.0.0.1:9050',
        'https': 'socks5h://127.0.0.1:9050'
    }
    try:
        response = requests.get(url, proxies=proxies, timeout=10)
        return response.text.strip()
    except Exception as e:
        return f"Error fetching IP: {e}"

def change_ip():
    """Reloads Tor to get a new identity."""
    run_command("sudo service tor reload")
    new_ip = get_current_ip()
    print(f'[+] IP Rotation Successful. New Identity: \033[1;32m{new_ip}\033[0m')

def print_banner():
    os.system("clear")
    banner = f"""\033[1;36m
   ___         _   _       _                _        
  / _ \  _ __ | |_(_) _ __ | |__    ___  _ _(_) __ _ 
 / /_\ \| '__|| __| || '_ \| '_ \  / _ \| '__| |/ _` |
/ /   \ \ |   | |_| || |_) | | | || (_) | |  | | (_| |
\/     \/\_|    \__|_|| .__/|_| |_| \___/|_|  |_|\\__,_|
                      |_|                             
 \033[1;35m             A C C U R A L - T O R - F L U X
 \033[1;32m      (Powered by Artiphoria | Optimized for Accural)
 \033[0m"""
    print(banner)

def main():
    if os.getuid() != 0:
        print("[!] This script must be run as root (sudo).")
        sys.exit(1)

    setup_tor()
    print_banner()
    
    print("\033[1;33m[!] Ensure your system/browser SOCKS5 proxy is set to 127.0.0.1:9050\033[0m\n")
    
    try:
        interval = input("[+] Set IP rotation interval (seconds) [default=60] >> ") or "60"
        iterations = input("[+] Number of rotations (enter for infinite) >> ") or "0"
        
        interval = int(interval)
        iterations = int(iterations)
        
        print(f"\n[+] Starting rotation every {interval}s...")
        
        current_count = 0
        while True:
            change_ip()
            current_count += 1
            
            if iterations != 0 and current_count >= iterations:
                print(f"\n[+] Completed {iterations} rotations.")
                break
                
            time.sleep(interval)
            
    except ValueError:
        print("\n[!] Invalid input. Numerical values required.")
    except KeyboardInterrupt:
        print('\n[!] Accural-Tor-Flux terminated by user.')

if __name__ == "__main__":
    main()
