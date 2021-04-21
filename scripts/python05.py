#!/usr/bin/python3
"""Russell Zachary Feeser || rzfeeser@alta3.com"""

# std library imports
import json

def main():
    with open("onISS.txt") as f:
        #print(f.read())
        data = json.load(f)
        print(data)
        
        
if __name__ == "__main__":
    main()