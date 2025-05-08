"""
Run the clipboard monitor
"""
from url_scanner.clipboard import ClipboardMonitor
import time

if __name__ == "__main__":
    monitor = ClipboardMonitor()
    try:
        monitor.start()
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        monitor.stop() 