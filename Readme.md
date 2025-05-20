# 🛡️ Simple File Integrity Checker

This is a basic file integrity checker script that uses **hashes** to detect changes in a file. It periodically calculates the file's hash and compares it with the previously saved hash. If it detects any changes, it throws an alert!

---

## ⚠️ **Ethical Considerations**
This project is for **educational purposes only**.  
Do **NOT** use this script to monitor files you don't own or don't have permission to track. Always respect privacy and adhere to legal guidelines.  

---

## 💻 **Setup Instructions**

### Clone the Repository  
```bash
git clone https://github.com/Saahil-gupta/file-integrity-checker.git
cd simple-file-integrity-checker
```

### Run the Script
```bash
python file_checker.py
```

### Stopping the Checker
Press Ctrl+C in the terminal to stop it

### How it Works
1. Calculates the SHA-256 hash of the specified file.
2. Saves the hash in a text file (file_hash.txt).
3. Periodically checks the file for changes (every 100 seconds by default).
4. Alerts if the current hash doesn't match the saved hash.
5. Updates the saved hash after detecting a change.

### 🌟 Customization
1. File to Monitor:
Change the file_path variable in the script to monitor a different file.

2. Check Interval:
Modify the interval variable to set how often it checks for changes.

3. Hash Type:
You can switch from SHA-256 to another hash algorithm (like MD5) by editing the calculate_hash() function:
```bash
sha256_hash = hashlib.md5()
```

4. Log Formatting:
Customize the alert message or log format by editing the print statements.


### 📜 Disclaimer
This project is intended for personal and educational purposes only.
Monitoring files you do not own or have explicit permission to track is illegal and unethical.
Please use responsibly and only for legitimate purposes.