from classes.graph import Graph
import numpy as np


class Alert(Graph):
    def __init__(self, default, argv):
        Graph.__init__(self, default, argv)

        self.debug("alert", "__init__")

        self.calc_data = {}
        self.market_data = {}

    def display(self, data):
        self.debug("alert", "display")

        for line in data:
            print("alert", "display", line, data[line])

    def display_calc(self):
        self.debug("alert", "display_calc")

        res_found = False
        for data in self.calc_data:
            if data in self.calc_data:
                res = ''
                var_prices, var_volumes = self.calc_data[data]

                if var_prices > self.conf['alert_price_threshold']:
                    res += "- Prices alert: {} ".format(var_prices)

                if var_volumes > self.conf['alert_volume_threshold']:
                    res += "- Volumes alert: {} ".format(var_volumes)

                if res not in '':
                    res_found = True
                    print('{} {}'.format(data, res))

        if res_found:
            print()
        else:
            print("No variation found")

    def calc(self, data):
        self.debug("alert", "calc")

        for calc in data:
            name = 'Nones'
            prices = []
            volumes = []
            for line in data[calc]:
                name = line.get('name')
                prices.append(line.get("price"))
                volumes.append(line.get("volume"))

            line_calc = np.array([prices, volumes]).astype(np.float)
            self.calc_data[name] = np.var(line_calc,1)
            print(name, self.calc_data[name])

            if (self.calc_data[name][0] > self.conf['alert_price_threshold']) \
                    or (self.calc_data[name][1] > self.conf['alert_volume_threshold']):
                self.market_data[name] = data[calc]

        return self.calc_data
