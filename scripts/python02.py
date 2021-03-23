#!/usr/bin/python3
"""A simple API request script || rzfeeser@alta3.com"""

ASTROS = "http://api.open-notify.org/astros.json"

# python3 -m pip install requests
import requests

def main():

    # make a request via requests library
    spacenauts = requests.get(ASTROS)
    
    # remove the json attached to the 200 response
    spacenauts = spacenauts.json()

    # display just the list (array) of space travelers
    print(spacenauts.get("people"))
    
if __name__ == "__main__":
    main()