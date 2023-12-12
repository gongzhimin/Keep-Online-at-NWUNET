import requests
from loguru import logger
from datetime import datetime


url = "http://10.0.1.165/"
usr = '202322882'
pwd = '160029'

def get_current_time():
    """
    Get current time.
    """
    current_time = datetime.now()
    formatted_time = current_time.strftime('%Y-%m-%d %H:%M:%S')
    
    return formatted_time


def set_logger(log_dir='./'):
    logger.remove(handler_id=None)
    logger.add(f"{log_dir}/logs.log", format='{message}', level='INFO')
    
    return logger


LOGGER = set_logger()


def login(usr, pwd):
    """
    Login the account.
    """
    # dictionary for login
    payload = {
        'DDDDD': usr,
        'upass': pwd,
        'R1': '0',
        'R2': '',
        'R3': '0',
        'R6': '0',
        'para': '00',
        '0MKKey': '123456',
        'v6ip': '',
        'hid1': '4575',
        'hid2': '30410004',
        'cn': '0',
        'buttonClicked': '',
        'redirect_url': '',
        'err_flag': '',
        'username': '',
        'password': '',
        'user': '',
        'cmd': '',
        'Login': '',
    }
    msg = f'{get_current_time()}\t Trying to login with [{usr}, {pwd}].'
    print(msg), LOGGER.info(msg)
    s = requests.Session()
    s.get(url)
    s.post(url + 'a70.htm', payload)


if __name__=='__main__':
    login(usr, pwd)
