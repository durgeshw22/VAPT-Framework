#!/usr/bin/env python3
"""
RECON VAPT Framework - Directory/File Discovery Module
3 reliable tools: ffuf, gobuster, dirb
"""

import os
import subprocess
import time
from colorama import Fore, Style
from utils.helpers import validate_url, create_output_dir, check_tool_installed, count_lines, read_file_lines

class DirectoryDiscovery:
    def __init__(self):
        self.tools = {
            "1": {
                "name": "ffuf",
                "description": "Fast web fuzzer",
                "command": "ffuf -u {url}/FUZZ -w {wordlist} -mc 200,204,301,302,307,401,403 -o {output} -of csv -s",
                "install": "go install github.com/ffuf/ffuf@latest",
                "requires_wordlist": True
            },
            "2": {
                "name": "gobuster",
                "description": "Directory/file brute-forcer",
                "command": "gobuster dir -u {url} -w {wordlist} -o {output} -q --no-error",
                "install": "go install github.com/OJ/gobuster/v3@latest",
                "requires_wordlist": True
            },
            "3": {
                "name": "dirb",
                "description": "Web content scanner",
                "command": "dirb {url} {wordlist} -o {output} -S -r",
                "install": "apt-get install dirb",
                "requires_wordlist": True
            }
        }
        
        # Common wordlists on Kali Linux
        self.wordlists = {
            "1": "/usr/share/wordlists/dirb/common.txt",
            "2": "/usr/share/wordlists/dirbuster/directory-list-2.3-small.txt",
            "3": "/usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt",
            "4": "custom"
        }
    
    def show_menu(self):
        """Display tool selection menu"""
        print(f"\n{Fore.YELLOW}╔══════════════════════════════════════════════════════════╗")
        print(f"{Fore.YELLOW}║        DIRECTORY/FILE DISCOVERY - Tool Selection         ║")
        print(f"{Fore.YELLOW}╚══════════════════════════════════════════════════════════╝{Style.RESET_ALL}")
        
        for key, tool in self.tools.items():
            print(f"{Fore.CYAN}[{key}]{Fore.WHITE} {tool['name']:<12} - {tool['description']}")
        
        print(f"{Fore.RED}[0] Back to Main Menu{Style.RESET_ALL}")
    
    def show_wordlist_menu(self):
        """Display wordlist selection"""
        print(f"\n{Fore.YELLOW}Select Wordlist:{Style.RESET_ALL}")
        print(f"{Fore.CYAN}[1]{Fore.WHITE} Common (4,614 entries)")
        print(f"{Fore.CYAN}[2]{Fore.WHITE} Small (87,650 entries)")
        print(f"{Fore.CYAN}[3]{Fore.WHITE} Medium (220,560 entries)")
        print(f"{Fore.CYAN}[4]{Fore.WHITE} Custom path")
    
    def get_wordlist(self):
        """Get wordlist selection"""
        self.show_wordlist_menu()
        
        choice = input(f"{Fore.WHITE}Select wordlist [1-4]: {Style.RESET_ALL}").strip()
        
        if choice in ['1', '2', '3']:
            wordlist = self.wordlists[choice]
            if os.path.exists(wordlist):
                return wordlist
            else:
                print(f"{Fore.RED}[!] Wordlist not found: {wordlist}{Style.RESET_ALL}")
                return None
        elif choice == '4':
            wordlist = input(f"{Fore.WHITE}Enter wordlist path: {Style.RESET_ALL}").strip()
            if os.path.exists(wordlist):
                return wordlist
            else:
                print(f"{Fore.RED}[!] File not found{Style.RESET_ALL}")
                return None
        else:
            print(f"{Fore.RED}[!] Invalid choice{Style.RESET_ALL}")
            return None
    
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
    
    def run_tool(self, tool_info, url, wordlist, output_file):
        """Execute selected tool"""
        print(f"\n{Fore.CYAN}[*] Running {tool_info['name']} on {url}...{Style.RESET_ALL}")
        print(f"{Fore.CYAN}[*] Wordlist: {wordlist}{Style.RESET_ALL}")
        print(f"{Fore.CYAN}[*] Output: {output_file}{Style.RESET_ALL}")
        
        # Prepare command
        command = tool_info['command'].format(url=url, wordlist=wordlist, output=output_file)
        
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
                timeout=1800  # 30 min timeout for large wordlists
            )
            
            elapsed = round(time.time() - start_time, 2)
            
            if process.returncode == 0 or os.path.exists(output_file):
                # Count results
                result_count = count_lines(output_file)
                
                print(f"{Fore.GREEN}[✓] Completed in {elapsed}s{Style.RESET_ALL}")
                print(f"{Fore.GREEN}[✓] Found {result_count} directories/files{Style.RESET_ALL}")
                
                # Show preview
                if result_count > 0:
                    preview = read_file_lines(output_file, 5)
                    print(f"{Fore.YELLOW}[*] Preview:{Style.RESET_ALL}")
                    for line in preview:
                        print(f"{Fore.WHITE}    {line}{Style.RESET_ALL}")
                    if result_count > 5:
                        print(f"{Fore.YELLOW}    ... and {result_count - 5} more{Style.RESET_ALL}")
                
                return True
            else:
                print(f"{Fore.RED}[!] Tool failed{Style.RESET_ALL}")
                return False
                
        except subprocess.TimeoutExpired:
            print(f"{Fore.RED}[!] Tool timed out (30 min limit){Style.RESET_ALL}")
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
            
            # Get target URL
            url = input(f"{Fore.WHITE}Enter target URL: {Style.RESET_ALL}").strip()
            url = validate_url(url)
            
            if not url:
                print(f"{Fore.RED}[!] Invalid URL format{Style.RESET_ALL}")
                continue
            
            # Get wordlist
            wordlist = self.get_wordlist()
            if not wordlist:
                continue
            
            # Create output directory
            domain = url.replace('http://', '').replace('https://', '').split('/')[0]
            output_dir = create_output_dir(f"dir_{domain}")
            print(f"{Fore.CYAN}[*] Output directory: {output_dir}{Style.RESET_ALL}")
            
            # Get tool
            tool_info = self.tools[choice]
            
            # Check installation
            if not check_tool_installed(tool_info['name']):
                if not self.install_tool(tool_info):
                    continue
            
            output_file = os.path.join(output_dir, f"{tool_info['name']}_results.txt")
            self.run_tool(tool_info, url, wordlist, output_file)
            
            input(f"\n{Fore.YELLOW}Press Enter to continue...{Style.RESET_ALL}")

if __name__ == "__main__":
    module = DirectoryDiscovery()
    module.run()
