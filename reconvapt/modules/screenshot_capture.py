#!/usr/bin/env python3
"""
RECON VAPT Framework - Screenshot Capture Module
2 reliable tools: gowitness, aquatone
"""

import os
import subprocess
import time
from colorama import Fore, Style
from utils.helpers import create_output_dir, check_tool_installed

class ScreenshotCapture:
    def __init__(self):
        self.tools = {
            "1": {
                "name": "gowitness",
                "description": "Web screenshot utility",
                "command": "gowitness single {url} --screenshot-path {output}",
                "install": "go install github.com/sensepost/gowitness@latest"
            },
            "2": {
                "name": "aquatone",
                "description": "Visual inspection tool",
                "command": "echo {url} | aquatone -out {output}",
                "install": "go install github.com/michenriksen/aquatone@latest"
            }
        }
    
    def show_menu(self):
        """Display tool selection menu"""
        print(f"\n{Fore.YELLOW}╔══════════════════════════════════════════════════════════╗")
        print(f"{Fore.YELLOW}║           SCREENSHOT CAPTURE - Tool Selection            ║")
        print(f"{Fore.YELLOW}╚══════════════════════════════════════════════════════════╝{Style.RESET_ALL}")
        
        for key, tool in self.tools.items():
            print(f"{Fore.CYAN}[{key}]{Fore.WHITE} {tool['name']:<12} - {tool['description']}")
        
        print(f"{Fore.RED}[0] Back to Main Menu{Style.RESET_ALL}")
    
    def install_tool(self, tool_info):
        """Install missing tool"""
        print(f"{Fore.YELLOW}[!] {tool_info['name']} is not installed")
        print(f"{Fore.CYAN}[*] Install command: {tool_info['install']}{Style.RESET_ALL}")
        
        choice = input(f"{Fore.WHITE}Install now? (y/n): {Style.RESET_ALL}").strip().lower()
        if choice != 'y':
            return False
        
        print(f"{Fore.CYAN}[*] Installing {tool_info['name']}...{Style.RESET_ALL}")
        
        try:
            env = os.environ.copy()
            go_bin = os.path.expanduser("~/go/bin")
            env['PATH'] = f"{go_bin}:{env.get('PATH', '')}"
            env['GOPATH'] = env.get('GOPATH', os.path.expanduser("~/go"))
            
            process = subprocess.run(tool_info['install'], shell=True, capture_output=True, 
                                   text=True, timeout=300, env=env)
            
            if process.returncode == 0:
                print(f"{Fore.GREEN}[✓] Installed successfully!{Style.RESET_ALL}")
                return True
            return False
        except Exception as e:
            print(f"{Fore.RED}[!] Error: {str(e)}{Style.RESET_ALL}")
            return False
    
    def run_tool(self, tool_info, url, output_dir):
        """Execute selected tool"""
        print(f"\n{Fore.CYAN}[*] Running {tool_info['name']} on {url}...{Style.RESET_ALL}")
        
        command = tool_info['command'].format(url=url, output=output_dir)
        tool_check = check_tool_installed(tool_info['name'])
        if isinstance(tool_check, str):
            command = command.replace(tool_info['name'], tool_check)
        
        start_time = time.time()
        
        try:
            process = subprocess.run(command, shell=True, capture_output=True, 
                                   text=True, timeout=300)
            elapsed = round(time.time() - start_time, 2)
            
            if process.returncode == 0:
                print(f"{Fore.GREEN}[✓] Completed in {elapsed}s{Style.RESET_ALL}")
                print(f"{Fore.GREEN}[✓] Screenshots saved to: {output_dir}{Style.RESET_ALL}")
                return True
            else:
                print(f"{Fore.RED}[!] Tool failed{Style.RESET_ALL}")
                return False
        except subprocess.TimeoutExpired:
            print(f"{Fore.RED}[!] Tool timed out{Style.RESET_ALL}")
            return False
        except Exception as e:
            print(f"{Fore.RED}[!] Error: {str(e)}{Style.RESET_ALL}")
            return False
    
    def run(self):
        """Main module execution"""
        while True:
            self.show_menu()
            choice = input(f"\n{Fore.WHITE}Select tool [0-2]: {Style.RESET_ALL}").strip()
            
            if choice == '0':
                break
            if choice not in ['1', '2']:
                print(f"{Fore.RED}[!] Invalid choice{Style.RESET_ALL}")
                continue
            
            url = input(f"{Fore.WHITE}Enter target URL: {Style.RESET_ALL}").strip()
            if not url.startswith(('http://', 'https://')):
                url = 'http://' + url
            
            domain = url.replace('http://', '').replace('https://', '').split('/')[0]
            output_dir = create_output_dir(f"screenshot_{domain}")
            print(f"{Fore.CYAN}[*] Output directory: {output_dir}{Style.RESET_ALL}")
            
            tool_info = self.tools[choice]
            if not check_tool_installed(tool_info['name']):
                if not self.install_tool(tool_info):
                    continue
            
            self.run_tool(tool_info, url, output_dir)
            input(f"\n{Fore.YELLOW}Press Enter to continue...{Style.RESET_ALL}")

if __name__ == "__main__":
    module = ScreenshotCapture()
    module.run()
