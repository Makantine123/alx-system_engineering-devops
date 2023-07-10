#!/usr/bin/python3
"""Module contains script that use Reddit API"""

import requests


def count_words(subreddit, word_list, after=None, count_dict=None):
    """Count words using recursion"""
    if count_dict is None:
        count_dict = {}

    base_url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "Mozilla/5.0"}

    params = {"limit": 100}
    if after:
        params["after"] = after

    response = requests.get(base_url, headers=headers, params=params)

    if response.status_code == 200:
        data = response.json()
        posts = data.get("data", {}).get("children", [])

        for post in posts:
            title = post.get("data", {}).get("title", "").lower()
            for word in word_list:
                if title.count(word) > 0:
                    count_dict[word] = count_dict.get(word, 0) + title.count(word)

        after = data.get("data", {}).get("after")
        if after:
            return count_words(subreddit, word_list, after, count_dict)

    sorted_counts = sorted(count_dict.items(), key=lambda x: (-x[1], x[0]))
    for word, count in sorted_counts:
        print(f"{word}: {count}")
