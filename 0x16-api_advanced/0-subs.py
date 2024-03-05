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
    subs = 0
    results = None

    with requests.get(f"https://www.reddit.com/r/{subreddit}/top.json",
             allow_redirects=False) as response:
        if (response.status_code == 200):
            res = response.json()
            subs = res["data"]["children"][0]["data"]["subreddit_subscribers"]

    return (subs)

if __name__ == "__main__":
    number_of_subscribers(argv[1])
