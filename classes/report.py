import csv
from datetime import datetime
from os import listdir, path
from os.path import isfile, join

class Report:
    def __init__(self, default):
        self.report_dir = default.get("report_dir")
        self.file = default.get("file")
        self.file_bool = default.get("file_bool")
        self.data = {}

    def check_exec(self):
        if self.file_bool in ('True', True):
            return True
        return False

    def display(self):
        for report in self.data:
            print("report.display",report)

    def get(self):
        onlyfiles = [f for f in listdir(self.report_dir) if isfile(join(self.report_dir, f))]
        data = {}
        for file in onlyfiles:
            filename = '{}/{}'.format(self.report_dir, file)
            name = file.split(self.file)[0]
            data[name] = []

            print("report.get", name, filename)

            with open(filename, 'rb') as csvfile:
                reader = csv.DictReader(csvfile, delimiter=',')
                for line in reader:
                    data[name].append(line)
        return data

    def save_header(self, filename):
        if self.check_exec:
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
        if self.check_exec:
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
        self.data = reports

        if self.check_exec:
            for report in self.data:
                filename = '{}/{}{}'.format(self.report_dir, report.get("name"), self.file)
                if not path.isfile(filename):
                    self.save_header(filename)
                self.save_content(filename, report)
