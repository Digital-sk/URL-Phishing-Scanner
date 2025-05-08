# URL Phishing Scanner
Developed a Python-based phishing URL scanner that analyzes suspicious links using heuristic rules and WHOIS data.

Integrated URL parsing, regular expressions, and domain analysis to flag phishing indicators like suspicious TLDs, subdomains, and IP-based URLs.

Implemented domain age verification using the python-whois library, identifying recently registered domains commonly used in phishing attacks.

Designed a risk scoring system to assess URLs based on multiple red flags and classify them as safe, suspicious, or malicious.

Created a CLI interface for real.
![image](https://github.com/user-attachments/assets/03e742bb-fe09-4def-899e-df3e170980e1)


## 📌 Features
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

🌐 Blacklist Integration Ready
Can be extended to use services like PhishTank, OpenPhish, or Google Safe Browsing API.

📝 Logging Support (Optional)
Scan results can be logged for later analysis or reporting.
![image](https://github.com/user-attachments/assets/d26b0bb4-1ec3-432b-a502-9e58912daf90)
![image](https://github.com/user-attachments/assets/0da832f9-0476-41cf-9f2e-d109f2f9e298)

## Project Structure

```
url_scanner/
├── __init__.py          # Package initialization
├── core.py             # Core scanning functionality
├── web.py              # Web interface
└── clipboard.py        # Clipboard monitoring
```

## Heuristic Analysis Includes

- HTTPS protocol checking
- Suspicious TLD detection
- IP address detection
- Phishing keyword analysis
- Subdomain length analysis
- Special character detection

## Setup

1. Clone this repository
2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Set up your Google Safe Browsing API key:
   - Go to the [Google Cloud Console](https://console.cloud.google.com/)
   - Create a new project or select an existing one
   - Enable the Safe Browsing API
   - Create credentials (API key)
   - Create a `.env` file in the project root and add:
     ```
     GOOGLE_SAFE_BROWSING_API_KEY=your_api_key_here
     ```

4. Run the application:
   ```bash
   # Start the web interface
   python run_web.py
   
   # In a separate terminal, start the clipboard monitor
   python run_clipboard.py
   ```

5. Open your browser and navigate to `http://localhost:5000`

## Usage

### Web Interface
1. Enter a URL in the input field
2. Click "Scan URL"
3. View the results, which include:
   - Risk level assessment
   - Heuristic score
   - Detailed reasons for the assessment
   - Blacklist match status
   - Scan timestamp

### Clipboard Monitor
The clipboard monitor automatically scans URLs when they are copied to the clipboard:
1. Start the clipboard monitor using `python run_clipboard.py`
2. Copy any URL to your clipboard
3. The monitor will automatically:
   - Detect the URL
   - Scan it for phishing risks
   - Display the results in the terminal
4. Press Ctrl+C to stop the monitor

## Extending the Project

The modular architecture makes it easy to extend the project:

1. Add new scanning methods:
   - Create a new class in `core.py` or a new module
   - Implement the scanning interface
   - Add it to the `URLScanner` class

2. Create new interfaces:
   - Add new interface modules (e.g., `api.py` for REST API)
   - Create corresponding entry points
   - Reuse the core scanning functionality

3. Add new features:
   - Browser extension support
   - Additional blacklist sources
   - Custom risk scoring rules
   - Integration with other security tools

## Security Note

This tool is meant to be used as a preliminary check and should not be the only security measure you rely on. Always exercise caution when visiting unknown websites and use additional security measures.

## License

MIT License 
