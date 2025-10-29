#!/usr/bin/env python3
"""
RECON VAPT Framework - Main Application
Simplified & Reliable Penetration Testing Toolkit
"""

import sys
import os
from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)

# Import modules
from utils.banner import print_banner
from modules.subdomain_enum import SubdomainEnumeration
from modules.directory_discovery import DirectoryDiscovery
from modules.port_scanning import PortScanning
from modules.screenshot_capture import ScreenshotCapture
from modules.vulnerability_scanning import VulnerabilityScanning
from modules.parameter_discovery import ParameterDiscovery
from modules.javascript_discovery import JavaScriptDiscovery
from modules.technology_detection import TechnologyDetection

class ReconVAPT:
    def __init__(self):
        self.modules = {
            "1": {
                "name": "Subdomain Enumeration",
                "class": SubdomainEnumeration,
                "description": "Discover subdomains (4 tools)"
            },
            "2": {
                "name": "Directory/File Discovery",
                "class": DirectoryDiscovery,
                "description": "Find hidden paths (3 tools)"
            },
            "3": {
                "name": "Port Scanning",
                "class": PortScanning,
                "description": "Scan open ports (3 tools)"
            },
            "4": {
                "name": "Screenshot Capture",
                "class": ScreenshotCapture,
                "description": "Capture screenshots (2 tools)"
            },
            "5": {
                "name": "Vulnerability Scanning",
                "class": VulnerabilityScanning,
                "description": "Automated vuln assessment (3 tools)"
            },
            "6": {
                "name": "Parameter Discovery",
                "class": ParameterDiscovery,
                "description": "Find hidden parameters (2 tools)"
            },
            "7": {
                "name": "JavaScript Discovery",
                "class": JavaScriptDiscovery,
                "description": "Analyze JS files (2 tools)"
            },
            "8": {
                "name": "Technology Detection",
                "class": TechnologyDetection,
                "description": "Identify technologies (2 tools)"
            }
        }
    
    def show_main_menu(self):
        """Display main menu"""
        print_banner()
        
        print(f"\n{Fore.CYAN}╔══════════════════════════════════════════════════════════════════╗")
        print(f"{Fore.CYAN}║                        MAIN MENU                                 ║")
        print(f"{Fore.CYAN}╠══════════════════════════════════════════════════════════════════╣")
        
        for key, module in self.modules.items():
            print(f"{Fore.WHITE}║  [{Fore.YELLOW}{key}{Fore.WHITE}] {module['name']:<30} {Fore.CYAN}{module['description']:<22}{Fore.WHITE} ║")
        
        print(f"{Fore.CYAN}╠══════════════════════════════════════════════════════════════════╣")
        print(f"{Fore.RED}║  [0] Exit Framework                                              ║")
        print(f"{Fore.CYAN}╚══════════════════════════════════════════════════════════════════╝{Style.RESET_ALL}")
    
    def run(self):
        """Main application loop"""
        try:
            while True:
                self.show_main_menu()
                
                choice = input(f"\n{Fore.WHITE}Select module [0-8]: {Style.RESET_ALL}").strip()
                
                if choice == '0':
                    print(f"\n{Fore.GREEN}[✓] Thanks for using RECON VAPT Framework!{Style.RESET_ALL}")
                    sys.exit(0)
                
                if choice in self.modules:
                    module_info = self.modules[choice]
                    print(f"\n{Fore.CYAN}[*] Loading {module_info['name']}...{Style.RESET_ALL}")
                    
                    try:
                        module_instance = module_info['class']()
                        module_instance.run()
                    except KeyboardInterrupt:
                        print(f"\n{Fore.YELLOW}[!] Module interrupted{Style.RESET_ALL}")
                    except Exception as e:
                        print(f"\n{Fore.RED}[!] Module error: {str(e)}{Style.RESET_ALL}")
                else:
                    print(f"{Fore.RED}[!] Invalid choice{Style.RESET_ALL}")
                
        except KeyboardInterrupt:
            print(f"\n{Fore.RED}[!] Interrupted by user{Style.RESET_ALL}")
            sys.exit(0)
        except Exception as e:
            print(f"\n{Fore.RED}[!] Fatal error: {str(e)}{Style.RESET_ALL}")
            sys.exit(1)

def main():
    """Entry point"""
    # Check Python version
    if sys.version_info < (3, 6):
        print(f"{Fore.RED}[!] Python 3.6+ required{Style.RESET_ALL}")
        sys.exit(1)
    
    # Create necessary directories
    for directory in ['output', 'logs', 'wordlists']:
        if not os.path.exists(directory):
            os.makedirs(directory)
    
    # Run framework
    framework = ReconVAPT()
    framework.run()

if __name__ == "__main__":
    main()
