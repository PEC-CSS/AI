import os
import csv
from datetime import datetime


LOG_FILE = os.path.join(os.path.dirname(__file__), 'logs', 'urls_log.csv')

os.makedirs(os.path.dirname(LOG_FILE), exist_ok=True)


visited_urls = set()

def log_url(url):
    
    if url not in visited_urls:
        
        visited_urls.add(url)
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        
        with open(LOG_FILE, mode='a', newline='') as file:
            writer = csv.writer(file)
            
            if file.tell() == 0:
                writer.writerow(['Timestamp', 'URL'])
                
            writer.writerow([timestamp, url])
            
        print(f"Logged URL: {url}")





if __name__ == "__main__":
    log_url(url)
