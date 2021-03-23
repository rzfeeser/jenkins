#!/usr/bin/python3
"""A simple API request script || rzfeeser@alta3.com"""

ASTROS = "http://api.open-notify.org/iss-now.json"

# python3 -m pip install requests
import requests

def main():

    # make a request via requests library
    isslocation = requests.get(ASTROS)
    
    # remove the json attached to the 200 response
    isslocation = isslocation.json()
    
    # create a file called "../locationISS.txt"
    # containing our desired data set
    with open("../locationISS.txt") as f:
        f.write(isslocation.get("iss_position"))
        
    
if __name__ == "__main__":
    main()