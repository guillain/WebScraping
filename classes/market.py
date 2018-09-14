import numpy as np

class Market:
    def __init__(self, default):
        self.data = {}

    def display(self):
        for market in self.data:
            market_line = self.data[market]
            for line in self.data[market]:
                print("market.display", line)

    def data_mapping(self, data):
        for line in data:
            if line.get('name') not in self.data:
                self.data[line.get('name')] = []
            self.data[line.get('name')].append(line)
        return self.data