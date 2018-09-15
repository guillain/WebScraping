#!/bin/python
import sys
import time
import getopt


class Standard(object):
    def __init__(self, default, argv):
        self.data = {}
        self.conf = {}
        self.conf['debug'] = int(default["debug"])
        self.conf['row_limit'] = int(default["row_limit"])
        self.conf['loop_timer_collector'] = int(default["loop_timer_collector"])
        self.conf['loop_timer_display'] = int(default["loop_timer_display"])
        self.conf['loop_timer_alert'] = int(default["loop_timer_alert"])
        self.conf['print_report'] = int(default["print_report"])
        self.conf['print_scraping'] = int(default["print_scraping"])
        self.conf['print_market'] = int(default["print_market"])
        self.conf['print_graph'] = int(default["print_graph"])
        self.conf['print_alert'] = int(default["print_alert"])
        self.conf['print_alert_graph'] = int(default["print_alert_graph"])
        self.conf['alert_price_threshold'] = int(default["alert_price_threshold"])
        self.conf['alert_volume_threshold'] = int(default["alert_volume_threshold"])
        self.conf['print_file'] = int(default["print_file"])
        self.conf['report_dir'] = default["report_dir"]
        self.conf['file'] = default["file"]
        self.conf['load_file'] = int(default["load_file"])
        self.conf['save_file'] = int(default["save_file"])
        self.conf['collect_name'] = default["collect_name"]
        self.conf['collect_url'] = default["collect_url"]

        self.debug("standard","__init__")

        self.init_params(argv)

    def init_params(self, argv):
        self.debug("standard","init_params")

        try:
            opts, args = getopt.getopt(argv, "hd:f:t:l:n:c:RPMGADFSO",
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
                elif opt in ("-R"):
                    self.conf['print_report'] = True
                elif opt in ("-P"):
                    self.conf['print_scraping'] = True
                elif opt in ("-M"):
                    self.conf['print_market'] = True
                elif opt in ("-G"):
                    self.conf['print_graph'] = True
                elif opt in ("-A"):
                    self.conf['print_alert'] = True
                elif opt in ("-D"):
                    self.conf['print_alert_graph'] = True
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
        self.debug("standard","help")

        print('program.py '
              '-h // --help '
              '      --debug '
              '-d / --dir= <output dir> / define the output folder'
              '-f / --file= <filename> / define the files suffix'
              '-t / --timer= <loop timer> / define the collector loop timer'
              '-l / --limit= <row limit> / define the limit to use during the market collection'
              '-n / --collect_name= <name> / define the name for this collection'
              '-u / --collect_url= <url to collect> / define the url to reach to collect the info'
              '-G / -- / graph the collection'
              '-A / -- / display the alert info (values of variation)'
              '-D / -- / graph the alert'
              '-R / -- / display the report info'
              '-P / -- / display the scraping info'
              '-M / -- / display the market info'
              '-F / -- / display the file info'
              '-S / -- / save the scraping output in file (compilation, one CSV file by collected entry)'
              '-O / -- / CSV files loader (history)'
              )

    def debug(self, clas, fct, data = None):
        if self.conf['debug']:
            print(">>>>>",clas," - ", fct, " - ", data)

    def timer(self, time_done):
        self.debug("standard", "timer")

        while time.time() < time_done:
            self.debug("standard", "timer", time.strftime("%Y-%m-%d %H:%M:%S"))
            time.sleep(1)