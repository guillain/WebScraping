import numpy as np

class Calcul:
    def __init__(self, default):
        self.data = {}

    def display(self):
        for data in self.data:
            print("calcul.display", data, self.data[data])

    def alert(self):
        for data in self.data:
            res = ''
            var_prices, var_volumes = self.data[data]
            if var_prices > 0:
                res += "- Prices alert: {} ".format(var_prices)
            if var_volumes > 0:
                res += "- Volumes alert: {} ".format(var_volumes)
            if res not in '':
                print("calcul.alert", data, res)
        print()

    def calc(self, data):
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