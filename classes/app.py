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
from classes.graph import Graph
from classes.market import Market
from classes.calcul import Calcul

class App(Standard):
    def __init__(self, default, argv):
        Standard.__init__(self, default, argv)
        self.report = Report(default, argv)
        self.scraping = Scraping(default, argv)
        self.market = Market(default, argv)
        self.calcul = Calcul(default, argv)
        self.graph = Graph(default, argv)
        if self.conf['load_file']: self.market.data = self.report.get()
        if self.conf['print_file']: self.report.display_file_list()

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
        if self.conf['print_graph']: self.graph.init()

        try:
            while True:
                self.conf['time_done_display'] = time.time() + self.conf['loop_timer_display']

                if self.conf['print_alert']: self.calcul.alert()
                if self.conf['print_scraping']: self.scraping.display()
                if self.conf['print_report']: self.report.display()
                if self.conf['print_market']: self.market.display()
                if self.conf['print_calcul']: self.calcul.display()
                if self.conf['print_graph']: self.graph.trace(self.market.data)
                # if self.conf.get('print_graph'): self.graph.display_file(self.report.file, self.scraping.data)

                self.timer(self.conf['time_done_display'])
        except KeyboardInterrupt:
            print('Manually stopped')
