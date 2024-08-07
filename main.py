import requests
from typing import Union
import json

base_url = "https://spoo.me"


def shorten_url():
    url: str = input("Enter the URL to be shortened: ")
    alias = None
    password = None
    max_clicks = None

    choice = input("Do you want to use an alias? (y/n): ")
    if choice == "y":
        alias: Union[str, None] = input("Enter the alias: ")

    choice = input("Do you want to use an password? (y/n): ")
    if choice == "y":
        password: Union[str, None] = input("Enter the password: ")

    choice = input("Do you want to use an max no: of clicks? (y/n): ")
    if choice == "y":
        max_clicks: Union[int, None] = int(input("Enter the maximum number of clicks: "))

    options = {'url': url, 'alias': alias if alias else None, 'password': password if password else None, 'max-clicks': max_clicks if max_clicks else None}
    headers = {"Accept": "application/json"}

    response = requests.post(base_url, data=options, headers=headers)
    if response.status_code == 200:
        print(response.json())
    else:
        print(f"Error: {response.status_code}")
        print(response.text)
        return None

def get_stats():
    password = None
    code: str = input("Enter the code to get the stats: ")

    confirmation = input("Do you have a password for the url code? (y/n): ")
    if confirmation == "y":
        password: Union[str, None] = input("Enter the password: ")

    url = f"{base_url}/stats/{code}"
    headers = {"Password": password} if password else None

    response = requests.post(url, headers=headers)
    if response.status_code == 200:
        print(json.dumps(response.json(), indent=4))
    else:
        print(f"Error: {response.status_code}")
        print(response.text)
        return None

def main():
    while True:
        print()
        print("Welcome to the URL Shortener!")
        print("-------------------------------")
        print()
        print("1. Shorten URL")
        print("2. Get Stats")
        print("3. Exit")
        options: int = int(input("What do you want to do?: "))

        if options == 1:
            shorten_url()
        elif options == 2:
            get_stats()
        elif options == 3:
            print("Exiting...")
            break
        else:
            print("Invalid option!")


if __name__ == "__main__":
    main()
