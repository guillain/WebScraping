from classes.standard import Standard

class Market(Standard):
    def __init__(self, default, argv):
        Standard.__init__(self, default, argv)

        self.debug("market", "__init__")
        self.data = {}

    def display(self):
        self.debug("market", "display")

        for market in self.data:
            market_line = self.data[market]
            for line in self.data[market]:
                print("market.display", line)

    def data_mapping(self, data):
        self.debug("market", "data_mapping")
        for line in data:
            if line.get('name') not in self.data:
                self.data[line.get('name')] = []
            self.data[line.get('name')].append(line)
        return self.data

    def debug(self, clas, fct, data = None):
        if self.conf['debug']:
            print(">>>>>", clas, " - ", fct, " - ", data)