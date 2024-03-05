#!/usr/bin/python3
"""
Define a function that queries the
Reddit API.
"""
import requests
from sys import argv


def top_ten(subreddit):
    """
    returns the titles of the first 10 hot posts listed for a given subreddit.
    """
    baseUrl = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    header = {'User-Agent': "0x16-api_advanced/1.0"}

    resp = requests.get(baseUrl, headers=header, allow_redirects=False)

    if (not resp.ok):
        print('None')
    else:
        top_ten = resp.json()['data']['children']
        for post in top_ten:
            print(post['data']['title'])


if __name__ == "__main__":
    top_ten(argv[1])
