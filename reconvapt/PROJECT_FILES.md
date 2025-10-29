# 📁 RECON VAPT Framework - Project Files

## Complete File Structure

```
reconvapt/
│
├── 📄 reconvapt.py                    # Main application entry point
├── 📄 requirements.txt                # Python dependencies
├── 📄 install.sh                      # Automated installer (Linux)
├── 📄 verify_install.sh               # Installation verification script
├── 📄 test_framework.py               # Framework functionality test
│
├── 📚 Documentation
│   ├── README.md                      # Complete documentation
│   ├── QUICKSTART.md                  # Quick start guide
│   ├── INSTALLATION.md                # Detailed installation guide
│   └── PROJECT_FILES.md               # This file
│
├── 📁 modules/                        # Security testing modules
│   ├── __init__.py
│   ├── subdomain_enum.py              # Module 1: Subdomain enumeration
│   ├── directory_discovery.py         # Module 2: Directory/file discovery
│   ├── port_scanning.py               # Module 3: Port scanning
│   ├── screenshot_capture.py          # Module 4: Screenshot capture
│   ├── vulnerability_scanning.py      # Module 5: Vulnerability scanning
│   ├── parameter_discovery.py         # Module 6: Parameter discovery
│   ├── javascript_discovery.py        # Module 7: JavaScript discovery
│   └── technology_detection.py        # Module 8: Technology detection
│
├── 📁 utils/                          # Utility functions
│   ├── __init__.py
│   ├── banner.py                      # ASCII banner display
│   ├── logger.py                      # Logging configuration
│   └── helpers.py                     # Helper functions
│
├── 📁 output/                         # Scan results (auto-created)
│   └── (timestamped directories)
│
├── 📁 logs/                           # Application logs (auto-created)
│   └── reconvapt_YYYYMMDD_HHMMSS.log
│
└── 📁 wordlists/                      # Custom wordlists (optional)
    └── (user wordlists)
```

---

## File Descriptions

### Core Files

#### `reconvapt.py` (Main Application)
- **Size**: ~3KB
- **Purpose**: Main entry point for the framework
- **Features**:
  - Interactive CLI menu system
  - Module selection and routing
  - Colored terminal output
  - Error handling and logging
  - Directory initialization
- **Usage**: `python3 reconvapt.py`

#### `requirements.txt`
- **Size**: <1KB
- **Purpose**: Python package dependencies
- **Contents**:
  ```
  colorama
  requests
  ```
- **Usage**: `pip3 install -r requirements.txt`

#### `install.sh`
- **Size**: ~3KB
- **Purpose**: Automated installation script
- **Features**:
  - System package updates
  - Python dependency installation
  - Go environment setup
  - Tool installation (21 tools)
  - Permission configuration
- **Usage**: `./install.sh`
- **Execution Time**: 10-15 minutes

#### `verify_install.sh`
- **Size**: ~2KB
- **Purpose**: Verify all tools are installed correctly
- **Checks**:
  - 9 Go-based tools
  - 5 system tools
  - 1 Python tool
  - 2 Python modules
  - Environment configuration
- **Usage**: `./verify_install.sh`

#### `test_framework.py`
- **Size**: ~2KB
- **Purpose**: Test framework functionality
- **Tests**:
  - Module imports
  - Utility functions
  - Logger initialization
  - Banner display
  - Directory creation
  - Python version compatibility
- **Usage**: `python3 test_framework.py`

---

### Module Files

#### `modules/subdomain_enum.py`
- **Size**: ~4KB
- **Tools**: subfinder, assetfinder, httpx, crt.sh
- **Features**:
  - Passive subdomain discovery
  - Live subdomain validation
  - Certificate transparency search
  - Result deduplication
  - "Run all tools" option

#### `modules/directory_discovery.py`
- **Size**: ~3.5KB
- **Tools**: ffuf, gobuster, dirb
- **Features**:
  - Wordlist selection menu
  - Fast fuzzing capabilities
  - Brute-force directory discovery
  - 30-minute timeout protection

#### `modules/port_scanning.py`
- **Size**: ~3.5KB
- **Tools**: nmap, naabu, masscan
- **Features**:
  - Comprehensive port scanning
  - Fast SYN scanning
  - High-speed scanning
  - Service detection
  - 60-minute timeout

#### `modules/screenshot_capture.py`
- **Size**: ~2.5KB
- **Tools**: gowitness, aquatone
- **Features**:
  - Single URL screenshots
  - Bulk screenshot capture
  - HTML report generation
  - Automatic directory creation

#### `modules/vulnerability_scanning.py`
- **Size**: ~3KB
- **Tools**: nuclei, nikto, sqlmap
- **Features**:
  - Template-based scanning
  - Web server vulnerability detection
  - SQL injection testing
  - Automated template updates

#### `modules/parameter_discovery.py`
- **Size**: ~2.5KB
- **Tools**: arjun, ffuf
- **Features**:
  - Hidden parameter discovery
  - GET/POST parameter fuzzing
  - Custom wordlist support
  - 15-minute timeout

#### `modules/javascript_discovery.py`
- **Size**: ~2.5KB
- **Tools**: linkfinder, httpx
- **Features**:
  - JavaScript file discovery
  - Endpoint extraction
  - API discovery
  - Pattern matching

#### `modules/technology_detection.py`
- **Size**: ~2.5KB
- **Tools**: httpx, whatweb
- **Features**:
  - Technology fingerprinting
  - Framework detection
  - Version identification
  - Live result preview

---

### Utility Files

#### `utils/banner.py`
- **Size**: ~1KB
- **Purpose**: Display ASCII art banner
- **Features**:
  - Colored ASCII art
  - Framework version display
  - Module count information

#### `utils/logger.py`
- **Size**: ~1KB
- **Purpose**: Logging configuration
- **Features**:
  - Timestamped log files
  - Console and file logging
  - Automatic log directory creation
  - Formatted log messages

#### `utils/helpers.py`
- **Size**: ~3KB
- **Purpose**: Helper functions
- **Functions**:
  - `validate_domain()` - Domain validation
  - `validate_url()` - URL validation
  - `validate_ip()` - IP address validation
  - `create_output_dir()` - Create timestamped directories
  - `check_tool_installed()` - Verify tool availability
  - `run_command()` - Execute subprocess commands
  - `count_lines()` - Count file lines
  - `read_file_lines()` - Read file content

---

### Documentation Files

#### `README.md`
- **Size**: ~8KB
- **Purpose**: Complete framework documentation
- **Sections**:
  - Overview and features
  - Module and tool descriptions
  - Installation instructions
  - Usage examples
  - Troubleshooting guide
  - Best practices
  - System requirements

#### `QUICKSTART.md`
- **Size**: ~4KB
- **Purpose**: Quick reference guide
- **Sections**:
  - 3-step installation
  - First run guide
  - Example scenarios
  - Result locations
  - Common commands
  - Troubleshooting quick fixes
  - Tool selection cheat sheet

#### `INSTALLATION.md`
- **Size**: ~6KB
- **Purpose**: Detailed installation guide
- **Sections**:
  - Prerequisites
  - Automated installation
  - Manual installation
  - Troubleshooting (6 common issues)
  - Post-installation checklist
  - Update procedures
  - System requirements

#### `PROJECT_FILES.md`
- **Size**: ~3KB
- **Purpose**: File structure reference
- **Sections**:
  - Complete file tree
  - File descriptions
  - Quick reference
  - Transfer instructions

---

## Quick Reference

### Total Files Created
- **Core Files**: 5
- **Module Files**: 9 (includes __init__.py)
- **Utility Files**: 4 (includes __init__.py)
- **Documentation Files**: 4
- **Total**: 22 files

### Total Lines of Code
- **Python Code**: ~1,200 lines
- **Shell Scripts**: ~200 lines
- **Documentation**: ~1,000 lines
- **Total**: ~2,400 lines

### Framework Statistics
- **Modules**: 8
- **Tools**: 21
- **Go-based tools**: 9
- **System tools**: 5
- **Python tools**: 1
- **API-based tools**: 1 (crt.sh)

---

## Files to Transfer to Kali Linux

### Method 1: Direct Copy
Copy the entire `reconvapt` folder to your Kali Linux machine

### Method 2: Individual Files
If copying individually, ensure you maintain the directory structure:

**Essential Files** (must have):
```
reconvapt.py
requirements.txt
install.sh
verify_install.sh
modules/*.py (all 9 files)
utils/*.py (all 4 files)
```

**Optional Files** (recommended):
```
test_framework.py
README.md
QUICKSTART.md
INSTALLATION.md
```

---

## After Transfer to Kali Linux

```bash
# 1. Navigate to directory
cd reconvapt

# 2. Make scripts executable
chmod +x install.sh verify_install.sh reconvapt.py test_framework.py

# 3. Run installer
./install.sh

# 4. Reload shell
source ~/.bashrc

# 5. Verify installation
./verify_install.sh

# 6. Test framework
python3 test_framework.py

# 7. Start using
python3 reconvapt.py
```

---

## Version Information

- **Framework Version**: 2.0
- **Created**: 2024
- **Python**: 3.6+
- **Platform**: Kali Linux
- **Architecture**: Modular CLI

---

**Ready to transfer and install!** 🚀

All files are complete and ready to use on Kali Linux.
