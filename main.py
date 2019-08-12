import requests
import csv
import schedule
import time


'''
    The script to check perticluar link status.
    It will continuously check in every 10 mins.
'''



def checkLinks():
    with open('links.csv', 'rt') as f:
        data = csv.reader(f)
        for link in data:
            # print(link)
            r = requests.get(link[0])
            print('Link: ', link[0], ' Response Code:', r.status_code)

        seconds = time.time()
        local_time = time.ctime(seconds)
        print('[', 'Time : ', local_time, ']')
        print('\n')


# It will check link status in every 10 minutes
schedule.every(10).minutes.do(checkLinks)


while True:
    # Checks whether a scheduled task
    # is pending to run or not
    schedule.run_pending()
    time.sleep(1)
