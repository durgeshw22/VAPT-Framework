#!/usr/bin/env python3
"""
RECON VAPT Framework - Basic Functionality Test
Tests if the framework loads correctly without errors
"""

import sys
import os

# Add current directory to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

print("[*] Testing RECON VAPT Framework...")
print("-" * 50)

# Test 1: Import utilities
print("[1] Testing utility imports...")
try:
    from utils.banner import print_banner
    from utils.logger import setup_logger
    from utils.helpers import validate_domain, validate_url, validate_ip
    print("    ✓ Utilities imported successfully")
except ImportError as e:
    print(f"    ✗ Failed to import utilities: {e}")
    sys.exit(1)

# Test 2: Import modules
print("[2] Testing module imports...")
try:
    from modules.subdomain_enum import SubdomainEnumeration
    from modules.directory_discovery import DirectoryDiscovery
    from modules.port_scanning import PortScanning
    from modules.screenshot_capture import ScreenshotCapture
    from modules.vulnerability_scanning import VulnerabilityScanning
    from modules.parameter_discovery import ParameterDiscovery
    from modules.javascript_discovery import JavaScriptDiscovery
    from modules.technology_detection import TechnologyDetection
    print("    ✓ All 8 modules imported successfully")
except ImportError as e:
    print(f"    ✗ Failed to import modules: {e}")
    sys.exit(1)

# Test 3: Test helper functions
print("[3] Testing helper functions...")
try:
    # Test domain validation (returns cleaned domain or None)
    assert validate_domain("example.com") == "example.com"
    assert validate_domain("invalid domain") == None
    
    # Test URL validation (returns URL with protocol)
    assert validate_url("http://example.com") == "http://example.com"
    assert validate_url("example.com").startswith("http://")
    
    # Test IP validation (returns True/False)
    assert validate_ip("192.168.1.1") == True
    assert validate_ip("999.999.999.999") == False
    
    print("    ✓ Helper functions working correctly")
except AssertionError as e:
    print(f"    ✗ Helper function validation failed: {e}")
    sys.exit(1)

# Test 4: Test logger
print("[4] Testing logger...")
try:
    logger = setup_logger()
    logger.info("Test log entry")
    print("    ✓ Logger initialized successfully")
except Exception as e:
    print(f"    ✗ Logger failed: {e}")
    sys.exit(1)

# Test 5: Test banner
print("[5] Testing banner display...")
try:
    print("\n" + "="*50)
    print_banner()
    print("="*50)
    print("    ✓ Banner displayed successfully")
except Exception as e:
    print(f"    ✗ Banner failed: {e}")
    sys.exit(1)

# Test 6: Test module initialization
print("[6] Testing module initialization...")
try:
    subdomain = SubdomainEnumeration()
    directory = DirectoryDiscovery()
    ports = PortScanning()
    screenshot = ScreenshotCapture()
    vuln = VulnerabilityScanning()
    params = ParameterDiscovery()
    js = JavaScriptDiscovery()
    tech = TechnologyDetection()
    print("    ✓ All modules initialized successfully")
except Exception as e:
    print(f"    ✗ Module initialization failed: {e}")
    sys.exit(1)

# Test 7: Check directory creation
print("[7] Testing directory structure...")
try:
    os.makedirs("output", exist_ok=True)
    os.makedirs("logs", exist_ok=True)
    os.makedirs("wordlists", exist_ok=True)
    print("    ✓ Required directories created/verified")
except Exception as e:
    print(f"    ✗ Directory creation failed: {e}")
    sys.exit(1)

# Test 8: Python version check
print("[8] Checking Python version...")
if sys.version_info >= (3, 6):
    print(f"    ✓ Python {sys.version_info.major}.{sys.version_info.minor} - Compatible")
else:
    print(f"    ✗ Python {sys.version_info.major}.{sys.version_info.minor} - Requires 3.6+")
    sys.exit(1)

# Summary
print("\n" + "="*50)
print("✓ ALL TESTS PASSED!")
print("="*50)
print("\n[*] Framework is ready to use")
print("[*] Run: python3 reconvapt.py")
print("-" * 50)
