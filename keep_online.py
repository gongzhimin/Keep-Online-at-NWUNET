import csv
import time
import random
import requests
from requests.exceptions import Timeout

from login import login


"""
Run this file with logs and no hang-up:
nohup python ./keep_online.py > ./keep_online.log 2>&1 &
"""

time_lag = 1800 # how long (seconds) to check the connection
csv_dir = './accounts.csv'
test_url = "http://www.baidu.com/"


def get_on(usr, pwd):
    print('Disconnection detected, login now.')
    login(usr, pwd)
    print('Login success.')


def listen_switch(csv_dir):
    """
    Keep listening to the connection status, and switch the account periodically.
    """
    # load account pool
    with open(csv_dir, mode='r', encoding="utf-8") as f:
        csv_reader = csv.reader(f)
        accounts = list(csv_reader)
    
    while True:
        random.shuffle(accounts) # shuffle the acount list
        usr, pwd = accounts[0]
        try:
            r = requests.get(test_url, timeout=5)
            if test_url in r.text :
                print('Connected now.')
                print(f'Wait {time_lag} seconds then check again.')
                time.sleep(time_lag)
                continue
            get_on(usr, pwd)
        except Timeout as e:
            get_on(usr, pwd)


if __name__ == "__main__":
    listen_switch(csv_dir)

