from datetime import datetime
import matplotlib.pyplot as plt
import numpy as np
from classes.standard import Standard


class Graph(Standard):
    def __init__(self, default, argv):
        Standard.__init__(self, default, argv)

        self.debug("graph", "__init__")

    def init(self):
        #figure = plt.figure()
        figure = plt.figure(num=None, figsize=(15, 9), dpi=80, facecolor='w', edgecolor='k')

        plt.ion()
        plt.show()

        ax = figure.add_subplot(211)
        ay = figure.add_subplot(223)

        self.plt = plt

    def screen(self):
        self.plt.subplot(211)
        self.plt.xlabel('Timestamp')
        self.plt.ylabel('Price')
        self.plt.title('Top of Price')

        self.plt.subplot(223)
        self.plt.xlabel('Timestamp')
        self.plt.ylabel('Volume')
        self.plt.title('Top of Volume')

    def display(self):
        self.debug("alert", "display")

        for line in self.data:
            print("alert", "display", line, self.data[line])

    def display_file(self, file, reports):
        self.debug("graph", "display_file")
        for index, report in enumerate(reports):
            timestamp, names, symbols, marketcaps, prices, volumes = \
                np.loadtxt('{}/{}{}'.format(self.conf['report_dir'], report.get('name'), file),
                           dtype={
                               'names': ('timestamp', 'name', 'symbol', 'marketcap', 'price','volume'),
                               'formats': ('S26', 'S32', 'S32', 'S32', 'f4', 'f4')
                           },
                           delimiter=',',
                           unpack=True,
                           skiprows=1
                )

            #dates = [datetime.strptime(ts, '%Y-%m-%d %H:%M:%S') for ts in timestamp]
            dates = []
            for ts in timestamp:
                try:
                    dates.append(datetime.strptime(ts, '%Y-%m-%d %H:%M:%S'))
                except:
                    dates.append(datetime.strptime(ts, '%Y-%m-%d %H:%M:%S.%f'))

            self.plt.subplot(211)
            self.plt.plot(timestamp, prices, label = report.get('name'))

            self.plt.subplot(223)
            self.plt.plot(timestamp, volumes, label = report.get('name'))

        self.plt.draw_all()
        self.plt.pause(.001)

    def trace(self, markets):
        self.debug("graph", "trace")

        if markets in (None, {}):
            return

        self.plt.clf()
        self.screen()
        for market in markets:
            #print("graph", "trace", market, markets[market])

            dates = []
            prices = []
            volumes = []
            counter = 0
            #market_date_sorted = markets[market].sort(key=lambda r: r['timestamp'])
            ##market_date_sorted = sorted(markets[market].items(), key=lambda p: p[1], reverse=True)
            #print("market_date_sorted",market_date_sorted)
            for line in markets[market]:
                if counter < 100:
                    dates.append(line.get("timestamp"))
                    prices.append(line.get("price"))
                    volumes.append(line.get("volume"))
                counter = counter + 1

            self.plt.subplot(211)
            self.plt.plot(dates, prices, label = market)

            self.plt.subplot(223)
            self.plt.plot(dates, volumes, label = market)

        self.plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
        self.plt.draw_all()
        self.plt.pause(.001)
