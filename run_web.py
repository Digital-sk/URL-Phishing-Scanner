"""
Run the web interface
"""
from url_scanner.web import create_app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True) 