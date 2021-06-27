import requests
from bs4 import BeautifulSoup
import time
import datetime;

POLLING_INTERVAL_SEC = 60
WORLD_STATUS_URL = 'https://na.finalfantasyxiv.com/lodestone/worldstatus/'
SERVER_NAMES_TO_CHECK = [ 'Shiva', 'Odin', 'Twintania' ]

while True:
    print('[{}] Checking server status... '.format(datetime.datetime.now()))
    page = requests.get(WORLD_STATUS_URL)

    soup = BeautifulSoup(page.content, 'html.parser')
    all_servers = soup.find_all('div', class_='world-list__item')

    for server in all_servers:
        server_name_div = server.find('div', class_='world-list__world_name')
        server_name = server_name_div.p.text

        if server_name in SERVER_NAMES_TO_CHECK:
            create_status_div = server.find('div', class_='world-list__create_character')
            create_status = create_status_div.i['class'][0]

            if create_status == 'world-ic__available':
                print('\t{} is AVAILABLE !!!!!!!!!!!!!!!!!!!!!!!!'.format(server_name))

    time.sleep(POLLING_INTERVAL_SEC)