# TASK -1 

# Fetching the ids
import requests
import time

Base_URL = "https://hacker-news.firebaseio.com/"

headers = {"User-Agent": "TrendPulse/1.0"}


try:

    response = requests.get(f'{Base_URL}v0/topstories.json')
    
    response.raise_for_status()
    ids = response.json()[0:500]

except Exception as e :
    print("Error in fetching top stories : ",e)


# setting up categories 
from datetime import datetime
categories = {
    "technology": ["ai", "software", "tech", "code", "computer", "data", "cloud", "api", "gpu", "llm"],
    "worldnews": ["war", "government", "country", "president", "election", "climate", "attack", "global"],
    "sports": ["nfl", "nba", "fifa", "sport", "game", "team", "player", "league", "championship"],
    "science": ["research", "study", "space", "physics", "biology", "discovery", "nasa", "genome"],
    "entertainment": ["movie", "film", "music", "netflix", "game", "book", "show", "award", "streaming"]
}

# Defining a function to check the terms in the title

def check_category(title):
    title = title.lower()

    for category,words in categories.items():
        for word in words:
            if word in title:
                return category
    return 'other category'

# Creating a empty list 
result = []

# story details
# here we created a second dict with intial key values 0
category_counts = dict.fromkeys(categories,0)

for id in ids:
        
    try:
        response1 = requests.get(f'https://hacker-news.firebaseio.com/v0/item/{id}.json', headers = headers)
        response1.raise_for_status()
        data = response1.json()

        if data and 'title' in data:

            title = data['title']
            detected_category = check_category(title)

            if detected_category in category_counts and category_counts[detected_category] <25:

    
            

                result.append({
                    'post_id' : data.get('id'),
                    'title'   : title,
                    'categogy' : detected_category,
                    'score' : data.get('score',0),
                    'num_comments' : data.get('descendants',0),
                    'author'   : data.get('by'),
                    "collected_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    })

                category_counts[detected_category] += 1

    except Exception as e: 
        print(f'Failed for{id}')
        print(e)

    # for each category we are delaying for 2 seconds
time.sleep(2)


# 3 - showing the details of the collected data
import os
import json
from datetime import datetime

# Create folder named 'data'
os.makedirs("data", exist_ok=True)

# File name with date
filename = f"data/trends_{datetime.now().strftime('%Y%m%d')}.json"

# Save file
with open(filename, "w") as f:
    json.dump(result, f, indent=4)

# Print output
print(f"Collected {len(result)} stories. Saved to {filename}")