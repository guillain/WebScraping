#!/bin/python
# @Subject: WebScraping : CSV record : Graph
# @Author: Guillain
# @Email: guillain@gmail.com

import sys
import time
import getopt

from classes.standard import Standard
from classes.report import Report
from classes.scraping import Scraping
from classes.plot import Plot
from classes.market import Market
from classes.calcul import Calcul

class App(Standard):
    def __init__(self, default, argv):
        Standard.__init__(self, default, argv)
        self.report = Report(default, argv)
        self.scraping = Scraping(default, argv)
        self.market = Market(default, argv)
        self.calcul = Calcul(default, argv)
        if self.conf['print_plot']: self.plot = Plot(default, argv)
        if self.conf['load_file']: self.market.data = self.report.get()
        if self.conf['print_file']: self.report.display_file_list()

    def init_params(self, argv):
        self.debug("app","init_params")
        try:
            opts, args = getopt.getopt(argv, "hd:f:t:l:n:c:ARGMPCFSO",
                                       ["help", "debug", "dir", "file=", "timer=", "limit=", "collect_name=", "collect_url="])
            for opt, arg in opts:
                if opt in ("-h", "--help"):
                    self.help()
                    sys.exit()
                elif opt in ("--debug"):
                    self.conf['debug'] = True
                elif opt in ("-d", "--dir"):
                    self.conf['report_dir'] = arg
                elif opt in ("-f", "--file"):
                    self.conf['realtime_file'] = arg
                elif opt in ("-t", "--timer"):
                    self.conf['loop_timer_collector'] = int(arg)
                elif opt in ("-l", "--limit"):
                    self.conf['row_limit'] = int(arg)
                elif opt in ("-n", "--collect_name"):
                    self.conf['collect_name'] = int(arg)
                elif opt in ("-c", "--collect_url"):
                    self.conf['collect_url'] = int(arg)
                elif opt in ("-A"):
                    self.conf['print_alert'] = True
                elif opt in ("-R"):
                    self.conf['print_report'] = True
                elif opt in ("-G"):
                    self.conf['print_scraping'] = True
                elif opt in ("-M"):
                    self.conf['print_market'] = True
                elif opt in ("-P"):
                    self.conf['print_plot'] = True
                elif opt in ("-C"):
                    self.conf['print_calcul'] = True
                elif opt in ("-F"):
                    self.conf['print_file'] = True
                elif opt in ("-S"):
                    self.conf['save_file'] = True
                elif opt in ("-O"):
                    self.conf['load_file'] = True
        except getopt.GetoptError:
            self.help()
            sys.exit(2)

    def help(self):
        self.debug("app","help")

        print('program.py '
              '-h // --help '
              '      --debug '
              '-d / --dir= <output dir> / define the output folder'
              '-f / --file= <filename> / define the files suffix'
              '-t / --timer= <loop timer> / define the collector loop timer'
              '-l / --limit= <row limit> / define the limit to use during the market collection'
              '-n / --collect_name= <name> / define the name for this collection'
              '-u / --collect_url= <url to collect> / define the url to reach to collect the info'
              '-A / -- / display the alert'
              '-R / -- / display the report info'
              '-G / -- / display the scraping info'
              '-M / -- / display the market info'
              '-P / -- / enable and display the graph creation and update'
              '-C / -- / display the calcu info'
              '-F / -- / display the file info'
              '-S / -- / save the scraping output in file'
              '-O / -- / CSV files loader'
              )

    def collector(self):
        self.debug("app","collector")

        try:
            while True:
                self.conf['time_done_collector'] = time.time() + self.conf['loop_timer_collector']

                scraping_data = self.scraping.get(self.scraping.get_html(), self.conf['row_limit'])
                self.report.save(scraping_data)

                market_data = self.market.data_mapping(scraping_data)
                calc_data = self.calcul.calc(market_data)

                self.timer(self.conf['time_done_collector'])
        except KeyboardInterrupt:
            print('Manual break by user')

    def display(self):
        self.debug("app","display")

        try:
            while True:
                self.conf['time_done_display'] = time.time() + self.conf['loop_timer_display']

                if self.conf['print_alert']: self.calcul.alert()
                if self.conf['print_scraping']: self.scraping.display()
                if self.conf['print_report']: self.report.display()
                if self.conf['print_market']: self.market.display()
                if self.conf['print_calcul']: self.calcul.display()
                if self.conf['print_plot']: self.plot.graph(self.market.data)
                # if self.conf.get('print_plot'): self.plot.display_file(self.report.file, self.scraping.data)

                self.timer(self.conf['time_done_display'])
        except KeyboardInterrupt:
            print('Manually stopped')
