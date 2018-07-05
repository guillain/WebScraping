import csv
from os import listdir, path
from os.path import isfile, join

class Report:
    def __init__(self, default):
        self.report_dir = default.get("report_dir")
        self.file = default.get("file")
        self.file_bool = default.get("file_bool")

    def check_exec(self):
        if self.file_bool in ('True', True):
            return True
        return False

    def display(self, reports):
        for report_name in reports:
            print(report_name)
            for report in reports[report_name]:
                print('{} \t {} \t {} \t {} \t {} \t {}'.format(
                    report.timestamp.strftime("%Y-%m-%d %H:%M:%S"),
                    report.name,
                    report.symbol,
                    report.marketcap,
                    report.price,
                    report.volume
                ))


    def load(self, dir):
        onlyfiles = [f for f in listdir(dir) if isfile(join(dir, f))]
        data = []
        for file in onlyfiles:
            filename = '{}/{}'.format(dir, file)
            with open(filename, 'rb') as csvfile:
                data.append(csv.reader(csvfile, delimiter=','))

        return data

    def save_header(self, filename):
        if self.check_exec:
            with open(filename, 'w') as f:
                f.write('{},{},{},{},{}\n'.format(
                    "timestamp",
                    "name",
                    "symbol",
                    "marketcap",
                    "price",
                    "volume"
                ))

    def save_content(self, filename, report):
        if self.check_exec:
            with open(filename, 'a') as f:
                f.write('{},{},{},{},{}\n'.format(
                    report.timestamp,
                    report.name,
                    report.symbol,
                    report.marketcap,
                    report.price,
                    report.volume
                ))

    def save(self, file, reports):
        if self.check_exec:
            for report in reports:
                filename = '{}/{}{}'.format(self.report_dir, report.name, file)
                if not path.isfile(filename):
                    self.save_header(filename)
                self.save_content(filename, report)

    def data_mapping(self, markets, reports):
        for report in reports:
            if report.name not in markets:
                markets[report.name] = []
            markets[report.name].append(report)

            """for key, value in markets.items():
                print(key, value)
                for v in value:
                    print("  ", v)
            """
        return markets