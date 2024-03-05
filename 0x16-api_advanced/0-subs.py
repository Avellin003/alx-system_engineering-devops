#!/usr/bin/python3
import requests


def number_of_subscribers(subreddit):
    # Reddit API endpoint for fetching subreddit information
    api_url = f"https://www.reddit.com/r/{subreddit}/about.json"

    # Set a custom User-Agent to avoid Too Many Requests errors
    headers = {'User-Agent': 'YourApp/1.0'}

    try:
        # Make the GET request to the Reddit API
        response = requests.get(api_url, headers=headers)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Parse the JSON response
            data = response.json()

            # Extract and return the number of subscribers
            return data['data']['subscribers']
        elif response.status_code == 404:
            # Subreddit not found, return 0
            return 0
        else:
            # Handle other status codes if needed
            print(f"Error: {response.status_code}")
            return 0

    except Exception as e:
        # Handle any exceptions that may occur during the request
        print(f"Error: {str(e)}")
        return 0

# Example usage:


subreddit_name = "python"
subscribers_count = number_of_subscribers(subreddit_name)

if subscribers_count > 0:
    print(f"The subreddit r/{subreddit_name} has {subscribers_count}\
            subscribers.")
else:
    print(f"Invalid subreddit or an error occurred.")
