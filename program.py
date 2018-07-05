#!/bin/python
# @Subject: WebScraping : CSV record : Graph
# @Author: Guillain
# @Email: guillain@gmail.com

import sys
import getopt
import time
import threading

from classes.report import Report
from classes.scraping import Scraping
from classes.plot import Plot

# Constantes definition
default = {
    "loop_timer_display": 5,  # (s)
    "loop_timer_collector": 0,  # (s)
    "row_limit": 10,
    "report_dir": "reports",
    "plot_bool": True,
    "file_bool": True,
    "file": "-timeserial_report.csv",
    "collect_name": "coinmarketcap",
    "collect_url": "https://coinmarketcap.com/fr/all/views/all/"
}


class App:
    def __init__(self, default, argv):
        self.loop_timer_display = default.get("loop_timer_display")
        self.loop_timer_collector = default.get("loop_timer_collector")
        self.row_limit = default.get("row_limit")

        self.report = Report(default)
        self.scraping = Scraping(default)
        self.plot = Plot(default)

        self.init_params(argv)

    def init_params(self, argv):
        try:
            opts, args = getopt.getopt(argv, "hf::t:l:o:d:PF",
                                       ["help", "noplot", "nofile", "timer=", "file=", "dir=", "limit=", "order="])
            for opt, arg in opts:
                if opt in ("-d", "--help"):
                    self.help()
                    sys.exit()
                elif opt in ("-d", "--dir"):
                    self.plot.report_dir = arg
                    self.report.report_dir = arg
                elif opt in ("-f", "--file"):
                    self.report.realtime_file = arg
                elif opt in ("-t", "--timer"):
                    self.loop_timer = int(arg)
                elif opt in ("-l", "--limit"):
                    self.row_limit = int(arg)
                elif opt in ("-o", "--order"):
                    self.plot.row_order = int(arg)
                elif opt in ("-P", "--noplot"):
                    self.plot.plot_bool = False
                elif opt in ("-F", "--nofile"):
                    self.report.file_bool = False
        except getopt.GetoptError:
            self.help()
            sys.exit(2)

    def help(self):
        print('program.py '
              '-t / --timer= <loop timer> '
              '-l / --limit= <row limit> '
              '-o / --order= <order> '
              '-f / --file= <filename> '
              '-d / --dir= <output dir> '
              '-P / --noplot '
              '-F / --nofile '
              '-h // --help '
              )

def collector(app):
    try:
            #while True:
            app.time_done_collector = time.time() + app.loop_timer_collector

            app.reports = app.scraping.get_reports(app.scraping.get_html(), app.row_limit)
            app.scraping.display(app.reports)
            app.report.save(app.report.file, app.reports)

            while time.time() < app.time_done_collector:
                print(time.strftime("%Y-%m-%d %H:%M:%S"))
                time.sleep(1)
    except KeyboardInterrupt:
        print('Manual break by user')

def display(app):
    try:
            #while True:
            app.time_done_display = time.time() + app.loop_timer_display

            app.markets = app.report.data_mapping(app.markets, app.reports)
            print(app.markets)
            app.report.display(app.markets)
            app.plot.display_file(app.report.file, app.reports)

            while time.time() < app.time_done_display:
                print(time.strftime("%Y-%m-%d %H:%M:%S"))
                time.sleep(1)
    except KeyboardInterrupt:
        print('Manual break by user')

def main(argv):
    app = App(default, argv)
    app.markets = {}

    """
    data = app.report.load(app.report.report_dir)
    print(data)
    for entry in data:
        print ', '.join(entry)
    """
    try:
        while True:
            collector(app)
            display(app)

            #t_collector = threading.Thread(name='collector', target=collector, args=app)
            #t_collector.start()
            #t_display = threading.Thread(name='display', target=display, args=app)
            #t_display.start()

    except KeyboardInterrupt:
        print('Manual break by user')

if __name__ == '__main__':
    main(sys.argv[1:])