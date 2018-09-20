from classes.graph import Graph
import matplotlib.pyplot as plt
import numpy as np


class Alert(Graph):
    def __init__(self, default, argv):
        Graph.__init__(self, default, argv)

        self.debug("alert", "__init__")

        self.calc_data = {}
        self.market_data = {}

    def display_calc(self):
        self.debug("alert", "display_calc")

        if self.calc_data in (None, {}):
            print("No variation found")
            return

        for name in self.calc_data:
            var_prices, var_volumes = self.calc_data[name]
            print('{} - Prices alert: {} - Volumes alert: {}'.format(name, var_prices, var_volumes))

    def calc(self, data):
        self.debug("alert", "calc")

        self.calc_data = {}
        self.market_data = {}

        for calc in data:
            name = 'Nones'
            prices = []
            volumes = []
            for line in data[calc]:
                name = line.get('name')
                prices.append(line.get("price"))
                volumes.append(line.get("volume"))

            line_calc = np.array([prices, volumes]).astype(np.float)
            var_res = np.var(line_calc,1)

            if (var_res[0] > self.conf['alert_price_threshold']) and (var_res[1] > self.conf['alert_volume_threshold']):
                self.calc_data[name] = var_res
                self.market_data[name] = data[calc]

        return self.calc_data
