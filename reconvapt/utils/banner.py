#!/usr/bin/env python3
"""
RECON VAPT Framework - Banner Display
"""

from colorama import Fore, Style

def print_banner():
    """Print the RECON VAPT Framework banner"""
    banner = f"""
{Fore.RED}
██████╗ ███████╗ ██████╗ ██████╗ ███╗   ██╗    ██╗   ██╗ █████╗ ██████╗ ████████╗
██╔══██╗██╔════╝██╔════╝██╔═══██╗████╗  ██║    ██║   ██║██╔══██╗██╔══██╗╚══██╔══╝
██████╔╝█████╗  ██║     ██║   ██║██╔██╗ ██║    ██║   ██║███████║██████╔╝   ██║   
██╔══██╗██╔══╝  ██║     ██║   ██║██║╚██╗██║    ╚██╗ ██╔╝██╔══██║██╔═══╝    ██║   
██║  ██║███████╗╚██████╗╚██████╔╝██║ ╚████║     ╚████╔╝ ██║  ██║██║        ██║   
╚═╝  ╚═╝╚══════╝ ╚═════╝ ╚═════╝ ╚═╝  ╚═══╝      ╚═══╝  ╚═╝  ╚═╝╚═╝        ╚═╝   
{Style.RESET_ALL}
{Fore.CYAN}╔═══════════════════════════════════════════════════════════════════════════╗
║          Vulnerability Assessment & Penetration Testing Framework         ║
║                         Simplified & Reliable Edition                     ║
║                                                                           ║
║ {Fore.YELLOW}Version: 2.0                                                             {Fore.CYAN}║
║ {Fore.YELLOW}Target: Kali Linux                                                       {Fore.CYAN}║
║ {Fore.YELLOW}Focus: Speed, Simplicity, Reliability                                   {Fore.CYAN}║
╚═══════════════════════════════════════════════════════════════════════════╝{Style.RESET_ALL}
"""
    print(banner)
