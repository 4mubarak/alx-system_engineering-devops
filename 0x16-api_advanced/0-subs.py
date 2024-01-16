#!/usr/bin/python3
"""
Reddit Subscribers Counter

This module provides a function to query the Reddit API and return the number
of subscribers (total subscribers) for a given subreddit. If an invalid subreddit
is given, the function returns 0.

No authentication is necessary for most features of the Reddit API. If you're
getting errors related to Too Many Requests, ensure you're setting a custom User-Agent.

Requirements:
    - Python 3
    - Requests module

Usage:
    - Call the number_of_subscribers(subreddit) function with the desired subreddit.

Example:
    subreddit_name = "python"
    subscribers = number_of_subscribers(subreddit_name)

    if subscribers != 0:
        print(f"The subreddit '{subreddit_name}' has {subscribers} subscribers.")
    else:
        print(f"Invalid subreddit: '{subreddit_name}'.")
"""

import requests

def number_of_subscribers(subreddit):
    """
    Get the number of subscribers for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit.

    Returns:
        int: The number of subscribers for the subreddit. Returns 0 for an invalid subreddit.
    """
    # Reddit API endpoint for subreddit information
    url = f"https://www.reddit.com/r/{subreddit}/about.json"

    # Set a custom User-Agent to avoid Too Many Requests error
    headers = {'User-Agent': 'YourAppName/1.0'}

    # Make the GET request to the Reddit API
    response = requests.get(url, headers=headers)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the JSON response
        data = response.json()

        # Extract the number of subscribers
        subscribers_count = data['data']['subscribers']

        return subscribers_count
    elif response.status_code == 404:
        # Invalid subreddit, return 0
        return 0
    else:
        # Handle other errors
        print(f"Error: {response.status_code}")
        return 0

# Example usage
if __name__ == "__main__":
    subreddit_name = "python"
    subscribers = number_of_subscribers(subreddit_name)

    if subscribers != 0:
        print(f"The subreddit '{subreddit_name}' has {subscribers} subscribers.")
    else:
        print(f"Invalid subreddit: '{subreddit_name}'.")
