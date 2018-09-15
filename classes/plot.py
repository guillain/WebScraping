from datetime import datetime
import matplotlib.pyplot as plt
import numpy as np
from classes.standard import Standard

class Plot(Standard):
    def __init__(self, default, argv):
        Standard.__init__(self, default, argv)
        self.debug("plot", "__init__")

        self.figure = plt.figure()

        plt.ion()
        plt.show()

        ax = self.figure.add_subplot(211)
        plt.subplot(211)
        plt.xlabel('Timestamp')
        plt.ylabel('Price')
        plt.title('Top of Price')
        # plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)

        ax = self.figure.add_subplot(212)
        plt.subplot(212)
        plt.xlabel('Timestamp')
        plt.ylabel('Volume')
        plt.title('Top of Volume')
        # plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)

        self.plt = plt

    def display_file(self, file, reports):
        self.debug("plot", "display")
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

            self.plt.subplot(212)
            self.plt.plot(timestamp, volumes, label = report.get('name'))

        self.plt.draw_all()
        self.plt.pause(.001)

    def graph(self, markets):
        self.debug("plot", "graph")
        for market in markets:
            print("market", market, "markets[market]", markets[market])
            dates = []
            prices = []
            volumes = []
            for line in markets[market]:
                dates.append(line.get("timestamp"))
                prices.append(line.get("price"))
                volumes.append(line.get("volume"))

            self.plt.subplot(211)
            self.plt.plot(dates, prices, label = market)

            self.plt.subplot(212)
            self.plt.plot(dates, volumes, label = market)

        self.plt.draw_all()
        self.plt.pause(.001)
