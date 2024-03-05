#!/usr/bin/python3
"""query for the users"""


import requests


def number_of_subscribers(subreddit):
    """ functions making
    """
    if subreddit is None or not isinstance(subreddit, str):
        return 0
    headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)\
            AppleWebKit/537.36 (KHTML, like Gecko)\
            Chrome/102.0.0.0 Safari/537.36'
            }
    r = requests.get(
            f"https://www.reddit.com/r/{subreddit}/about.json",
            allow_redirects=False,
            headers=headers
            )
    if r.status_code != 200:
        return 0
    return (r.json()["data"]["subscribers"])
