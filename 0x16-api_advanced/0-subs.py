#!/usr/bin/python3

import requests


def number_of_subscribers(subreddit):
    """
    Function queries the reddit API and returns the number of subscribers
    for a given subreddit
    """
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'User-Agent': 'Custom User Agent'}

    try:
        response = requests.get(url, headers=headers, timeout=5)
        data = response.json()
        if 'data' in data and 'subscribers' in data['data']:
            return data['data']['subscribers']
        return 0
    except requests.exceptions.RequestException:
        return 0
