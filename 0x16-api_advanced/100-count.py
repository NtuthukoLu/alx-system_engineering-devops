#!/usr/bin/python3
import requests

def count_words(subreddit, word_list, after=None, counts=None):
    if counts is None:
        counts = {}

    url = f'https://www.reddit.com/r/{subreddit}/hot.json?limit=100'
    headers = {
        'User-Agent': 'MyRedditBot/1.0 (by YourUsername)'
    }
    params = {'after': after} if after else None

    try:
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()  # Raise an exception for HTTP errors

        data = response.json()

        if 'data' in data and 'children' in data['data']:
            posts = data['data']['children']

            for post in posts:
                title = post['data']['title'].lower()
                for word in word_list:
                    if word.lower() in title:
                        if word in counts:
                            counts[word] += 1
                        else:
                            counts[word] = 1

            after = data['data']['after']

            if after is not None:
                return count_words(subreddit, word_list, after, counts)

    except requests.exceptions.RequestException as e:
        print(f'Error: {e}')
    except Exception as e:
        print(f'An error occurred: {e}')

    sorted_counts = sorted(counts.items(), key=lambda item: (-item[1], item[0]))
    for word, count in sorted_counts:
        print(f"{word}: {count}")
