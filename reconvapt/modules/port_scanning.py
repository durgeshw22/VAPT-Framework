#!/usr/bin/env python3
"""
RECON VAPT Framework - Port Scanning Module
3 reliable tools: nmap, naabu, masscan
"""

import os
import subprocess
import time
from colorama import Fore, Style
from utils.helpers import validate_domain, validate_ip, create_output_dir, check_tool_installed, count_lines, read_file_lines

class PortScanning:
    def __init__(self):
        self.tools = {
            "1": {
                "name": "nmap",
                "description": "Network exploration and security auditing",
                "command": "nmap -p- -T4 --open {target} -oN {output}",
                "install": "apt-get install nmap"
            },
            "2": {
                "name": "naabu",
                "description": "Fast port scanner",
                "command": "naabu -host {target} -p - -o {output} -silent",
                "install": "go install -v github.com/projectdiscovery/naabu/v2/cmd/naabu@latest"
            },
            "3": {
                "name": "masscan",
                "description": "Fast port scanner for large ranges",
                "command": "masscan {target} -p1-65535 --rate=1000 -oL {output}",
                "install": "apt-get install masscan"
            }
        }
    
    def show_menu(self):
        """Display tool selection menu"""
        print(f"\n{Fore.YELLOW}╔══════════════════════════════════════════════════════════╗")
        print(f"{Fore.YELLOW}║             PORT SCANNING - Tool Selection               ║")
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
            
            if 'PATH' in env:
                env['PATH'] = f"{go_bin}:{env['PATH']}"
            else:
                env['PATH'] = go_bin
            
            if 'GOPATH' not in env:
                env['GOPATH'] = os.path.expanduser("~/go")
            
            process = subprocess.run(
                tool_info['install'],
                shell=True,
                capture_output=True,
                text=True,
                timeout=300,
                env=env
            )
            
            if process.returncode == 0:
                print(f"{Fore.GREEN}[✓] {tool_info['name']} installed successfully!{Style.RESET_ALL}")
                return True
            else:
                print(f"{Fore.RED}[!] Installation failed{Style.RESET_ALL}")
                return False
                
        except Exception as e:
            print(f"{Fore.RED}[!] Installation error: {str(e)}{Style.RESET_ALL}")
            return False
    
    def run_tool(self, tool_info, target, output_file):
        """Execute selected tool"""
        print(f"\n{Fore.CYAN}[*] Running {tool_info['name']} on {target}...{Style.RESET_ALL}")
        print(f"{Fore.CYAN}[*] Output: {output_file}{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}[*] This may take several minutes...{Style.RESET_ALL}")
        
        # Prepare command
        command = tool_info['command'].format(target=target, output=output_file)
        
        # Check if tool exists and get full path if needed
        tool_check = check_tool_installed(tool_info['name'])
        if isinstance(tool_check, str):
            command = command.replace(tool_info['name'], tool_check)
        
        start_time = time.time()
        
        try:
            process = subprocess.run(
                command,
                shell=True,
                capture_output=True,
                text=True,
                timeout=3600  # 60 min timeout
            )
            
            elapsed = round(time.time() - start_time, 2)
            
            if process.returncode == 0 or os.path.exists(output_file):
                # Count results
                result_count = count_lines(output_file)
                
                print(f"{Fore.GREEN}[✓] Completed in {elapsed}s{Style.RESET_ALL}")
                print(f"{Fore.GREEN}[✓] Found {result_count} open ports{Style.RESET_ALL}")
                
                # Show preview
                if result_count > 0:
                    preview = read_file_lines(output_file, 10)
                    print(f"{Fore.YELLOW}[*] Preview:{Style.RESET_ALL}")
                    for line in preview:
                        print(f"{Fore.WHITE}    {line}{Style.RESET_ALL}")
                    if result_count > 10:
                        print(f"{Fore.YELLOW}    ... and {result_count - 10} more{Style.RESET_ALL}")
                
                return True
            else:
                print(f"{Fore.RED}[!] Tool failed{Style.RESET_ALL}")
                return False
                
        except subprocess.TimeoutExpired:
            print(f"{Fore.RED}[!] Tool timed out (60 min limit){Style.RESET_ALL}")
            return False
        except Exception as e:
            print(f"{Fore.RED}[!] Error: {str(e)}{Style.RESET_ALL}")
            return False
    
    def run(self):
        """Main module execution"""
        while True:
            self.show_menu()
            
            choice = input(f"\n{Fore.WHITE}Select tool [0-3]: {Style.RESET_ALL}").strip()
            
            if choice == '0':
                break
            
            if choice not in ['1', '2', '3']:
                print(f"{Fore.RED}[!] Invalid choice{Style.RESET_ALL}")
                continue
            
            # Get target
            target = input(f"{Fore.WHITE}Enter target (IP or domain): {Style.RESET_ALL}").strip()
            
            # Validate target
            if not (validate_ip(target) or validate_domain(target)):
                print(f"{Fore.RED}[!] Invalid target format{Style.RESET_ALL}")
                continue
            
            # Create output directory
            output_dir = create_output_dir(f"ports_{target}")
            print(f"{Fore.CYAN}[*] Output directory: {output_dir}{Style.RESET_ALL}")
            
            # Get tool
            tool_info = self.tools[choice]
            
            # Check installation
            if not check_tool_installed(tool_info['name']):
                if not self.install_tool(tool_info):
                    continue
            
            output_file = os.path.join(output_dir, f"{tool_info['name']}_results.txt")
            self.run_tool(tool_info, target, output_file)
            
            input(f"\n{Fore.YELLOW}Press Enter to continue...{Style.RESET_ALL}")

if __name__ == "__main__":
    module = PortScanning()
    module.run()
