#!/bin/bash
# RECON VAPT Framework - Complete Installation Script for Kali Linux

echo "╔═══════════════════════════════════════════════════════════════════╗"
echo "║              RECON VAPT FRAMEWORK - INSTALLER                     ║"
echo "║                   Quick & Simple Setup                            ║"
echo "╚═══════════════════════════════════════════════════════════════════╝"

# Colors
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m'

echo -e "${BLUE}[*]${NC} Starting installation..."

# Step 1: Update system
echo -e "\n${BLUE}[*]${NC} Updating system packages..."
sudo apt update > /dev/null 2>&1

# Step 2: Install Python dependencies
echo -e "${BLUE}[*]${NC} Installing Python dependencies..."
sudo apt install -y python3-pip curl jq > /dev/null 2>&1

# Install Python packages individually
echo -e "${BLUE}[*]${NC} Installing colorama..."
pip3 install colorama --break-system-packages 2>/dev/null || pip3 install colorama 2>/dev/null

echo -e "${BLUE}[*]${NC} Installing requests..."
pip3 install requests --break-system-packages 2>/dev/null || pip3 install requests 2>/dev/null

# Verify
if python3 -c "import colorama, requests" 2>/dev/null; then
    echo -e "${GREEN}[✓]${NC} Python dependencies installed"
else
    echo -e "${YELLOW}[!]${NC} Python packages may need manual install"
    echo -e "${YELLOW}[*]${NC} Try: pip3 install colorama requests --break-system-packages"
fi

# Step 3: Install Go (if not present)
echo -e "${BLUE}[*]${NC} Checking Go installation..."
if ! command -v go &> /dev/null; then
    echo -e "${BLUE}[*]${NC} Installing Go..."
    sudo apt install -y golang-go > /dev/null 2>&1
fi

# Step 4: Setup Go environment
export GOPATH=$HOME/go
export PATH=$PATH:$GOPATH/bin
mkdir -p ~/go/bin

# Add to bashrc if not present
if ! grep -q "export GOPATH=\$HOME/go" ~/.bashrc; then
    echo 'export GOPATH=$HOME/go' >> ~/.bashrc
    echo 'export PATH=$PATH:$GOPATH/bin' >> ~/.bashrc
fi

echo -e "${GREEN}[✓]${NC} Go environment configured"

# Step 5: Install Go-based tools
echo -e "${BLUE}[*]${NC} Installing reconnaissance tools..."

# Subdomain enumeration tools
go install -v github.com/projectdiscovery/subfinder/v2/cmd/subfinder@latest 2>/dev/null && echo -e "${GREEN}[✓]${NC} subfinder"
go install github.com/tomnomnom/assetfinder@latest 2>/dev/null && echo -e "${GREEN}[✓]${NC} assetfinder"
go install -v github.com/projectdiscovery/httpx/cmd/httpx@latest 2>/dev/null && echo -e "${GREEN}[✓]${NC} httpx"

# Directory discovery tools
go install github.com/ffuf/ffuf@latest 2>/dev/null && echo -e "${GREEN}[✓]${NC} ffuf"
go install github.com/OJ/gobuster/v3@latest 2>/dev/null && echo -e "${GREEN}[✓]${NC} gobuster"

# Port scanning tools
go install -v github.com/projectdiscovery/naabu/v2/cmd/naabu@latest 2>/dev/null && echo -e "${GREEN}[✓]${NC} naabu"

# Screenshot tools
go install github.com/sensepost/gowitness@latest 2>/dev/null && echo -e "${GREEN}[✓]${NC} gowitness"
go install github.com/michenriksen/aquatone@latest 2>/dev/null && echo -e "${GREEN}[✓]${NC} aquatone"

# Vulnerability scanning
go install -v github.com/projectdiscovery/nuclei/v2/cmd/nuclei@latest 2>/dev/null && echo -e "${GREEN}[✓]${NC} nuclei"

# Step 6: Install system tools
echo -e "${BLUE}[*]${NC} Installing system tools..."
sudo apt install -y nmap masscan nikto sqlmap dirb whatweb > /dev/null 2>&1
echo -e "${GREEN}[✓]${NC} System tools installed"

# Step 7: Install Python tools
echo -e "${BLUE}[*]${NC} Installing Python tools..."
pip3 install arjun > /dev/null 2>&1 && echo -e "${GREEN}[✓]${NC} arjun"

# Step 8: Set permissions
chmod +x reconvapt.py
echo -e "${GREEN}[✓]${NC} Permissions set"

# Step 9: Create directories
mkdir -p output logs wordlists
echo -e "${GREEN}[✓]${NC} Directories created"

# Summary
echo -e "\n${GREEN}╔═══════════════════════════════════════════════════════════════════╗"
echo -e "║                  INSTALLATION COMPLETE!                           ║"
echo -e "╚═══════════════════════════════════════════════════════════════════╝${NC}"

echo -e "\n${BLUE}[*]${NC} Quick Start:"
echo -e "    1. Reload shell: ${YELLOW}source ~/.bashrc${NC}"
echo -e "    2. Run framework: ${YELLOW}python3 reconvapt.py${NC}"

echo -e "\n${BLUE}[*]${NC} If tools not found, run: ${YELLOW}export PATH=\$PATH:~/go/bin${NC}"

echo -e "\n${GREEN}[✓]${NC} All done! Happy hunting! 🎯"
