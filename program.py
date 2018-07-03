#!/bin/python
# @Subject: WebScraping : CSV record : Graph
# @Author: Guillain
# @Email: guillain@gmail.com

import sys
import getopt
import time

from classes.report import Report
from classes.scraping import Scraping
from classes.plot import Plot

# Constantes definition
default = {
    "loop_timer": 5, # (s)
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
        self.loop_timer = default.get("loop_timer")
        self.row_limit = default.get("row_limit")

        self.report = Report(default)
        self.scraping = Scraping(default)
        self.plot = Plot(default)

        self.init_params(argv)

    def init_params(self, argv):
        try:
            opts, args = getopt.getopt(argv, "hf::t:l:o:d:PF",
                                       ["help", "noplot", "nofile", "timer=", "file=", "dir=", "limit=","order="])
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

# Start Main program
def main(argv):
    app = App(default, argv)
    try:
        while True:
            app.time_done = time.time() + app.loop_timer
            reports = app.scraping.get_reports(app.scraping.get_html(), app.row_limit)
            app.report.display(reports)
            app.report.save(app.report.file, reports)
            app.plot.display_file(app.report.file, reports)
            while time.time() < app.time_done:
                print(time.strftime("%Y-%m-%d %H:%M:%S"))
                time.sleep(1)
    except KeyboardInterrupt:
        print('Manual break by user')

if __name__ == '__main__':
   main(sys.argv[1:])