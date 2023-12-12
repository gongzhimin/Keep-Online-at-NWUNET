import csv
import time
import random
import requests
from requests.exceptions import Timeout

from login import get_current_time, login, LOGGER


"""
Run this file with logs and no hang-up:
nohup python ./keep_online.py > ./keep_online.log 2>&1 &
"""

time_lag = 1800 # how long (seconds) to check the connection
csv_dir = './accounts.csv'
test_url = "http://www.baidu.com/"


def get_on(usr, pwd):
    msg1 = f'{get_current_time()}\t Disconnection detected, login now.'
    print(msg1), LOGGER.info(msg1)
    login(usr, pwd)
    msg2 = f'{get_current_time()}\t Login success.'
    print(msg2), LOGGER.info(msg2)


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
                msg = f'{get_current_time()}\t Connected now, wait {time_lag} seconds then check again.'
                print(msg), LOGGER.info(msg)
                time.sleep(time_lag)
                continue
            get_on(usr, pwd)
        except Timeout as e:
            get_on(usr, pwd)


if __name__ == "__main__":
    listen_switch(csv_dir)

