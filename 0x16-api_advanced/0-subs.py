#!/usr/bin/python3
"""
Define a function that queries the
Reddit API.
"""
import requests
from sys import argv

def number_of_subscribers(subreddit):
    """
    returns the number of subscribers for a given subreddit
    """
    baseUrl = f"https://www.reddit.com/r/{subreddit}/about.json"
    header = {'User-Agent': "0x16-api_advanced/1.0"}
    
    resp = requests.get(baseUrl, headers=header, allow_redirects=False)
    
    if (not resp.ok):
        return 0
    sub_count = resp.json().get('data').get('subscribers')
    return sub_count

if __name__ == "__main__":
    number_of_subscribers(argv[1])
