#!/usr/bin/env python3
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

import os
import sys
import subprocess

def run_command(command):
    try:
        subprocess.run(command, shell=True, check=True)
        return True
    except subprocess.CalledProcessError:
        return False

def install():
    print('[+] Installing Accural-Tor-Flux...')
    
    # Paths
    script_path = os.path.abspath('auto_flux.py')
    install_dir = '/usr/share/accural-flux'
    bin_path = '/usr/bin/acc' # Shortcut set to 'acc'
    
    run_command(f'sudo mkdir -p {install_dir}')
    run_command(f'sudo cp {script_path} {install_dir}/auto_flux.py')
    run_command(f'sudo chmod 755 {install_dir}/auto_flux.py')
    
    # Create the binary shortcut
    launcher = f'#!/bin/sh\nexec python3 {install_dir}/auto_flux.py "$@"'
    
    try:
        with open('acc_launcher', 'w') as f:
            f.write(launcher)
        
        run_command(f'sudo mv acc_launcher {bin_path}')
        run_command(f'sudo chmod +x {bin_path}')
        
        # Also create 'aut' for legacy/shortcut preference
        # Remove old legacy directory if it exists to avoid confusion
        if os.path.exists('/usr/share/aut'):
            print('[+] Removing legacy installation at /usr/share/aut...')
            run_command('sudo rm -rf /usr/share/aut')
            
        run_command(f'sudo ln -sf {bin_path} /usr/bin/aut')
        
        print('\n\033[1;32m[!] Accural-Tor-Flux installed successfully!\033[0m')
        print(f'[+] You can now run it from anywhere by typing: \033[1;36macc\033[0m or \033[1;36maut\033[0m')
    except Exception as e:
        print(f'[!] Installation failed: {e}')

def uninstall():
    print('[!] Removing Accural-Tor-Flux...')
    run_command('sudo rm -rf /usr/share/accural-flux')
    run_command('sudo rm -f /usr/bin/acc')
    run_command('sudo rm -f /usr/bin/aut')
    print('[+] Uninstalled successfully.')

if __name__ == "__main__":
    if len(sys.argv) > 1:
        if sys.argv[1].lower() == 'uninstall':
            uninstall()
            sys.exit(0)

    print("""
[1] Install
[2] Uninstall
[3] Exit
""")
    choice = input('[?] Select an option (1-3): ').strip()

    if choice == '1':
        install()
    elif choice == '2':
        uninstall()
    elif choice == '3':
        sys.exit(0)
    else:
        print('[!] Invalid choice.')
