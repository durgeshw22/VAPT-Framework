# QUICK START GUIDE

## ⚡ 3-Step Installation (Kali Linux)

```bash
# Step 1: Navigate to framework directory
cd reconvapt

# Step 2: Run installer
chmod +x install.sh
./install.sh

# Step 3: Reload shell and verify
source ~/.bashrc
chmod +x verify_install.sh
./verify_install.sh
```

## 🎯 First Run

```bash
# Start the framework
python3 reconvapt.py

# You'll see the main menu:
[1] Subdomain Enumeration
[2] Directory/File Discovery
[3] Port Scanning
[4] Screenshot Capture
[5] Vulnerability Scanning
[6] Parameter Discovery
[7] JavaScript Discovery
[8] Technology Detection
[0] Exit
```

## 📝 Example Usage Scenarios

### Scenario 1: Basic Domain Reconnaissance
```
1. python3 reconvapt.py
2. Choose [1] Subdomain Enumeration
3. Select [5] Run All Tools
4. Enter: example.com
5. Results: output/example.com_timestamp/
```

### Scenario 2: Web Application Testing
```
1. Start with directory discovery
   - Choose [2] Directory/File Discovery
   - Select [1] ffuf
   - Enter: http://example.com
   
2. Then scan for vulnerabilities
   - Choose [5] Vulnerability Scanning
   - Select [1] nuclei
   - Enter: http://example.com
```

### Scenario 3: Network Assessment
```
1. Port scan first
   - Choose [3] Port Scanning
   - Select [1] nmap
   - Enter: example.com or 192.168.1.1
   
2. Capture screenshots
   - Choose [4] Screenshot Capture
   - Select [1] gowitness
   - Enter URLs found from port scan
```

## 🔍 Where to Find Results

All results are saved in timestamped directories:
```
reconvapt/output/
├── example.com_20241028_123456/
│   ├── subfinder_results.txt
│   ├── assetfinder_results.txt
│   ├── httpx_results.txt
│   └── combined_results.txt
└── dir_example.com_20241028_234567/
    └── ffuf_results.txt
```

## 🛠️ Common Commands

```bash
# Check if tools are installed
which subfinder httpx nmap

# Update nuclei templates
nuclei -update-templates

# Re-run installer if needed
./install.sh

# Check installation
./verify_install.sh

# View logs
tail -f logs/reconvapt_*.log
```

## ⚠️ Troubleshooting Quick Fixes

### "Command not found" for Go tools
```bash
export PATH=$PATH:~/go/bin
source ~/.bashrc
```

### "No module named 'colorama'"
```bash
pip3 install colorama requests
```

### Permission errors
```bash
chmod +x reconvapt.py install.sh verify_install.sh
```

## 🎓 Recommended Learning Path

**Day 1: Passive Reconnaissance**
- Module 1: Subdomain Enumeration
- Module 7: JavaScript Discovery
- Module 8: Technology Detection

**Day 2: Active Scanning**
- Module 2: Directory Discovery
- Module 3: Port Scanning
- Module 4: Screenshot Capture

**Day 3: Vulnerability Assessment**
- Module 5: Vulnerability Scanning
- Module 6: Parameter Discovery

## 💡 Pro Tips

1. **Always start passive**: Use subfinder before aggressive tools
2. **Validate findings**: Use httpx to check if subdomains are live
3. **Use wordlists wisely**: Start with common.txt, escalate if needed
4. **Combine modules**: Subdomain enum → Port scan → Screenshots
5. **Check output regularly**: Results auto-save, check while scanning
6. **Legal authorization**: Only test domains you own or have permission

## 📱 Tool Selection Cheat Sheet

**Fast Results?**
- Subdomains: subfinder
- Directories: ffuf
- Ports: naabu
- Screenshots: gowitness

**Comprehensive Results?**
- Subdomains: Run all tools (option 5)
- Directories: gobuster
- Ports: nmap
- Vulnerabilities: nuclei

**Specific Needs?**
- SQL injection: sqlmap
- Web server issues: nikto
- Hidden parameters: arjun
- Technology stack: whatweb

## 🔄 Regular Maintenance

```bash
# Weekly: Update nuclei templates
nuclei -update-templates

# Monthly: Update Go tools
go install -v github.com/projectdiscovery/nuclei/v2/cmd/nuclei@latest
go install -v github.com/projectdiscovery/httpx/cmd/httpx@latest
go install -v github.com/projectdiscovery/subfinder/v2/cmd/subfinder@latest

# As needed: Update system tools
sudo apt update && sudo apt upgrade nmap nikto sqlmap
```

## 🎯 Next Steps After Installation

1. ✅ Run `./verify_install.sh` - Ensure all tools installed
2. ✅ Test with a safe domain you own
3. ✅ Explore each module one by one
4. ✅ Check output directory structure
5. ✅ Read full README.md for detailed info

---

**Need help?** Check the main README.md or logs/ directory

**Ready to start?** Run: `python3 reconvapt.py`
