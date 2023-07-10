#!/usr/bin/python3
"""module contains function which uses reddit api"""
import requests


def top_ten(subreddit):
    """Fetches top 10 titles of hot posts"""
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': 'Custom User Agent'}
    params = {'limit': 10}

    try:
        response = requests.get(url, headers=headers, params=params, timeout=5)
        response.raise_for_status()
        data = response.json()
        if 'data' in data and 'children' in data['data']:
            posts = data['data']['children']
            for post in posts:
                title = post['data']['title']
                print(title)
        else:
            print(None)
    except (requests.exceptions.RequestException, ValueError):
        print(None)
