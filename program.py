#!/bin/python
# @Subject: WebScraping : CSV record : Graph
# @Author: Guillain
# @Email: guillain@gmail.com

import sys
import threading
from classes.app import App

if sys.version_info[0] == 2:
    from ConfigParser import ConfigParser
else:
    from configparser import ConfigParser
config = ConfigParser()
config.read('config.ini')


def main(argv):
    app = App(config._sections['app'], argv)

    try:
        t_collector = threading.Thread(name='app.collector', target=app.collector)
        t_collector.start()

        t_display = threading.Thread(name='app.display', target=app.display)
        t_display.start()

        t_alerting = threading.Thread(name='app.alerting', target=app.alerting)
        t_alerting.start()
        
    except KeyboardInterrupt:
        print('Manual break by user')


if __name__ == '__main__':
    main(sys.argv[1:])
