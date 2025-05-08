# URL-Phishing-Scanner
Developed a Python-based phishing URL scanner that analyzes suspicious links using heuristic rules and WHOIS data.
!![image](https://github.com/user-attachments/assets/a56aab02-9566-41d0-bf25-51ed1cdbd534)
# 📌 Features
🧠 Heuristic-Based URL Analysis
Detects phishing traits such as use of IP addresses, suspicious TLDs (e.g., .tk, .xyz), long/obfuscated URLs, and phishing-related keywords.

🔍 Domain Age Detection via WHOIS
Flags newly registered domains commonly used in phishing attacks.

⚠️ Phishing Risk Scoring System
Calculates a risk score based on red flags and categorizes URLs as Safe, Suspicious, or Malicious.

📋 Clipboard Monitoring (Real-Time Detection)
Automatically scans any copied URL from the clipboard to catch threats before the user clicks.

🛠️ Command-Line Interface (CLI)
Lightweight CLI for quick scanning of URLs with clean output and flag descriptions.

📁 Modular & Extensible Codebase
Designed for easy integration with future features like API checks, GUI, or browser extensions.


# ⚙️ How It Works
Clipboard Monitoring
The program continuously monitors the system clipboard for copied URLs. As soon as a URL is copied, the scanner automatically checks it for potential phishing indicators, such as suspicious TLDs or excessive length.

Phishing Risk Scoring
The scanner assigns a phishing risk score based on multiple heuristic rules:

Suspicious Top-Level Domains (TLDs) like .tk, .xyz, etc.

Length of the URL (longer URLs are often more suspicious).

Common phishing-related keywords (e.g., login, secure, verify).

Domain characteristics such as the number of subdomains or IP-based URLs.

Newly registered domains, which are more likely to be used in phishing campaigns.

URL Classification
Based on the calculated score, the program classifies the URL into one of three categories:

Safe: The URL passes all checks and is deemed trustworthy.

Suspicious: The URL contains some indicators of phishing but isn't fully dangerous.

Malicious: The URL shows strong signs of phishing and should be avoided.

User Feedback
If a URL is flagged as suspicious or malicious, the program provides immediate feedback to the user, displaying relevant red flags and risk factors for better awareness.

!![image](https://github.com/user-attachments/assets/e1ebbbd5-b3fe-4088-be88-c0245cc97c1f)
!![image](https://github.com/user-attachments/assets/d4b3e946-0db5-4e20-86f3-b3a1e695c79a)

# 🚀 How to Use
Clone the Repository

First, clone the repository to your local machine:

bash
Copy
Edit
git clone https://github.com/yourusername/phishing-risk-scanner.git
cd phishing-risk-scanner
Install Dependencies

Install the necessary libraries:

bash
Copy
Edit
pip install -r requirements.txt
Alternatively, you can manually install the required dependencies:

bash
Copy
Edit
pip install pyperclip
Run the Clipboard Monitor Script

To start the clipboard monitoring feature, run the following command:

bash
Copy
Edit
python phishing_scanner.py
The program will continuously monitor your clipboard for URLs. Whenever a URL is copied, it will be checked for phishing risks, and a report will be displayed in the terminal with the results.

View Phishing Risk Report

The scanner will output one of the following for each copied URL:

Safe: No phishing indicators detected.

Suspicious: Some suspicious characteristics detected (e.g., odd TLD or keyword).

Malicious: Strong indications of phishing.
