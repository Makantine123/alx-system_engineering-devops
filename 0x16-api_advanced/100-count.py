#!/usr/bin/python3
"""module contains function which uses reddit api"""
import requests
from collections import Counter


def count_words(subreddit, word_list, after=None):
    """Count words function"""
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
            word_counts = Counter()
            for title in titles:
                words = title.lower().split()
                word_counts.update(words)
            after = data['data']['after']
            if after is not None:
                word_counts.update(count_words(subreddit, word_list, after))
            return word_counts
        return Counter()
    except (requests.exceptions.RequestException, ValueError):
        return Counter()


def print_word_counts(word_counts):
    """Print words function"""
    sorted_counts = sorted(word_counts.items(), key=lambda x: (-x[1], x[0]))
    for word, count in sorted_counts:
        print(f"{word}: {count}")


def count_words(subreddit, word_list):
    """Count words"""
    word_counts = count_words(subreddit, word_list)
    print_word_counts(word_counts)
