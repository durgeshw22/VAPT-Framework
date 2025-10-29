#!/usr/bin/env python3
"""
RECON VAPT Framework - Helper Utilities
"""

import os
import re
import subprocess
import time
from colorama import Fore

def validate_domain(domain):
    """Validate and clean domain input"""
    if not domain:
        return None
    
    # Remove protocol
    domain = domain.replace('http://', '').replace('https://', '')
    
    # Remove path and port
    domain = domain.split('/')[0].split(':')[0]
    
    # Basic validation
    domain_pattern = re.compile(
        r'^(?:[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?\.)*[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?$'
    )
    
    if domain_pattern.match(domain) and '.' in domain:
        return domain.lower()
    
    return None

def validate_url(url):
    """Validate URL format"""
    if not url:
        return None
    
    # Add protocol if missing
    if not url.startswith(('http://', 'https://')):
        url = 'http://' + url
    
    return url

def validate_ip(ip):
    """Validate IP address"""
    ip_pattern = re.compile(
        r'^((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$'
    )
    return ip_pattern.match(ip) is not None

def create_output_dir(base_name):
    """Create timestamped output directory"""
    from datetime import datetime
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_path = os.path.join("output", f"{base_name}_{timestamp}")
    
    if not os.path.exists(output_path):
        os.makedirs(output_path)
    
    return output_path

def check_tool_installed(tool_name):
    """Check if a tool is installed and accessible"""
    # Check in PATH
    try:
        result = subprocess.run(['which', tool_name], 
                             capture_output=True, 
                             text=True, 
                             timeout=5)
        if result.returncode == 0:
            return True
    except:
        pass
    
    # Check common Go paths
    go_paths = [
        os.path.expanduser(f"~/go/bin/{tool_name}"),
        f"/usr/local/bin/{tool_name}",
        f"/usr/bin/{tool_name}"
    ]
    
    for path in go_paths:
        if os.path.exists(path) and os.access(path, os.X_OK):
            return path
    
    return False

def run_command(command, timeout=600):
    """Execute shell command with timeout"""
    start_time = time.time()
    
    try:
        process = subprocess.run(
            command,
            shell=True,
            capture_output=True,
            text=True,
            timeout=timeout
        )
        
        execution_time = round(time.time() - start_time, 2)
        
        return {
            'success': process.returncode == 0,
            'returncode': process.returncode,
            'stdout': process.stdout,
            'stderr': process.stderr,
            'execution_time': execution_time
        }
    except subprocess.TimeoutExpired:
        return {
            'success': False,
            'returncode': -1,
            'stdout': '',
            'stderr': f'Command timed out after {timeout} seconds',
            'execution_time': timeout
        }
    except Exception as e:
        return {
            'success': False,
            'returncode': -1,
            'stdout': '',
            'stderr': str(e),
            'execution_time': time.time() - start_time
        }

def count_lines(file_path):
    """Count non-empty lines in file"""
    try:
        with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
            return sum(1 for line in f if line.strip())
    except:
        return 0

def read_file_lines(file_path, limit=5):
    """Read first N lines from file"""
    try:
        with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
            lines = []
            for i, line in enumerate(f):
                if i >= limit:
                    break
                if line.strip():
                    lines.append(line.strip())
            return lines
    except:
        return []
