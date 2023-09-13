# Forty bt croc100

import requests

# Enter your API key obtained from the Google Developers Console
api_key = 'YOUR_API_KEY'

# Enter your Google Custom Search Engine (CSE) ID
cse_id = 'YOUR_CSE_ID'

# Enter the country code (e.g., 'us' for the United States, 'kr' for South Korea)
country_code = 'us'  # Set the country code here

# Google Custom Search JSON API endpoint URL
url = 'https://www.googleapis.com/customsearch/v1'

# Function to get real-time popular keywords
def get_realtime_popular_keywords():
    params = {
        'key': api_key,
        'cx': cse_id,
        'q': '',  # Leave the query empty to get real-time popular keywords
        'num': 10,  # Get the top 10 keywords
        'gl': country_code,  # Set the country code
    }
    
    response = requests.get(url, params=params)
    
    if response.status_code == 200:
        data = response.json()
        items = data.get('items', [])
        for rank, item in enumerate(items, start=1):
            title = item.get('title', '')
            print(f"{rank}. {title}")
    else:
        print("API request failed")

if __name__ == '__main__':
    get_realtime_popular_keywords()
