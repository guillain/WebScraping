from datetime import datetime
import matplotlib.pyplot as plt
import numpy as np

class Plot:
    def __init__(self, default):
        self.report_dir = default.get("report_dir")
        self.plot_bool = default.get("plot_bool")
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
        for index, report in enumerate(reports):
            timestamp, name, marketcap, price, volume = \
                np.loadtxt('{}/{}{}'.format(self.report_dir, report.name, file),
                           dtype={
                               'names': ('timestamp', 'name', 'marketcap', 'price','volume'),
                               'formats': ('S26', 'S32', 'S32', 'f4', 'f4')
                           },
                           delimiter=',',
                           unpack=True,
                           skiprows=1
                )
            dates_list = [datetime.strptime(ts, '%Y-%m-%d %H:%M:%S.%f') for ts in timestamp]

            self.plt.subplot(211)
            self.plt.plot(dates_list, price, label=report.name)

            self.plt.subplot(212)
            self.plt.plot(dates_list, volume, label=report.name)

        self.plt.draw_all()
        self.plt.pause(.001)