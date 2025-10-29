#!/bin/bash

# RECON VAPT Framework Installation Verification Script
# This script checks if all required tools are properly installed

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

echo -e "${BLUE}═══════════════════════════════════════════════${NC}"
echo -e "${BLUE}  RECON VAPT - Installation Verification${NC}"
echo -e "${BLUE}═══════════════════════════════════════════════${NC}\n"

# Track status
TOTAL=0
INSTALLED=0
MISSING=0

# Function to check if command exists
check_tool() {
    local tool=$1
    local name=$2
    TOTAL=$((TOTAL + 1))
    
    if command -v $tool &> /dev/null; then
        echo -e "[${GREEN}✓${NC}] $name - Installed"
        INSTALLED=$((INSTALLED + 1))
        return 0
    else
        echo -e "[${RED}✗${NC}] $name - Missing"
        MISSING=$((MISSING + 1))
        return 1
    fi
}

# Function to check Go bin path
check_go_path() {
    if command -v subfinder &> /dev/null; then
        return 0
    elif [ -f "$HOME/go/bin/subfinder" ]; then
        echo -e "${YELLOW}[!] Go tools found but not in PATH${NC}"
        echo -e "${YELLOW}[!] Add to PATH: export PATH=\$PATH:\$HOME/go/bin${NC}\n"
        return 1
    fi
}

echo -e "${YELLOW}Checking Go-based tools...${NC}"
check_tool "subfinder" "Subfinder"
check_tool "assetfinder" "Assetfinder"
check_tool "httpx" "HTTPX"
check_tool "ffuf" "FFUF"
check_tool "gobuster" "Gobuster"
check_tool "naabu" "Naabu"
check_tool "gowitness" "GoWitness"
check_tool "aquatone" "Aquatone"
check_tool "nuclei" "Nuclei"

echo -e "\n${YELLOW}Checking system tools...${NC}"
check_tool "nmap" "Nmap"
check_tool "masscan" "Masscan"
check_tool "nikto" "Nikto"
check_tool "sqlmap" "SQLMap"
check_tool "dirb" "Dirb"
check_tool "whatweb" "WhatWeb"

echo -e "\n${YELLOW}Checking Python tools...${NC}"
check_tool "arjun" "Arjun"

echo -e "\n${YELLOW}Checking Python modules...${NC}"
TOTAL=$((TOTAL + 2))

if python3 -c "import colorama" 2>/dev/null; then
    echo -e "[${GREEN}✓${NC}] Colorama - Installed"
    INSTALLED=$((INSTALLED + 1))
else
    echo -e "[${RED}✗${NC}] Colorama - Missing"
    MISSING=$((MISSING + 1))
fi

if python3 -c "import requests" 2>/dev/null; then
    echo -e "[${GREEN}✓${NC}] Requests - Installed"
    INSTALLED=$((INSTALLED + 1))
else
    echo -e "[${RED}✗${NC}] Requests - Missing"
    MISSING=$((MISSING + 1))
fi

echo -e "\n${YELLOW}Checking environment...${NC}"
TOTAL=$((TOTAL + 2))

if [ -d "$HOME/go" ]; then
    echo -e "[${GREEN}✓${NC}] Go workspace - Found"
    INSTALLED=$((INSTALLED + 1))
else
    echo -e "[${RED}✗${NC}] Go workspace - Missing"
    MISSING=$((MISSING + 1))
fi

if [[ ":$PATH:" == *":$HOME/go/bin:"* ]]; then
    echo -e "[${GREEN}✓${NC}] Go bin in PATH - Yes"
    INSTALLED=$((INSTALLED + 1))
else
    echo -e "[${YELLOW}✗${NC}] Go bin in PATH - No"
    echo -e "    ${YELLOW}Run: export PATH=\$PATH:\$HOME/go/bin${NC}"
    MISSING=$((MISSING + 1))
fi

# Summary
echo -e "\n${BLUE}═══════════════════════════════════════════════${NC}"
echo -e "${BLUE}  Installation Summary${NC}"
echo -e "${BLUE}═══════════════════════════════════════════════${NC}"
echo -e "Total Checks:    ${TOTAL}"
echo -e "${GREEN}Installed:       ${INSTALLED}${NC}"
echo -e "${RED}Missing:         ${MISSING}${NC}"

if [ $MISSING -eq 0 ]; then
    echo -e "\n${GREEN}✓ All tools installed successfully!${NC}"
    echo -e "${GREEN}✓ Ready to use RECON VAPT Framework${NC}\n"
    exit 0
else
    echo -e "\n${RED}✗ Some tools are missing${NC}"
    echo -e "${YELLOW}Run ./install.sh to install missing tools${NC}\n"
    exit 1
fi
