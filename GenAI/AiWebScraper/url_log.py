import os
import csv
from datetime import datetime

# Define log file location
LOG_FILE = os.path.join(os.path.dirname(__file__), 'logs', 'urls_log.csv')

# Create the logs directory if it doesn't exist
os.makedirs(os.path.dirname(LOG_FILE), exist_ok=True)

# Store visited URLs to avoid duplicates
visited_urls = set()

def log_url(url):
    if url not in visited_urls:
        visited_urls.add(url)
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        # Open the log file and write the URL with timestamp
        with open(LOG_FILE, mode='a', newline='') as file:
            writer = csv.writer(file)
            
            # Write header if the file is empty
            if file.tell() == 0:
                writer.writerow(['Timestamp', 'URL'])
                
            writer.writerow([timestamp, url])
            
        print(f"Logged URL: {url}")
