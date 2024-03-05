#!/usr/bin/python3
"""
the 10 hotest
"""
import requests


def top_ten(subreddit):
    """
    making the function
    """
    if subreddit is None or type(subreddit) is not str:
        print(None)
    headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)\
            AppleWebKit/537.36 (KHTML, like Gecko)\
            Chrome/102.0.0.0 Safari/537.36'
            }
    r = requests.get(
            f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10",
            allow_redirects=False,
            headers=headers
            )
    if r.status_code != 200:
        print("None")
        return
    for child in r.json()["data"]["children"][1:]:
        print(child["data"]["title"])
