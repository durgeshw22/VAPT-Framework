# ✅ DEPLOYMENT CHECKLIST

## Pre-Transfer Checklist (Windows)

- [ ] All files created in `C:\Users\sonali\OneDrive\Desktop\reconvapt\`
- [ ] Verify folder structure exists:
  - [ ] `modules/` directory with 9 Python files
  - [ ] `utils/` directory with 4 Python files
  - [ ] Root directory with main files
- [ ] Check file count: Should have 22 files total
- [ ] Review README.md for completeness
- [ ] Verify install.sh has proper line endings (will handle on Kali)

---

## Transfer to Kali Linux

### Option 1: USB Drive
```bash
# On Windows:
# Copy entire 'reconvapt' folder to USB drive

# On Kali Linux:
cp -r /media/usb/reconvapt ~/
cd ~/reconvapt
```

### Option 2: Git (if using version control)
```bash
# On Windows:
cd C:\Users\sonali\OneDrive\Desktop\reconvapt
git init
git add .
git commit -m "Initial RECON VAPT Framework"
git push

# On Kali Linux:
git clone <your-repo-url>
cd reconvapt
```

### Option 3: SCP/SFTP
```bash
# From Windows to Kali:
scp -r C:\Users\sonali\OneDrive\Desktop\reconvapt user@kali-ip:~/
```

### Option 4: Shared Network Folder
```bash
# Access shared folder from Kali and copy
cp -r /mnt/share/reconvapt ~/
```

---

## Post-Transfer Checklist (Kali Linux)

### Step 1: Verify Transfer
- [ ] All 22 files transferred successfully
- [ ] Directory structure intact
- [ ] Check file permissions

```bash
cd ~/reconvapt
ls -la
tree  # if tree is installed
```

### Step 2: Fix Line Endings (Important!)
```bash
# Install dos2unix if not present
sudo apt install dos2unix -y

# Convert line endings for shell scripts
dos2unix install.sh
dos2unix verify_install.sh

# Make scripts executable
chmod +x install.sh
chmod +x verify_install.sh
chmod +x reconvapt.py
chmod +x test_framework.py
```

### Step 3: Run Installation
- [ ] Execute installer: `./install.sh`
- [ ] Wait for completion (10-15 minutes)
- [ ] Check for any errors during installation
- [ ] Reload shell: `source ~/.bashrc`

### Step 4: Verify Installation
- [ ] Run verification: `./verify_install.sh`
- [ ] All 19 checks should pass
- [ ] Check output shows green checkmarks

Expected output:
```
Total Checks:    19
Installed:       19
Missing:         0

✓ All tools installed successfully!
```

### Step 5: Test Framework
- [ ] Run test script: `python3 test_framework.py`
- [ ] All 8 tests should pass
- [ ] Banner displays correctly

Expected output:
```
✓ ALL TESTS PASSED!
```

### Step 6: First Run
- [ ] Start framework: `python3 reconvapt.py`
- [ ] Main menu displays with all 8 modules
- [ ] Test Module 1 (Subdomain Enumeration)
- [ ] Choose option 1 (subfinder)
- [ ] Test with a safe domain you own
- [ ] Check output directory for results

---

## Troubleshooting Checklist

### If "Command not found" for Go tools:
- [ ] Check PATH: `echo $PATH | grep go/bin`
- [ ] Add to PATH: `export PATH=$PATH:~/go/bin`
- [ ] Make permanent: `echo 'export PATH=$PATH:~/go/bin' >> ~/.bashrc`
- [ ] Reload: `source ~/.bashrc`
- [ ] Verify: `which subfinder httpx nuclei`

### If Python import errors:
- [ ] Install dependencies: `pip3 install colorama requests`
- [ ] Check installation: `pip3 list | grep colorama`
- [ ] Verify Python version: `python3 --version` (should be 3.6+)

### If install.sh fails:
- [ ] Check internet connection
- [ ] Run with sudo: `sudo ./install.sh`
- [ ] Check disk space: `df -h`
- [ ] Review error messages
- [ ] Try manual installation (see INSTALLATION.md)

### If permission denied:
- [ ] Fix script permissions: `chmod +x *.sh *.py`
- [ ] Fix directory permissions: `chmod -R 755 ~/reconvapt`

---

## Validation Checklist

### Tool Availability Test
Run these commands to verify each tool:

```bash
# Go-based tools
subfinder -version
assetfinder -h
httpx -version
ffuf -V
gobuster version
naabu -version
gowitness version
aquatone -version
nuclei -version

# System tools
nmap --version
masscan --version
nikto -Version
sqlmap --version
dirb
whatweb --version

# Python tools
arjun -h
```

- [ ] All commands execute without "command not found"
- [ ] Version numbers display correctly

### Framework Module Test
- [ ] Module 1: Subdomain Enumeration works
- [ ] Module 2: Directory Discovery works
- [ ] Module 3: Port Scanning works
- [ ] Module 4: Screenshot Capture works
- [ ] Module 5: Vulnerability Scanning works
- [ ] Module 6: Parameter Discovery works
- [ ] Module 7: JavaScript Discovery works
- [ ] Module 8: Technology Detection works

### Output Directory Test
- [ ] `output/` directory created automatically
- [ ] Scan results save with timestamps
- [ ] Results are readable
- [ ] Logs directory created
- [ ] Log files generated

---

## Safety Checklist

### Before Running Any Scans:
- [ ] **Have written authorization** to test target
- [ ] Using own domain or authorized test target
- [ ] Understand legal implications
- [ ] Not testing production systems without approval
- [ ] Rate limiting configured appropriately

### Recommended First Test:
- [ ] Use your own domain
- [ ] Start with passive tools (subfinder)
- [ ] Verify results make sense
- [ ] Check tool output format
- [ ] Ensure no errors in logs

---

## Optimization Checklist

### After Successful Installation:
- [ ] Update nuclei templates: `nuclei -update-templates`
- [ ] Download common wordlists:
  ```bash
  sudo apt install seclists -y
  # Wordlists in /usr/share/seclists/
  ```
- [ ] Configure favorite wordlists in `wordlists/` folder
- [ ] Bookmark important documentation files

### Optional Enhancements:
- [ ] Create desktop shortcut
- [ ] Add alias: `alias recon='cd ~/reconvapt && python3 reconvapt.py'`
- [ ] Set up automated backups for results
- [ ] Configure log rotation

---

## Documentation Review Checklist

- [ ] Read README.md (complete overview)
- [ ] Read QUICKSTART.md (quick reference)
- [ ] Read INSTALLATION.md (detailed install guide)
- [ ] Bookmark PROJECT_FILES.md (file reference)
- [ ] Keep this checklist for future reference

---

## Final Validation

### Everything Working?
- [ ] Framework starts without errors
- [ ] All 8 modules accessible
- [ ] At least 1 successful scan completed
- [ ] Results saved in output directory
- [ ] Logs being generated
- [ ] No critical errors in logs

### If ALL checkboxes above are checked:
```
🎉 CONGRATULATIONS! 🎉
RECON VAPT Framework is fully deployed and ready to use!
```

### Next Steps:
1. Read tool documentation for advanced usage
2. Practice with safe, authorized targets
3. Explore different module combinations
4. Save frequently used commands
5. Keep tools updated regularly

---

## Maintenance Schedule

### Weekly:
- [ ] Update nuclei templates: `nuclei -update-templates`
- [ ] Clean old results: `rm -rf output/old_scans/`

### Monthly:
- [ ] Update Go tools: `go install -v github.com/projectdiscovery/nuclei/v2/cmd/nuclei@latest`
- [ ] Update system tools: `sudo apt update && sudo apt upgrade`
- [ ] Review and archive old logs

### As Needed:
- [ ] Install new wordlists
- [ ] Update framework if new version released
- [ ] Backup important results

---

## Support Resources

- **Documentation**: Check README.md, QUICKSTART.md, INSTALLATION.md
- **Logs**: Review `logs/reconvapt_*.log` for errors
- **Verification**: Re-run `./verify_install.sh`
- **Test**: Re-run `python3 test_framework.py`
- **Reinstall**: Safe to run `./install.sh` again

---

**Created**: 2024
**Framework Version**: 2.0
**Status**: Ready for Deployment ✅

Good luck with your penetration testing! 🔒🔍
