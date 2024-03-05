#!/usr/bin/env python3
import requests


def top_ten(subreddit):
    # Reddit API endpoint for fetching hot posts in a subreddit
    api_url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"

    # Set a custom User-Agent to avoid Too Many Requests errors
    headers = {'User-Agent': 'YourApp/1.0'}

    try:
        # Make the GET request to the Reddit API
        response = requests.get(api_url, headers=headers)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Parse the JSON response
            data = response.json()

            # Extract and print the titles of the first 10 hot posts
            for post in data['data']['children']:
                print(post['data']['title'])

        elif response.status_code == 404:
            # Subreddit not found, print None
            print(None)
        else:
            # Handle other status codes if needed
            print(f"Error: {response.status_code}")
            print(None)

    except Exception as e:
        # Handle any exceptions that may occur during the request
        print(f"Error: {str(e)}")
        print(None)

# Example usage:


subreddit_name = "python"
print(f"Top 10 hot posts in r/{subreddit_name}:")
top_ten(subreddit_name)
