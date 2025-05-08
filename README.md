# URL Phishing Scanner

A modular and extensible tool for detecting malicious URLs using both blacklist checking and heuristic analysis.

## Features

- URL validation and formatting
- Blacklist checking using Google Safe Browsing API
- Heuristic analysis for phishing detection
- Modern, responsive web interface
- Real-time scanning results
- Clipboard monitoring for automatic URL scanning
- Modular and extensible architecture

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