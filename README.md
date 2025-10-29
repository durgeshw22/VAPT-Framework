# RECON VAPT Framework
**Simplified & Reliable Vulnerability Assessment and Penetration Testing Toolkit**

## 🎯 Overview
A clean, efficient VAPT framework with 8 modules and 21 carefully selected tools. Designed for Kali Linux with focus on simplicity, reliability, and ease of use.

## ✨ Features
- **8 Security Testing Modules** with hand-picked reliable tools
- **Simple CLI Interface** inspired by Social Engineering Toolkit
- **One-Command Installation** for all tools
- **Organized Output** with timestamped directories
- **Minimal Dependencies** - Just Python 3 and Go
- **Error Resilient** - Robust error handling throughout

## 📋 Modules & Tools

### 1. Subdomain Enumeration (4 tools)
- subfinder - Fast passive enumeration
- assetfinder - Multi-source subdomain finder
- httpx - HTTP toolkit & validator
- crt.sh - Certificate Transparency search

### 2. Directory/File Discovery (3 tools)
- ffuf - Fast web fuzzer
- gobuster - Directory brute-forcer
- dirb - Web content scanner

### 3. Port Scanning (3 tools)
- nmap - Network scanner (pre-installed)
- naabu - Fast SYN scanner
- masscan - High-speed scanner

### 4. Screenshot Capture (2 tools)
- gowitness - Screenshot utility
- aquatone - Visual inspection tool

### 5. Vulnerability Scanning (3 tools)
- nuclei - Template-based scanner
- nikto - Web server scanner (pre-installed)
- sqlmap - SQL injection tool (pre-installed)

### 6. Parameter Discovery (2 tools)
- arjun - HTTP parameter finder
- ffuf - Parameter fuzzer

### 7. JavaScript Discovery (2 tools)
- linkfinder - Endpoint discovery in JS
- httpx - JavaScript file finder

### 8. Technology Detection (2 tools)
- httpx - Tech detection via HTTP
- whatweb - Technology identifier (pre-installed)

## 🚀 Installation

### Quick Install (Kali Linux)
```bash
# Clone or download the framework
cd reconvapt

# Run automated installer
chmod +x install.sh
./install.sh

# Reload shell
source ~/.bashrc

# Run the framework
python3 reconvapt.py
```

### Manual Installation
```bash
# 1. Install Python dependencies
pip3 install colorama requests

# 2. Setup Go environment
export GOPATH=$HOME/go
export PATH=$PATH:$GOPATH/bin
echo 'export GOPATH=$HOME/go' >> ~/.bashrc
echo 'export PATH=$PATH:$GOPATH/bin' >> ~/.bashrc

# 3. Install Go-based tools
go install -v github.com/projectdiscovery/subfinder/v2/cmd/subfinder@latest
go install github.com/tomnomnom/assetfinder@latest
go install -v github.com/projectdiscovery/httpx/cmd/httpx@latest
go install github.com/ffuf/ffuf@latest
go install github.com/OJ/gobuster/v3@latest
go install -v github.com/projectdiscovery/naabu/v2/cmd/naabu@latest
go install github.com/sensepost/gowitness@latest
go install github.com/michenriksen/aquatone@latest
go install -v github.com/projectdiscovery/nuclei/v2/cmd/nuclei@latest

# 4. Install system tools
sudo apt install -y nmap masscan nikto sqlmap dirb whatweb

# 5. Install Python tools
pip3 install arjun

# 6. Run framework
python3 reconvapt.py
```

## 📖 Usage

### Basic Workflow
```bash
# Start framework
python3 reconvapt.py

# Select module (1-8)
# Choose tool from module menu
# Enter target (domain/URL/IP)
# View results in output directory
```

### Example: Subdomain Enumeration
```
1. Run: python3 reconvapt.py
2. Select: [1] Subdomain Enumeration
3. Choose: [1] subfinder
4. Enter: example.com
5. Results: output/example.com_20241028_123456/subfinder_results.txt
```

### Example: Directory Discovery
```
1. Select: [2] Directory/File Discovery
2. Choose: [1] ffuf
3. Enter: http://example.com
4. Select wordlist: [1] Common
5. Results: output/dir_example.com_timestamp/ffuf_results.txt
```

## 📁 Project Structure
```
reconvapt/
├── reconvapt.py              # Main application
├── install.sh                # Installation script
├── requirements.txt          # Python dependencies
├── modules/
│   ├── subdomain_enum.py
│   ├── directory_discovery.py
│   ├── port_scanning.py
│   ├── screenshot_capture.py
│   ├── vulnerability_scanning.py
│   ├── parameter_discovery.py
│   ├── javascript_discovery.py
│   └── technology_detection.py
├── utils/
│   ├── banner.py             # ASCII banner
│   ├── logger.py             # Logging utility
│   └── helpers.py            # Helper functions
├── output/                   # Scan results
├── logs/                     # Application logs
└── wordlists/                # Custom wordlists
```

## 🔧 Troubleshooting

### Tools Not Found
```bash
# Add Go bin to PATH
export PATH=$PATH:~/go/bin

# Or permanently
echo 'export PATH=$PATH:~/go/bin' >> ~/.bashrc
source ~/.bashrc
```

### Permission Denied
```bash
chmod +x reconvapt.py
chmod +x install.sh
```

### Import Errors
```bash
pip3 install colorama requests
```

### Go Installation Issues
```bash
sudo apt update
sudo apt install -y golang-go
```

## 💡 Tips

1. **Start Simple**: Begin with subfinder and assetfinder - most reliable
2. **Use Wordlists**: Kali has pre-installed wordlists in `/usr/share/wordlists/`
3. **Check Output**: All results saved in timestamped `output/` directories
4. **Tool Selection**: Each module offers multiple tools - choose what works best
5. **Rate Limiting**: Some tools auto-adjust speed to avoid rate limiting

## 🎯 Best Practices

- **Subdomain Enum**: Run subfinder first, then httpx to validate
- **Directory Discovery**: Start with common.txt, escalate if needed
- **Port Scanning**: Use naabu for speed, nmap for detail
- **Screenshots**: Useful after subdomain enumeration
- **Vulnerability Scanning**: Run nuclei with updated templates
- **Always verify findings** - automated tools may have false positives

## ⚠️ Legal Disclaimer
This tool is for **authorized security testing only**. Users are responsible for complying with applicable laws. Unauthorized access is illegal.

## 📊 System Requirements
- **OS**: Kali Linux (recommended)
- **Python**: 3.6+
- **Go**: 1.16+
- **RAM**: 4GB minimum
- **Disk**: 2GB for tools and wordlists

## 🔄 Updates
```bash
# Update Go tools
go install -v github.com/projectdiscovery/nuclei/v2/cmd/nuclei@latest

# Update nuclei templates
nuclei -update-templates

# Update system tools
sudo apt update && sudo apt upgrade
```

## 🤝 Support
If you encounter issues:
1. Check if tools are in PATH: `which subfinder`
2. Verify installation: `subfinder -version`
3. Re-run installer: `./install.sh`
4. Check logs in `logs/` directory

## 📝 License
MIT License - Use responsibly and legally

---

**Made with ❤️ for the Security Community**

*Simple. Reliable. Effective.*
