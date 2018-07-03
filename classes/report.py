import os

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
        for report in reports:
            print('{} \t {} \t {} \t {} \t {} \t {}'.format(
                report.timestamp.strftime("%Y-%m-%d %H:%M:%S"),
                report.name,
                report.symbol,
                report.marketcap,
                report.price,
                report.volume
            ))

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
        print(filename, report)
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
                if not os.path.isfile(filename):
                    self.save_header(filename)
                self.save_content(filename, report)
