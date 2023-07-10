#!/usr/bin/python3
"""Module contains script that use Reddit API"""

import requests
from collections import Counter


def count_words(subreddit, word_list, after=None, word_counts=None):
    """Count words using recursion"""
    if word_counts is None:
        word_counts = Counter()

    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': 'Custom User Agent'}
    params = {'limit': 100, 'after': after}

    try:
        response = requests.get(url, headers=headers, params=params, timeout=5)
        response.raise_for_status()
        data = response.json()
        if 'data' in data and 'children' in data['data']:
            posts = data['data']['children']
            titles = [post['data']['title'] for post in posts]
            for title in titles:
                words = title.lower().split()
                word_counts.update(words)
            after = data['data']['after']
            if after is not None:
                return count_words(subreddit, word_list, after, word_counts)
        else:
            return None
    except (requests.exceptions.RequestException, ValueError):
        return None

    word_counts_combined = Counter()
    for word in word_list:
        count = sum(word_counts[word.lower()] for word in word_counts if word.lower() == word)
        if count > 0:
            word_counts_combined[word.lower()] += count

    sorted_counts = sorted(word_counts_combined.items(), key=lambda x: (-x[1], x[0].lower()))
    for word, count in sorted_counts:
        print(f"{word}: {count}")
