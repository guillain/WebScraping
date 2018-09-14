import numpy as np

class Calcul:
    def __init__(self, default):
        self.data = {}

    def display(self):
        #print("calcul.display", self.data)
        for calc in self.data:
            print("calcul.display", calc, self.data[calc])

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