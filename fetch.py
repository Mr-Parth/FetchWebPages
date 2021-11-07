#!/usr/bin/env python3

import argparse
import requests
from datetime import datetime
import re

def isValidURL(str):
    regex = ("((http|https)://)(www.)?" +
             "[a-zA-Z0-9@:%._\\+~#?&//=]" +
             "{2,256}\\.[a-z]" +
             "{2,6}\\b([-a-zA-Z0-9@:%" +
             "._\\+~#?&//=]*)")
     
    p = re.compile(regex)
    if (str == None):
        return False

    if(re.search(p, str)):
        return True
    else:
        return False

def fetch_websites(websites=[]):
    for website in websites:
        try:
            r = requests.get(website)
            html = r.text
            file_name = website.split("//")[1]
            with open(f"{file_name}.html", 'w') as file:  # Use file to refer to the file object
                file.write(html)
            with open(f"{file_name}_metadata.txt", 'w') as file:
                img_count, href_count = html.count("<img"), html.count("<a")
                file.write(f"Last Fetch: {datetime.now().strftime('%m/%d/%Y, %H:%M:%S')}\n")
                file.write(f"Image Count: {img_count}\n")
                file.write(f"Links Count: {href_count}\n")
            print(f"Html fetched and stored at {file_name}.html")
        except Exception as err:
            with open(f"fetch_websites.errors.log", 'a+') as file:  # Use file to refer to the file object
                file.write(f"Error while fetching website : {website} at {datetime.now().strftime('%m/%d/%Y, %H:%M:%S')} \n")
                file.write(f"{err} \n \n")
            print(f"Error while fetching website : {website} -> {err}")

def fetch_metadata(website):
    file_name = website
    if "https://" in website or "http://" in website:
        file_name = website.split("//")[1]
    try:
        with open(f"{file_name}_metadata.txt") as file:
            data = file.read()
            print(data)
    except Exception as err:
        print(f"Metadata for website {website} not found. Please fetch website first")

def main():
    parser = argparse.ArgumentParser(description='Fetch websites.')
    parser.add_argument('websites', default=[], type=str, nargs='*',
                        help='websites to fetch')
    parser.add_argument('--metadata', type=str)

    args = parser.parse_args()

    websites = [website for website in args.websites if isValidURL(website)]

    if args.metadata and isValidURL(args.metadata):
        return fetch_metadata(args.metadata)

    if websites:
        return fetch_websites(websites)

    return  print("No Website in Argument")

if __name__ == '__main__':
    main()    


