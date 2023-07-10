#!/usr/bin/python3
"""module contains function which uses reddit api"""

import requests


def recurse(subreddit, hot_list=[], after=None):
    """
    Reddit API and return a list containing the titles of all hot articles
    for a given subreddit
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': 'Custom User Agent'}
    params = {'limit': 100, 'after': after}

    try:
        response = requests.get(url, headers=headers, params=params, timeout=5)
        response.raise_for_status()
        data = response.json()
        if 'data' in data and 'children' in data['data']:
            posts = data['data']['children']
            for post in posts:
                title = post['data']['title']
                hot_list.append(title)
            after = data['data']['after']
            if after is not None:
                return recurse(subreddit, hot_list, after)
            return hot_list
        return None
    except (requests.exceptions.RequestException, ValueError):
        return None
