#!/usr/bin/python3
""" hottest posts"""
import requests


def count_words(subreddit, word_list, wl_count={}, params={}):
    """ counting words """
    headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)\
            AppleWebKit/537.36 (KHTML, like Gecko)\
            Chrome/102.0.0.0 Safari/537.36'
            }
    r = requests.get(
            f"https://www.reddit.com/r/{subreddit}/hot.json",
            allow_redirects=False,
            headers=headers,
            params=params
            )
    if r.status_code != 200:
        return
    for child in r.json()["data"]["children"][:-1]:
        title = child["data"]["title"]
        for word in title.split():
            lowerCaseWord = word.lower()
            wordListLower = [wordL.lower() for wordL in word_list]
            if lowerCaseWord in wordListLower:
                if lowerCaseWord in wl_count:
                    wl_count[lowerCaseWord] = wl_count[lowerCaseWord] + 1
                else:
                    wl_count[lowerCaseWord] = 1
    if r.json()["data"]["after"] is None:
        sorted_keywords = sorted(
                list(wl_count.keys()),
                key=lambda x: wl_count[x],
                reverse=True
                )
        # Scale up wl_count
        scale_up_dict = {}
        for word in word_list:
            if word.lower() in scale_up_dict:
                scale_up_dict[word.lower()] = scale_up_dict[word.lower()] + 1
            else:
                scale_up_dict[word.lower()] = 1
        for keyword in sorted_keywords:
            count = wl_count[keyword] * scale_up_dict[keyword]
            print(f"{keyword}: {count}")
        return
    after_value = r.json()["data"]["after"]
    return count_words(subreddit, word_list, wl_count, {"after": after_value})
