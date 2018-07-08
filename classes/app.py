#!/bin/python
# @Subject: WebScraping : CSV record : Graph
# @Author: Guillain
# @Email: guillain@gmail.com

import sys
import time
import getopt

from classes.report import Report
from classes.scraping import Scraping
from classes.plot import Plot
from classes.market import Market

class App:
    def __init__(self, default):
        self.default = default
        if self.default.get('debug'): print("app.__init__")

        self.loop_timer_display = default.get("loop_timer_display")
        self.loop_timer_collector = default.get("loop_timer_collector")
        self.row_limit = default.get("row_limit")

        self.report = Report(default)
        self.scraping = Scraping(default)
        self.plot = Plot(default)
        self.market = Market(default)

    def init(self, argv):
        if self.default.get('debug'): print("app.init")

        self.init_params(argv)

        self.market.data = self.report.get()

    def init_params(self, argv):
        if self.default.get('debug'): print("app.init_params")

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
        if self.default.get('debug'): print("app.help")

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

    def collector(self, app):
        try:
            # while True:
            app.time_done_collector = time.time() + app.loop_timer_collector

            app.scraping.data = app.scraping.get(app.scraping.get_html(), app.row_limit)
            app.market.data_mapping(app.scraping.data)
            app.report.save(app.scraping.data)

            self.timer(app.time_done_collector)
        except KeyboardInterrupt:
            print('Manual break by user')

    def display(self, app):
        try:
            # while True:
            app.time_done_display = time.time() + app.loop_timer_display

            if app.default.get('print_scraping'): app.scraping.display()
            if app.default.get('print_report'): app.report.display()
            if app.default.get('print_market'):  app.market.display()

            #app.plot.display_file(app.report.file, app.scraping.data)
            app.plot.graph(app.market.data)

            self.timer(app.time_done_display)
        except KeyboardInterrupt:
            print('Manual break by user')

    def timer(self, time_done):
        while time.time() < time_done:
            print(time.strftime("%Y-%m-%d %H:%M:%S"))
            time.sleep(1)