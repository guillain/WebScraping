#!/bin/python
# @Subject: WebScraping : CSV record : Graph
# @Author: Guillain
# @Email: guillain@gmail.com

import sys
import threading
from classes.app import App

# Constantes definition
default = {
    "debug": 1,
    "loop_timer_display": 5,  # (s)
    "loop_timer_collector": 0,  # (s)
    "print_scraping": 0, #0/1
    "print_report": 0, #0/1
    "print_market": 1, #0/1
    "row_limit": 10,
    "report_dir": "reports",
    "plot_bool": True,
    "file_bool": True,
    "file": "-timeserial_report.csv",
    "collect_name": "coinmarketcap",
    "collect_url": "https://coinmarketcap.com/fr/all/views/all/"
}

def main(argv):
    app = App(default)
    app.init(argv)

    try:
        while True:
            app.collector(app)
            app.display(app)

            #t_collector = threading.Thread(name='ap.collector', target=collector, args=app)
            #t_collector.start()
            #t_display = threading.Thread(name='app.display', target=display, args=app)
            #t_display.start()

    except KeyboardInterrupt:
        print('Manual break by user')

if __name__ == '__main__':
    main(sys.argv[1:])