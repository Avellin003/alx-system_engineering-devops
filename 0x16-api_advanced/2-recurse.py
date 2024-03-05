#!/usr/bin/python3
import requests


def recurse(subreddit, hot_list=None, after=None):
    # Initialize hot_list if not provided
    if hot_list is None:
        hot_list = []

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

            # Extract titles and append to hot_list
            for post in data['data']['children']:
                hot_list.append(post['data']['title'])

            # Check for pagination and recursively call the function
            if data['data']['after']:
                return recurse(
                        (subreddit, hot_list, after=data['data']['after']))
            else:
                return hot_list

        elif response.status_code == 404:
            # Subreddit not found, return None
            return None
        else:
            # Handle other status codes if needed
            print(f"Error: {response.status_code}")
            return None

    except Exception as e:
        # Handle any exceptions that may occur during the request
        print(f"Error: {str(e)}")
        return None

# Example usage:


subreddit_name = "python"
result = recurse(subreddit_name)

if result is not None:
    print(f"All hot article titles in r/{subreddit_name}:")
    for title in result:
        print(title)
else:
    print(f"Invalid subreddit or no results found.")
