#!/usr/bin/env python3
"""
RECON VAPT Framework - Technology Detection Module
2 tools: httpx, whatweb
"""

import os
import subprocess
import time
from colorama import Fore, Style
from utils.helpers import create_output_dir, check_tool_installed, validate_url

class TechnologyDetection:
    def __init__(self):
        self.tools = {
            "1": {
                "name": "httpx",
                "description": "HTTP toolkit with tech detection",
                "command": "echo {url} | httpx -tech-detect -title -status-code -silent > {output}",
                "install": "go install -v github.com/projectdiscovery/httpx/cmd/httpx@latest"
            },
            "2": {
                "name": "whatweb",
                "description": "Web technology identifier",
                "command": "whatweb '{url}' -v --color=never | tee {output}",
                "install": "apt-get install whatweb"
            }
        }
    
    def show_menu(self):
        print(f"\n{Fore.YELLOW}╔══════════════════════════════════════════════════════════╗")
        print(f"{Fore.YELLOW}║        TECHNOLOGY DETECTION - Tool Selection             ║")
        print(f"{Fore.YELLOW}╚══════════════════════════════════════════════════════════╝{Style.RESET_ALL}")
        for key, tool in self.tools.items():
            print(f"{Fore.CYAN}[{key}]{Fore.WHITE} {tool['name']:<12} - {tool['description']}")
        print(f"{Fore.RED}[0] Back to Main Menu{Style.RESET_ALL}")
    
    def install_tool(self, tool_info):
        print(f"{Fore.YELLOW}[!] {tool_info['name']} not installed")
        choice = input(f"{Fore.WHITE}Install? (y/n): {Style.RESET_ALL}").strip().lower()
        if choice != 'y':
            return False
        
        try:
            env = os.environ.copy()
            go_bin = os.path.expanduser("~/go/bin")
            env['PATH'] = f"{go_bin}:{env.get('PATH', '')}"
            env['GOPATH'] = env.get('GOPATH', os.path.expanduser("~/go"))
            
            process = subprocess.run(tool_info['install'], shell=True, capture_output=True,
                                   text=True, timeout=300, env=env)
            if process.returncode == 0:
                print(f"{Fore.GREEN}[✓] Installed!{Style.RESET_ALL}")
                return True
            return False
        except:
            return False
    
    def run_tool(self, tool_info, url, output_file):
        print(f"\n{Fore.CYAN}[*] Running {tool_info['name']}...{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}[*] Detecting technologies...{Style.RESET_ALL}\n")
        
        command = tool_info['command'].format(url=url, output=output_file)
        tool_check = check_tool_installed(tool_info['name'])
        if isinstance(tool_check, str):
            command = command.replace(tool_info['name'], tool_check)
        
        try:
            start_time = time.time()
            # Show live output
            process = subprocess.run(command, shell=True, timeout=300)
            elapsed = round(time.time() - start_time, 2)
            
            print(f"\n{Fore.GREEN}[✓] Completed in {elapsed}s{Style.RESET_ALL}")
            
            # Check if output file has content
            if os.path.exists(output_file):
                file_size = os.path.getsize(output_file)
                if file_size > 0:
                    print(f"{Fore.GREEN}[✓] Results saved to: {output_file}{Style.RESET_ALL}")
                else:
                    print(f"{Fore.YELLOW}[!] No results captured in file (but output shown above){Style.RESET_ALL}")
            
            return True
        except subprocess.TimeoutExpired:
            print(f"\n{Fore.RED}[!] Timeout (5 minutes){Style.RESET_ALL}")
            return False
        except KeyboardInterrupt:
            print(f"\n{Fore.YELLOW}[!] Cancelled by user{Style.RESET_ALL}")
            return False
    
    def run(self):
        while True:
            self.show_menu()
            choice = input(f"\n{Fore.WHITE}Select [0-2]: {Style.RESET_ALL}").strip()
            
            if choice == '0':
                break
            if choice not in ['1', '2']:
                continue
            
            url = input(f"{Fore.WHITE}Enter URL: {Style.RESET_ALL}").strip()
            url = validate_url(url)
            if not url:
                continue
            
            domain = url.replace('http://', '').replace('https://', '').split('/')[0]
            output_dir = create_output_dir(f"tech_{domain}")
            tool_info = self.tools[choice]
            
            if not check_tool_installed(tool_info['name']):
                if not self.install_tool(tool_info):
                    continue
            
            output_file = os.path.join(output_dir, f"{tool_info['name']}_results.txt")
            self.run_tool(tool_info, url, output_file)
            input(f"\n{Fore.YELLOW}Press Enter...{Style.RESET_ALL}")

if __name__ == "__main__":
    module = TechnologyDetection()
    module.run()
