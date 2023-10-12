#!/usr/bin/python3
"""script for parsing web data from an api
"""
import requests


def top_ten(subreddit):
    base_url = f'https://www.reddit.com/r/{subreddit}/top.json?limit=10'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; de; rv:1.9.2.3) '
                      'Gecko/20100401 Firefox/3.6.3 (FM Scene 4.6.1)'
    }

    try:
        response = requests.get(base_url, headers=headers)
        response.raise_for_status()  # Raise an exception for HTTP errors

        data = response.json()

        if 'data' in data and 'children' in data['data']:
            posts = data['data']['children']

            for i, post in enumerate(posts[:10]):
                print(post['data']['title'])

        else:
            print('None')
    except requests.exceptions.RequestException as e:
        print(f'Error: {e}')
    except Exception as e:
        print(f'An error occurred: {e}')
