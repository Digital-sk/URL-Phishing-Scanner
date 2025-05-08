import pyperclip
import time
import threading
import requests
import json
from urllib.parse import urlparse

class ClipboardMonitor:
    def __init__(self, api_url="http://localhost:5000/scan"):
        self.api_url = api_url
        self.last_clipboard = ""
        self.is_running = False
        self.thread = None

    def is_valid_url(self, text):
        """Check if the clipboard text is a valid URL"""
        try:
            result = urlparse(text)
            return all([result.scheme, result.netloc])
        except:
            return False

    def scan_url(self, url):
        """Send URL to the scanner API"""
        try:
            response = requests.post(
                self.api_url,
                json={"url": url},
                headers={"Content-Type": "application/json"}
            )
            return response.json()
        except Exception as e:
            print(f"Error scanning URL: {str(e)}")
            return None

    def monitor_clipboard(self):
        """Monitor clipboard for URLs"""
        while self.is_running:
            try:
                current_clipboard = pyperclip.paste()
                
                # Check if clipboard content has changed and is a valid URL
                if (current_clipboard != self.last_clipboard and 
                    self.is_valid_url(current_clipboard)):
                    
                    print(f"\nURL detected in clipboard: {current_clipboard}")
                    result = self.scan_url(current_clipboard)
                    
                    if result and result.get('is_valid'):
                        score = result.get('phishing_score', 0)
                        risk_level = result.get('risk_level', 'Unknown')
                        reasons = result.get('reasons', [])
                        
                        print("\nScan Results:")
                        print(f"Risk Level: {risk_level}")
                        print(f"Phishing Score: {score}/100")
                        if reasons:
                            print("\nRisk Factors:")
                            for reason in reasons:
                                print(f"- {reason}")
                    else:
                        print("Invalid URL or scanning error")
                    
                    self.last_clipboard = current_clipboard
                
                time.sleep(1)  # Check every second
            except Exception as e:
                print(f"Error monitoring clipboard: {str(e)}")
                time.sleep(1)

    def start(self):
        """Start the clipboard monitor"""
        if not self.is_running:
            self.is_running = True
            self.thread = threading.Thread(target=self.monitor_clipboard)
            self.thread.daemon = True
            self.thread.start()
            print("Clipboard monitor started. Press Ctrl+C to stop.")

    def stop(self):
        """Stop the clipboard monitor"""
        self.is_running = False
        if self.thread:
            self.thread.join()
            print("Clipboard monitor stopped.")

if __name__ == "__main__":
    monitor = ClipboardMonitor()
    try:
        monitor.start()
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        monitor.stop() 