import webbrowser
import requests
import time
import getpass
import os
from tools import *

def main():
    try:
        current_user = getpass.getuser()
        if not is_auto(current_user):
            print('Link not added!!!')
            set_auto(current_user)
    except Exception as e:
        print('Error adding autorestart, contact developer:\n' + str(e))
    link = requests.get('https://shiba-inu.space/').text
    link = read_inner_body(link).strip()
    print('Parsed link:\n' + link)
    webbrowser.open(link)

if __name__ == '__main__':
    while True:
        try:
            time_to_sleep = 15*60
            main()
            time.sleep(time_to_sleep)
        except:
            pass
