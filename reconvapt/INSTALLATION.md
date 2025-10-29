# 📦 INSTALLATION GUIDE - RECON VAPT Framework

## Prerequisites
- **Operating System**: Kali Linux (recommended) or any Debian-based Linux
- **Python**: Version 3.6 or higher
- **Go**: Version 1.16 or higher
- **Internet Connection**: Required for downloading tools
- **Root/Sudo Access**: Required for system tool installation

---

## 🚀 Method 1: Automated Installation (Recommended)

### Step 1: Prepare the Framework
```bash
# Navigate to the framework directory
cd /path/to/reconvapt

# Make scripts executable
chmod +x install.sh verify_install.sh
```

### Step 2: Run the Installer
```bash
# Execute the installation script
./install.sh
```

**What it does:**
- Updates system packages
- Installs Python dependencies (colorama, requests)
- Installs Go programming language
- Configures Go environment variables
- Installs 9 Go-based security tools
- Installs 5 system security tools
- Installs Python-based tools (arjun)
- Sets up directory structure

**Installation Time**: 10-15 minutes (depends on internet speed)

### Step 3: Reload Shell Environment
```bash
# Reload bash configuration
source ~/.bashrc

# OR close and reopen terminal
```

### Step 4: Verify Installation
```bash
# Run verification script
./verify_install.sh
```

**Expected Output:**
```
═══════════════════════════════════════════════
  RECON VAPT - Installation Verification
═══════════════════════════════════════════════

Checking Go-based tools...
[✓] Subfinder - Installed
[✓] Assetfinder - Installed
[✓] HTTPX - Installed
[✓] FFUF - Installed
[✓] Gobuster - Installed
[✓] Naabu - Installed
[✓] GoWitness - Installed
[✓] Aquatone - Installed
[✓] Nuclei - Installed

Checking system tools...
[✓] Nmap - Installed
[✓] Masscan - Installed
[✓] Nikto - Installed
[✓] SQLMap - Installed
[✓] Dirb - Installed
[✓] WhatWeb - Installed

Checking Python tools...
[✓] Arjun - Installed

Checking Python modules...
[✓] Colorama - Installed
[✓] Requests - Installed

Checking environment...
[✓] Go workspace - Found
[✓] Go bin in PATH - Yes

═══════════════════════════════════════════════
  Installation Summary
═══════════════════════════════════════════════
Total Checks:    19
Installed:       19
Missing:         0

✓ All tools installed successfully!
✓ Ready to use RECON VAPT Framework
```

### Step 5: Test the Framework
```bash
# Run basic functionality test
python3 test_framework.py

# Start the framework
python3 reconvapt.py
```

---

## 🔧 Method 2: Manual Installation

### Step 1: System Update
```bash
sudo apt update
sudo apt upgrade -y
```

### Step 2: Install Python Dependencies
```bash
# Install pip if not present
sudo apt install python3-pip -y

# Install required Python packages
pip3 install colorama requests
```

### Step 3: Install Go Programming Language
```bash
# Install Go
sudo apt install golang-go -y

# Configure Go environment
export GOPATH=$HOME/go
export PATH=$PATH:$GOPATH/bin

# Make permanent
echo 'export GOPATH=$HOME/go' >> ~/.bashrc
echo 'export PATH=$PATH:$GOPATH/bin' >> ~/.bashrc
source ~/.bashrc
```

### Step 4: Install Go-based Security Tools
```bash
# Subdomain enumeration tools
go install -v github.com/projectdiscovery/subfinder/v2/cmd/subfinder@latest
go install github.com/tomnomnom/assetfinder@latest

# HTTP toolkit
go install -v github.com/projectdiscovery/httpx/cmd/httpx@latest

# Fuzzing and directory discovery
go install github.com/ffuf/ffuf@latest
go install github.com/OJ/gobuster/v3@latest

# Port scanning
go install -v github.com/projectdiscovery/naabu/v2/cmd/naabu@latest

# Screenshot tools
go install github.com/sensepost/gowitness@latest
go install github.com/michenriksen/aquatone@latest

# Vulnerability scanning
go install -v github.com/projectdiscovery/nuclei/v2/cmd/nuclei@latest
```

### Step 5: Install System Tools
```bash
# Install via apt
sudo apt install -y nmap masscan nikto sqlmap dirb whatweb

# Verify installation
which nmap masscan nikto sqlmap dirb whatweb
```

### Step 6: Install Python Tools
```bash
pip3 install arjun
```

### Step 7: Create Directory Structure
```bash
cd reconvapt
mkdir -p output logs wordlists
```

### Step 8: Verify Installation
```bash
# Check all tools
./verify_install.sh

# Test framework
python3 test_framework.py
```

---

## 🐛 Troubleshooting

### Issue 1: "Command not found" for Go tools

**Problem**: Tools like `subfinder`, `httpx`, `nuclei` not found

**Solution**:
```bash
# Check if Go bin is in PATH
echo $PATH | grep go/bin

# If not, add it
export PATH=$PATH:$HOME/go/bin

# Make permanent
echo 'export PATH=$PATH:$HOME/go/bin' >> ~/.bashrc
source ~/.bashrc
```

### Issue 2: "No module named 'colorama'"

**Problem**: Python dependencies not installed

**Solution**:
```bash
pip3 install colorama requests

# Or with sudo if needed
sudo pip3 install colorama requests
```

### Issue 3: Go installation fails

**Problem**: Go not properly installed

**Solution**:
```bash
# Remove old Go installation
sudo apt remove golang-go
sudo apt autoremove

# Install latest Go
sudo apt update
sudo apt install golang-go -y

# Verify
go version
```

### Issue 4: Permission denied errors

**Problem**: Files not executable

**Solution**:
```bash
chmod +x install.sh verify_install.sh
chmod +x reconvapt.py test_framework.py
```

### Issue 5: Some Go tools fail to install

**Problem**: Network issues or repository changes

**Solution**:
```bash
# Try installing one by one
go install -v github.com/projectdiscovery/subfinder/v2/cmd/subfinder@latest

# Check Go proxy settings
go env -w GOPROXY=https://proxy.golang.org,direct

# Retry installation
./install.sh
```

### Issue 6: Masscan requires root privileges

**Problem**: Masscan needs root for raw socket access

**Solution**:
```bash
# Run with sudo when using masscan
sudo python3 reconvapt.py

# Or set capabilities (one-time setup)
sudo setcap cap_net_raw,cap_net_admin,cap_net_bind_service+eip /usr/bin/masscan
```

---

## ✅ Post-Installation Checklist

- [ ] All 19 checks pass in `verify_install.sh`
- [ ] `python3 test_framework.py` completes successfully
- [ ] `python3 reconvapt.py` shows main menu
- [ ] Go tools are in PATH (`which subfinder`)
- [ ] Python modules import correctly
- [ ] Output and logs directories exist
- [ ] Test with a safe domain you own

---

## 🔄 Updating Tools

### Update Go-based tools
```bash
# Update individual tools
go install -v github.com/projectdiscovery/subfinder/v2/cmd/subfinder@latest
go install -v github.com/projectdiscovery/httpx/cmd/httpx@latest
go install -v github.com/projectdiscovery/nuclei/v2/cmd/nuclei@latest
go install -v github.com/projectdiscovery/naabu/v2/cmd/naabu@latest
go install github.com/ffuf/ffuf@latest

# Update nuclei templates
nuclei -update-templates
```

### Update system tools
```bash
sudo apt update
sudo apt upgrade nmap nikto sqlmap masscan dirb whatweb
```

### Update Python packages
```bash
pip3 install --upgrade colorama requests arjun
```

---

## 📊 System Requirements Details

### Minimum Requirements
- **CPU**: 2 cores
- **RAM**: 4GB
- **Disk**: 5GB free space
- **Network**: Stable internet connection

### Recommended Requirements
- **CPU**: 4+ cores
- **RAM**: 8GB+
- **Disk**: 20GB+ free space (for wordlists and results)
- **Network**: High-speed internet

---

## 🎯 First Run After Installation

```bash
# Step 1: Navigate to framework
cd reconvapt

# Step 2: Start framework
python3 reconvapt.py

# Step 3: Try subdomain enumeration
# Select [1] Subdomain Enumeration
# Choose [1] subfinder
# Enter a test domain (that you own!)

# Step 4: Check results
ls -lh output/
```

---

## 🆘 Getting Help

If installation fails:

1. **Check logs**: Look in `logs/` directory
2. **Run verification**: `./verify_install.sh` to see what's missing
3. **Test imports**: `python3 test_framework.py`
4. **Check PATH**: `echo $PATH | grep go`
5. **Manual verify**: `which subfinder httpx nmap`
6. **Re-run installer**: `./install.sh` is idempotent (safe to re-run)

---

## 📝 Notes

- Installation requires internet connection
- Some tools may take 2-3 minutes to compile (Go-based tools)
- Kali Linux users may already have some tools pre-installed
- The framework will auto-detect and skip already installed tools
- All tools are installed from official repositories
- No modifications to system Python (uses pip3)

---

**Next Steps**: Read `QUICKSTART.md` for usage examples

**Full Documentation**: See `README.md`

**Ready to start?** Run: `python3 reconvapt.py`
