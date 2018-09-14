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
from classes.calcul import Calcul

class App:
    def __init__(self, default):
        self.default = default
        if self.default.get('debug'): print("app.__init__")

        self.loop_timer_display = default.get("loop_timer_display")
        self.loop_timer_collector = default.get("loop_timer_collector")
        self.row_limit = default.get("row_limit")

        self.report = Report(default)
        self.scraping = Scraping(default)
        self.market = Market(default)
        self.calcul = Calcul(default)

        if self.default.get('print_plot'): self.plot = Plot(default)

    def init(self, argv):
        if self.default.get('debug'): print("app.init")

        self.init_params(argv)

        if self.default.get('load_file'):
            self.market.data = self.report.get()

    def init_params(self, argv):
        if self.default.get('debug'): print("app.init_params")
        try:
            opts, args = getopt.getopt(argv, "hd:f:t:l:n:c:RSMPCFO",
                                       ["help", "debug", "dir", "file=", "timer=", "limit=", "collect_name=", "collect_url="])
            for opt, arg in opts:
                if opt in ("-h", "--help"):
                    self.help()
                    sys.exit()
                elif opt in ("--debug"):
                    self.debug = True
                elif opt in ("-d", "--dir"):
                    self.plot.report_dir = arg
                    self.report.report_dir = arg
                elif opt in ("-f", "--file"):
                    self.report.realtime_file = arg
                elif opt in ("-t", "--timer"):
                    self.loop_timer_collector = int(arg)
                elif opt in ("-l", "--limit"):
                    self.row_limit = int(arg)
                elif opt in ("-n", "--collect_name"):
                    self.collect_name = int(arg)
                elif opt in ("-c", "--collect_url"):
                    self.plot.collect_url = int(arg)
                elif opt in ("-R"):
                    self.report.print_report = True
                elif opt in ("-S"):
                    self.report.print_scraping = True
                elif opt in ("-M"):
                    self.report.print_market = True
                elif opt in ("-P"):
                    self.report.print_plot = True
                elif opt in ("-C"):
                    self.report.print_calcul = True
                elif opt in ("-F"):
                    self.report.print_file = True
                elif opt in ("-O"):
                    self.report.old_file = True
        except getopt.GetoptError:
            self.help()
            sys.exit(2)

    def help(self):
        if self.default.get('debug'): print("app.help")

        print('program.py '
              '-h // --help '
              '      --debug '
              '-d / --dir= <output dir> / define the output folder'
              '-f / --file= <filename> / define the files suffix'
              '-t / --timer= <loop timer> / define the collector loop timer'
              '-l / --limit= <row limit> / define the limit to use during the market collection'
              '-n / --collect_name= <name> / define the name for this collection'
              '-u / --collect_url= <url to collect> / define the url to reach to collect the info'
              '-R / -- / display the report info'
              '-S / -- / display the scraping info'
              '-M / -- / display the market info'
              '-P / -- / enable the graph creation and update'
              '-C / -- / display the calcu info'
              '-F / -- / display the file info'
              '-O / -- / load old the files info'
              )

    def collector(self):
        try:
            while True:
                self.time_done_collector = time.time() + self.loop_timer_collector

                scraping_data = self.scraping.get(self.scraping.get_html(), self.row_limit)
                self.report.save(scraping_data)

                market_data = self.market.data_mapping(scraping_data)
                max_data = self.calcul.calc(market_data)


                self.timer(self.time_done_collector)
        except KeyboardInterrupt:
            print('Manual break by user')

    def display(self):
        try:
            while True:
                self.time_done_display = time.time() + self.loop_timer_display

                self.calcul.alert()
                if self.default.get('print_scraping'): self.scraping.display()
                if self.default.get('print_report'): self.report.display()
                if self.default.get('print_market'): self.market.display()
                if self.default.get('print_calcul'): self.calcul.display()
                if self.default.get('print_plot'): self.plot.graph(self.market.data)
                # if self.default.get('print_plot'): self.plot.display_file(self.report.file, self.scraping.data)

                self.timer(self.time_done_display)
        except KeyboardInterrupt:
            print('Manually stopped')

    def timer(self, time_done):
        while time.time() < time_done:
            if self.default.get('debug'): print(time.strftime("%Y-%m-%d %H:%M:%S"))
            time.sleep(1)