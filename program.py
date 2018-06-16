#!/bin/python
# @Subject: Scraping collect
# @Author: Guillain
# @Email: guillain@gmail.com
import os
import sys
import getopt
import time
import re
import datetime
import bs4
import requests
import collections

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.dates import DayLocator, HourLocator, DateFormatter, drange

# Constantes definition
LOOP_TIMER = 5 # (s)
ROW_LIMIT = 10
REPORT_DIR = "reports"
CSF_FILE_realtime = "realtime_report.csv"
CSF_FILE_timeserial = "timeserial_report.csv"
timeserial_file = ""

# Collection definition
CollectName = "coinmarketcap"
CollectUrl = "https://coinmarketcap.com/fr/all/views/all/"
CollectReport = collections.namedtuple(CollectName, 'timestamp, name, symbol, marketcap, price, volume')

def help():
    print( 'program.py '
           '-t <loop timer> '
           '-l <row limit> '
           '-o <order> '
           '-s <timeserie file> '
           '-r <realtime file> '
           '-D <output dir> '
           '-h '
    )

# Start Main program
def main(argv):
    report_dir = REPORT_DIR
    loop_timer = LOOP_TIMER
    row_limit = ROW_LIMIT
    realtime_file = CSF_FILE_realtime
    timeserial_file = CSF_FILE_timeserial

    # Get params
    try:
        opts, args = getopt.getopt(argv,"hr:s:t:l:o:D:",["timer=","rfile=","sfile=","dir=","limit=","order="])
        for opt, arg in opts:
            if opt == '-h':
                help()
                sys.exit()
            elif opt in ("-D", "--dir"):
                report_dir = arg
            elif opt in ("-r", "--rfile"):
                realtime_file = arg
            elif opt in ("-s", "--sfile"):
                timeserial_file = arg
            elif opt in ("-t", "--timer"):
                loop_timer = int(arg)
            elif opt in ("-l", "--limit"):
                row_limit = int(arg)
            elif opt in ("-o", "--order"):
                row_order = int(arg)
    except getopt.GetoptError:
        help()
        sys.exit(2)

    # Init the headers
    print_the_header()

    # Timer = loop
    try:
        while True:
            # save the loop starting time
            time_done = time.time() + loop_timer

            html = get_html_from_web()
            reports = get_reports_from_html(html,row_limit)
            print_report(reports)
            save_report(report_dir, realtime_file, reports, 'group')
            save_report(report_dir, timeserial_file, reports, '')
            #print_plot(timeserial_file, reports)

            # check timer and wait if necessary
            while(time.time() < time_done):
                print(time.strftime("%Y-%m-%d %H:%M:%S"))
                time.sleep(1)
    except KeyboardInterrupt:
        print('Manual break by user')


def print_the_header():
    print('-----------------------------------')
    print('            {} APP'.format(CollectName))
    print('-----------------------------------')
    print('')

def print_report(reports):
    for report in reports:
        # display for the collection
        print('{} \t {} \t {} \t {} \t {} \t {}'.format(
            report.timestamp.strftime("%Y-%m-%d %H:%M:%S"),
            report.name,
            report.symbol,
            report.marketcap,
            report.price,
            report.volume
        ))

def print_plot(file, reports):
    for report in reports:
        timestamp, name, marketcap, price, volume = np.loadtxt('{}/{}-{}'.format(REPORT_DIR, report.name, file), delimiter=',', unpack=True)
        plt.plot(datetime.strptime(timestamp, '%Y-%m-%d %H:%M:%S'), price, label='Loaded from file!')
        plt.xlabel('timestamp')
        plt.ylabel('price')
        plt.title('price of ')
        plt.legend()
        plt.show()

def save_report(dir, file, reports, option):
    for report in reports:
        report_name = report.name
        if 'group' in option:
            report_name = 'Global'
        filename = '{}/{}-{}'.format(dir, report_name,file)

        if not os.path.isfile(filename):
            save_report_header(filename)

        save_report_content(filename, report)

def save_report_header(filename):
    with open(filename, 'w') as f:
        f.write('{},{},{},{},{}\n'.format(
            "timestamp",
            "name",
            "symbol",
            "marketcap",
            "price",
            "volume"
        ))

def save_report_content(filename, report):
    with open(filename, 'a') as f:
        f.write('{},{},{},{},{}\n'.format(
            report.timestamp,
            report.name,
            report.symbol,
            report.marketcap,
            report.price,
            report.volume
        ))

def get_html_from_web():
    response = requests.get(CollectUrl)
    return response.text

def get_reports_from_html(html,limit):
    reports = []
    timestamp = datetime.datetime.now()
    soup = bs4.BeautifulSoup(html, 'html.parser')
    table = soup.find(id='currencies-all')
    table_body = table.find('tbody')
    rows = table_body.find_all('tr')
    index = 0

    for row in rows:
        reports.append(
            CollectReport(
                timestamp=timestamp,
                name=cleanup_text(row.find(class_='currency-name').get_text()),
                symbol=cleanup_text(row.find(class_='currency-symbol').get_text()),
                marketcap=cleanup_text(row.find(class_='market-cap').get_text()),
                price=cleanup_text(row.find(class_='price').get_text()),
                volume=cleanup_text(row.find(class_='volume').get_text())
            )
        )
        index = index + 1
        if index > limit:
            return reports
    return reports

def cleanup_text(text):
    if not text:
        return text

    text = re.sub('[^A-Za-z0-9]+', '', text)

    """text = text.strip()
    text = text.replace('$','')
    text = text.replace(',','')
    text = text.replace(' ', '_')
    text = text.replace('\\', '')
    text = text.replace('/', '')
    text = text.replace('\n', '')
    """
    return text

if __name__ == '__main__':
   main(sys.argv[1:])