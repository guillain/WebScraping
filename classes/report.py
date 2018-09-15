import csv
from os import listdir, path
from os.path import isfile, join
from classes.standard import Standard


class Report(Standard):
    def __init__(self, default, argv):
        Standard.__init__(self, default, argv)

        self.debug("report", "__init__")

        self.files = {}

    def display(self):
        self.debug("report", "display")

        for report in self.data:
            print("report.display",report)

    def get(self):
        self.debug("report", "get")

        file_list = self.get_file_list()
        for name in file_list:
            self.data[name] = []
            with open(file_list[name][0], 'rt') as csvfile:
                reader = csv.DictReader(csvfile, delimiter=',')
                for line in reader:
                    line_data = {}
                    line_data['timestamp'] = line.get("timestamp")
                    line_data['name'] = line.get("name")
                    line_data['symbol'] = line.get("symbol")
                    line_data['marketcap'] = line.get("marketcap")
                    line_data['price'] = float(line.get("price"))
                    line_data['volume'] = float(line.get("volume"))
                    self.data[name].append(line_data)
        return self.data

    def display_file_list(self):
        self.debug("report", "display_file_list")

        files = self.get_file_list()
        for file in files:
            print("report.display_file_list",file, files[file][0])

    def get_file_list(self):
        self.debug("report", "get_file_list")

        onlyfiles = [f for f in listdir(self.conf['report_dir']) if isfile(join(self.conf['report_dir'], f))]
        self.files = {}
        for file in onlyfiles:
            filename = '{}/{}'.format(self.conf['report_dir'], file)
            name = file.split(self.conf['file'])[0]
            if name  not in self.files:
                self.files[name] = []
            self.files[name].append(filename)
        return self.files

    def save_header(self, filename):
        self.debug("report", "save_header")

        if self.conf['save_file']:
            with open(filename, 'w') as f:
                f.write('{},{},{},{},{},{}\n'.format(
                    "timestamp",
                    "name",
                    "symbol",
                    "marketcap",
                    "price",
                    "volume"
                ))

    def save_content(self, filename, report):
        self.debug("report", "save_content")

        if self.conf['save_file']:
            with open(filename, 'a') as f:
                f.write('{},{},{},{},{},{}\n'.format(
                    report.get("timestamp"),
                    report.get("name"),
                    report.get("symbol"),
                    report.get("marketcap"),
                    report.get("price"),
                    report.get("volume")
                ))

    def save(self, reports):
        self.debug("report", "save")

        self.data = reports

        if self.conf['save_file']:
            for report in self.data:
                filename = '{}/{}{}'.format(self.conf['report_dir'], report.get("name"), self.conf['file'])
                if not path.isfile(filename):
                    self.save_header(filename)
                self.save_content(filename, report)