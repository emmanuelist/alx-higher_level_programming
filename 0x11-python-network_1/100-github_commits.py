#!/usr/bin/python3
"""Python script that fetches github"""
import requests
import sys


if __name__ == "__main__":
    # headers = {
    #     "Accept": "application/vnd.github.v3+json",
    #     "X-GitHub-Api-Version": "2022-11-28"
    # }
    url = f'https://api.github.com/repos/{sys.argv[2]}/{sys.argv[1]}/commits'

    response = requests.get(url)

    user_data = response.json()
    for i in range(0, 10):
        print(f'{user_data[i].get("sha")}: '
              f'{user_data[i].get("commit").get("author").get("name")}')