from flask import Flask, render_template, request, jsonify
import requests
import validators
import tldextract
from bs4 import BeautifulSoup
import re
import json
import os
from datetime import datetime
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

app = Flask(__name__)

# Common phishing keywords
PHISHING_KEYWORDS = [
    'login', 'signin', 'account', 'verify', 'security', 'bank', 'paypal',
    'amazon', 'ebay', 'password', 'confirm', 'update', 'secure', 'alert'
]

# Risk weights for different factors
RISK_WEIGHTS = {
    'no_https': 20,
    'suspicious_tld': 25,
    'ip_address': 30,
    'phishing_keyword': 15,
    'long_subdomain': 10,
    'special_chars': 15,
    'blacklist_match': 40
}

def check_url_blacklist(url):
    """Check if URL is in any known blacklist"""
    try:
        # Using Google Safe Browsing API (you'll need to add your API key)
        api_key = os.getenv('GOOGLE_SAFE_BROWSING_API_KEY')
        if not api_key:
            return False, "API key not configured"
            
        api_url = f"https://safebrowsing.googleapis.com/v4/threatMatches:find?key={api_key}"
        payload = {
            "client": {
                "clientId": "urlscanner",
                "clientVersion": "1.0.0"
            },
            "threatInfo": {
                "threatTypes": ["MALWARE", "SOCIAL_ENGINEERING", "UNWANTED_SOFTWARE", "POTENTIALLY_HARMFUL_APPLICATION"],
                "platformTypes": ["ANY_PLATFORM"],
                "threatEntryTypes": ["URL"],
                "threatEntries": [{"url": url}]
            }
        }
        response = requests.post(api_url, json=payload)
        return response.status_code == 200, response.json() if response.status_code == 200 else None
    except Exception as e:
        return False, str(e)

def analyze_url_heuristics(url):
    """Analyze URL using various heuristics"""
    score = 0
    reasons = []
    
    # Extract domain information
    extracted = tldextract.extract(url)
    domain = f"{extracted.domain}.{extracted.suffix}"
    
    # Check for HTTPS
    if not url.startswith('https://'):
        score += 1
        reasons.append("URL doesn't use HTTPS")
    
    # Check for suspicious TLDs
    suspicious_tlds = ['.xyz', '.tk', '.pw', '.cc', '.top', '.work', '.site']
    if any(tld in url.lower() for tld in suspicious_tlds):
        score += 2
        reasons.append("Suspicious TLD detected")
    
    # Check for IP address instead of domain
    ip_pattern = r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}'
    if re.search(ip_pattern, url):
        score += 2
        reasons.append("URL contains IP address instead of domain")
    
    # Check for phishing keywords in domain
    for keyword in PHISHING_KEYWORDS:
        if keyword in domain.lower():
            score += 1
            reasons.append(f"Suspicious keyword '{keyword}' found in domain")
    
    # Check for subdomain length
    if len(extracted.subdomain) > 20:
        score += 1
        reasons.append("Suspiciously long subdomain")
    
    # Check for special characters
    if re.search(r'[^a-zA-Z0-9\-\.]', domain):
        score += 1
        reasons.append("Domain contains special characters")
    
    return score, reasons

def calculate_phishing_score(heuristic_score, reasons, blacklist_match):
    """Calculate phishing risk score (0-100)"""
    base_score = 0
    
    # Add scores based on reasons
    for reason in reasons:
        if "doesn't use HTTPS" in reason:
            base_score += RISK_WEIGHTS['no_https']
        elif "Suspicious TLD" in reason:
            base_score += RISK_WEIGHTS['suspicious_tld']
        elif "IP address" in reason:
            base_score += RISK_WEIGHTS['ip_address']
        elif "Suspicious keyword" in reason:
            base_score += RISK_WEIGHTS['phishing_keyword']
        elif "long subdomain" in reason:
            base_score += RISK_WEIGHTS['long_subdomain']
        elif "special characters" in reason:
            base_score += RISK_WEIGHTS['special_chars']
    
    # Add blacklist match score
    if blacklist_match:
        base_score += RISK_WEIGHTS['blacklist_match']
    
    # Ensure score is between 0 and 100
    return min(100, base_score)

def get_risk_level(score):
    """Determine risk level based on score"""
    if score <= 30:
        return "Safe"
    elif score <= 60:
        return "Suspicious"
    else:
        return "Likely Phishing"

def scan_url(url):
    """Main function to scan a URL"""
    if not validators.url(url):
        return {
            'is_valid': False,
            'error': 'Invalid URL format'
        }
    
    try:
        # Check blacklist
        blacklist_result, blacklist_data = check_url_blacklist(url)
        
        # Analyze heuristics
        heuristic_score, reasons = analyze_url_heuristics(url)
        
        # Calculate phishing score
        phishing_score = calculate_phishing_score(heuristic_score, reasons, blacklist_result)
        
        # Determine risk level
        risk_level = get_risk_level(phishing_score)
        
        return {
            'is_valid': True,
            'url': url,
            'scan_time': datetime.now().isoformat(),
            'risk_level': risk_level,
            'phishing_score': phishing_score,
            'heuristic_score': heuristic_score,
            'blacklist_match': blacklist_result,
            'reasons': reasons,
            'blacklist_data': blacklist_data
        }
    except Exception as e:
        return {
            'is_valid': False,
            'error': str(e)
        }

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/scan', methods=['POST'])
def scan():
    url = request.json.get('url', '')
    result = scan_url(url)
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True) 