import subprocess
import logging
import time
from datetime import datetime

# Configure logging
logging.basicConfig(filename='clouddash.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

def check_for_updates():
    """Checks for available Windows updates"""
    try:
        logging.info("Checking for updates...")
        result = subprocess.run(['powershell', '-Command', 'Get-WindowsUpdate'], capture_output=True, text=True)
        logging.info(f"Updates check completed: {result.stdout}")
        return result.stdout
    except Exception as e:
        logging.error(f"Error checking for updates: {e}")
        return None

def apply_updates():
    """Applies available Windows updates"""
    try:
        logging.info("Applying updates...")
        result = subprocess.run(['powershell', '-Command', 'Install-WindowsUpdate', '-AcceptAll', '-AutoReboot'], capture_output=True, text=True)
        logging.info(f"Updates application completed: {result.stdout}")
        return result.stdout
    except Exception as e:
        logging.error(f"Error applying updates: {e}")
        return None

def main():
    logging.info("CloudDash started.")
    while True:
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        logging.info(f"Checking for updates at {current_time}")
        updates = check_for_updates()
        if updates:
            apply_updates()
        else:
            logging.info("No updates available.")
        
        # Wait for 24 hours before checking again
        logging.info("Sleeping for 24 hours before next check.")
        time.sleep(86400)

if __name__ == "__main__":
    main()