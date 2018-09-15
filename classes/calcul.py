import numpy as np
from classes.standard import Standard

class Calcul(Standard):
    def __init__(self, default, argv):
        Standard.__init__(self, default, argv)

        self.debug("calcul", "__init__")

        self.data = {}

    def display(self):
        self.debug("calcul", "display")

        for data in self.data:
            print("calcul.display", data, self.data[data])

    def alert(self):
        self.debug("calcul", "alert")

        res_found = False
        for data in self.data:
            res = ''
            var_prices, var_volumes = self.data[data]
            if var_prices > 0:
                res += "- Prices alert: {} ".format(var_prices)
            if var_volumes > 0:
                res += "- Volumes alert: {} ".format(var_volumes)
            if res not in '':
                res_found = True
                print("calcul.alert", data, res)
        if res_found:
            print()
        else:
            print("No variation found")

    def calc(self, data):
        self.debug("calcul", "calc")

        for calc in data:
            name = 'Nones'
            prices = []
            volumes = []
            for line in data[calc]:
                name = line.get('name')
                prices.append(line.get("price"))
                volumes.append(line.get("volume"))

            line_calc = np.array([prices, volumes]).astype(np.float)
            self.data[name] = np.var(line_calc,1)
        return self.data
