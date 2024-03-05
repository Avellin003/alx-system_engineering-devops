#!/usr/bin/python3
"""acts on the query subscibers"""
import requests


def number_of_subscribers(subreddit):
    """returns the total sum of subscribers"""
    ul = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    heads = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
    }
    responses = requests.get(ul, heads=heads, allow_redirects=False)
    if responses.status_code == 404:
        return 0
    results = responses.json().get("data")
    return results.get("subscribers")
