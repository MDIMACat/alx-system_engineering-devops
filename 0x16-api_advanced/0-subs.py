#!/usr/bin/python3
"""
Define a function that queries the
Reddit API.
"""
from requests import get


if __name__ == "__main__":
    
    def number_of_subscribers(subreddit):
        """
        returns the number of subscribers for a given subreddit
        """
        baseUrl = f"https://www.reddit.com/r/{subreddit}/about.json"
        header = {'User-Agent': "0x16-api_advanced/1.0"}
        
        resp = get(baseUrl, headers=header, allow_redirects=False)
        
        if resp.status_code == 200:
            try:
                data = resp.json()
                sub_info = data['data']['subscribers']
                return sub_info
            except Exception:
                return 0
