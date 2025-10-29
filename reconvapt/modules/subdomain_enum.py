#!/usr/bin/env python3
"""
RECON VAPT Framework - Subdomain Enumeration Module
Simplified version with 4 reliable tools only
"""

import os
import subprocess
import time
from datetime import datetime
from colorama import Fore, Style
from utils.helpers import validate_domain, create_output_dir, check_tool_installed, count_lines, read_file_lines

class SubdomainEnumeration:
    def __init__(self):
        # Only 4 most reliable tools
        self.tools = {
            "1": {
                "name": "subfinder",
                "description": "Fast passive subdomain enumeration",
                "command": "subfinder -d {domain} -o {output}",
                "install": "go install -v github.com/projectdiscovery/subfinder/v2/cmd/subfinder@latest"
            },
            "2": {
                "name": "assetfinder",
                "description": "Find subdomains from various sources",
                "command": "assetfinder --subs-only {domain} > {output}",
                "install": "go install github.com/tomnomnom/assetfinder@latest"
            },
            "3": {
                "name": "httpx",
                "description": "HTTP toolkit for subdomain validation",
                "command": "echo {domain} | httpx -silent > {output}",
                "install": "go install -v github.com/projectdiscovery/httpx/cmd/httpx@latest"
            },
            "4": {
                "name": "crt.sh",
                "description": "Certificate Transparency search",
                "command": "curl -s 'https://crt.sh/?q=%25.{domain}&output=json' | grep -oP '\"name_value\":\"\\K[^\"]*' | sed 's/\\*\\.//g' | sort -u > {output}",
                "install": "Built-in (requires curl)"
            }
        }
    
    def show_menu(self):
        """Display tool selection menu"""
        print(f"\n{Fore.YELLOW}╔══════════════════════════════════════════════════════════╗")
        print(f"{Fore.YELLOW}║          SUBDOMAIN ENUMERATION - Tool Selection          ║")
        print(f"{Fore.YELLOW}╚══════════════════════════════════════════════════════════╝{Style.RESET_ALL}")
        
        for key, tool in self.tools.items():
            print(f"{Fore.CYAN}[{key}]{Fore.WHITE} {tool['name']:<15} - {tool['description']}")
        
        print(f"{Fore.GREEN}[5] Run All Available Tools")
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
            # Setup Go environment
            env = os.environ.copy()
            go_bin = os.path.expanduser("~/go/bin")
            
            if 'PATH' in env:
                env['PATH'] = f"{go_bin}:{env['PATH']}"
            else:
                env['PATH'] = go_bin
            
            if 'GOPATH' not in env:
                env['GOPATH'] = os.path.expanduser("~/go")
            
            # Install
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
                if process.stderr:
                    print(f"{Fore.RED}{process.stderr[:200]}{Style.RESET_ALL}")
                return False
                
        except Exception as e:
            print(f"{Fore.RED}[!] Installation error: {str(e)}{Style.RESET_ALL}")
            return False
    
    def run_tool(self, tool_info, domain, output_file):
        """Execute selected tool"""
        print(f"\n{Fore.CYAN}[*] Running {tool_info['name']} on {domain}...{Style.RESET_ALL}")
        print(f"{Fore.CYAN}[*] Output: {output_file}{Style.RESET_ALL}")
        
        # Prepare command
        command = tool_info['command'].format(domain=domain, output=output_file)
        
        # Check if tool exists and get full path if needed
        tool_check = check_tool_installed(tool_info['name'])
        if isinstance(tool_check, str):
            # Replace tool name with full path
            command = command.replace(tool_info['name'], tool_check)
        
        start_time = time.time()
        
        try:
            process = subprocess.run(
                command,
                shell=True,
                capture_output=True,
                text=True,
                timeout=600
            )
            
            elapsed = round(time.time() - start_time, 2)
            
            if process.returncode == 0:
                # Count results
                result_count = count_lines(output_file)
                
                print(f"{Fore.GREEN}[✓] Completed in {elapsed}s{Style.RESET_ALL}")
                print(f"{Fore.GREEN}[✓] Found {result_count} subdomains{Style.RESET_ALL}")
                
                # Show preview
                if result_count > 0:
                    preview = read_file_lines(output_file, 3)
                    print(f"{Fore.YELLOW}[*] Preview:{Style.RESET_ALL}")
                    for line in preview:
                        print(f"{Fore.WHITE}    {line}{Style.RESET_ALL}")
                    if result_count > 3:
                        print(f"{Fore.YELLOW}    ... and {result_count - 3} more{Style.RESET_ALL}")
                
                return True
            else:
                print(f"{Fore.RED}[!] Tool failed{Style.RESET_ALL}")
                if process.stderr:
                    print(f"{Fore.RED}{process.stderr[:200]}{Style.RESET_ALL}")
                return False
                
        except subprocess.TimeoutExpired:
            print(f"{Fore.RED}[!] Tool timed out (10 min limit){Style.RESET_ALL}")
            return False
        except Exception as e:
            print(f"{Fore.RED}[!] Error: {str(e)}{Style.RESET_ALL}")
            return False
    
    def combine_results(self, output_dir, domain):
        """Combine and deduplicate results from all tools"""
        print(f"\n{Fore.CYAN}[*] Combining results...{Style.RESET_ALL}")
        
        all_subdomains = set()
        
        # Read all result files
        for file in os.listdir(output_dir):
            if file.endswith('_results.txt'):
                filepath = os.path.join(output_dir, file)
                try:
                    with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
                        for line in f:
                            subdomain = line.strip()
                            if subdomain and domain in subdomain:
                                all_subdomains.add(subdomain)
                except:
                    continue
        
        # Save combined results
        if all_subdomains:
            combined_file = os.path.join(output_dir, "all_subdomains.txt")
            with open(combined_file, 'w') as f:
                for subdomain in sorted(all_subdomains):
                    f.write(f"{subdomain}\n")
            
            print(f"{Fore.GREEN}[✓] Combined: {len(all_subdomains)} unique subdomains{Style.RESET_ALL}")
            print(f"{Fore.GREEN}[✓] Saved to: {combined_file}{Style.RESET_ALL}")
        else:
            print(f"{Fore.YELLOW}[!] No subdomains found{Style.RESET_ALL}")
    
    def run(self):
        """Main module execution"""
        while True:
            self.show_menu()
            
            choice = input(f"\n{Fore.WHITE}Select tool [0-5]: {Style.RESET_ALL}").strip()
            
            if choice == '0':
                break
            
            if choice not in ['1', '2', '3', '4', '5']:
                print(f"{Fore.RED}[!] Invalid choice{Style.RESET_ALL}")
                continue
            
            # Get target domain
            domain = input(f"{Fore.WHITE}Enter target domain: {Style.RESET_ALL}").strip()
            domain = validate_domain(domain)
            
            if not domain:
                print(f"{Fore.RED}[!] Invalid domain format{Style.RESET_ALL}")
                continue
            
            # Create output directory
            output_dir = create_output_dir(domain)
            print(f"{Fore.CYAN}[*] Output directory: {output_dir}{Style.RESET_ALL}")
            
            if choice == '5':
                # Run all tools
                for key, tool_info in self.tools.items():
                    # Check if installed
                    if not check_tool_installed(tool_info['name']) and tool_info['name'] != 'crt.sh':
                        print(f"\n{Fore.YELLOW}[!] {tool_info['name']} not installed, skipping{Style.RESET_ALL}")
                        continue
                    
                    output_file = os.path.join(output_dir, f"{tool_info['name']}_results.txt")
                    self.run_tool(tool_info, domain, output_file)
                
                # Combine results
                self.combine_results(output_dir, domain)
            else:
                # Run single tool
                tool_info = self.tools[choice]
                
                # Check installation
                if not check_tool_installed(tool_info['name']) and tool_info['name'] != 'crt.sh':
                    if not self.install_tool(tool_info):
                        continue
                
                output_file = os.path.join(output_dir, f"{tool_info['name']}_results.txt")
                self.run_tool(tool_info, domain, output_file)
            
            input(f"\n{Fore.YELLOW}Press Enter to continue...{Style.RESET_ALL}")

if __name__ == "__main__":
    module = SubdomainEnumeration()
    module.run()
