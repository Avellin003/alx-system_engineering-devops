#!/usr/bin/env python3
import requests
from collections import Counter


def count_words(subreddit, word_list, after=None, counts=None):
    # Initialize counts if not provided
    if counts is None:
        counts = Counter()

    # Reddit API endpoint for fetching hot posts in a subreddit
    api_url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=100"

    # Set a custom User-Agent to avoid Too Many Requests errors
    headers = {'User-Agent': 'YourApp/1.0'}

    # Add 'after' parameter if it's not None
    if after:
        api_url += f"&after={after}"

    try:
        # Make the GET request to the Reddit API
        response = requests.get(api_url, headers=headers)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Parse the JSON response
            data = response.json()

            # Extract titles and update counts
            for post in data['data']['children']:
                title = post['data']['title'].lower()
                for word in word_list:
                    if f" {word.lower()} " in f" {title} ":
                        counts[word.lower()] += 1

            # Check for pagination and recursively call the function
            if data['data']['after']:
                return count_words(subreddit, word_list, after=data['data']['after'], counts=counts)
            else:
                # Print the sorted counts
                for word, count in sorted(counts.items(), key=lambda x: (-x[1], x[0])):
                    print(f"{word}: {count}")

        elif response.status_code == 404:
            # Subreddit not found, print nothing
            pass
        else:
            # Handle other status codes if needed
            print(f"Error: {response.status_code}")

    except Exception as e:
        # Handle any exceptions that may occur during the request
        print(f"Error: {str(e)}")

# Example usage:


subreddit_name = "python"
keywords = ["python", "java", "javascript", "reddit"]

print(f"Keyword counts in r/{subreddit_name}:")
count_words(subreddit_name, keywords)
