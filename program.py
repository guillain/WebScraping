#!/bin/python
# @Subject: WebScraping : CSV record : Graph
# @Author: Guillain
# @Email: guillain@gmail.com

import sys
import threading
from classes.app import App

# Constantes definition
default = {
    "debug": True,
    "row_limit": 15,
    "loop_timer_display": 5,  # (s)
    "loop_timer_collector": 0,  # (s)
    "print_report": False,
    "print_scraping": False,
    "print_market": False,
    "print_plot": False,
    "print_calcul": False,
    "print_file": False,
    "report_dir": "reports",
    "file": "-timeserial_report.csv",
    "load_file": False,
    "collect_name": "coinmarketcap",
    "collect_url": "https://coinmarketcap.com/fr/all/views/all/"
}

def main(argv):
    app = App(default)
    app.init(argv)

    try:
        #while True:
            #app.collector()
            #app.display()

        t_collector = threading.Thread(name='app.collector', target=app.collector)
        t_collector.start()

        t_display = threading.Thread(name='app.display', target=app.display)
        t_display.start()

    except KeyboardInterrupt:
        print('Manual break by user')

if __name__ == '__main__':
    main(sys.argv[1:])