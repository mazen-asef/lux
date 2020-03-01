import json
import time

STANDARD_WAIT_TIME = 0

def wait ():
    while True:
        """
        The user should press enter, which would equate to an empty 
        string. It may look weird, but an empty string could be interpreted
        in python as not 'something', so if it's not something, it's what we
        want. 
        """
        key = input ()
        if not key:
            break

def show_history_branches (conversation):
    for p in conversation['question']:
         print (p)
    branches = conversation['branches']
    for p in branches:
        print(p)
    
def main ():
    with open ('story/eden.json') as json_file:
        data = json.load (json_file)
        for p in data['intro']:
            print (p)
            time.sleep (STANDARD_WAIT_TIME)
        wait ()
        show_history_branches (data)
        wait ()
                
if __name__ == '__main__':
    main ()
