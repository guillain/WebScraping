import re
from datetime import datetime
import bs4
import requests
import collections

class Scraping:
    def __init__(self, default):
        self.CollectName = default.get("collect_name")
        self.CollectUrl = default.get("collect_url")

    def get_html(self):
        response = requests.get(self.CollectUrl)
        return response.text

    def get_reports(self, html, limit):
        reports = []
        timestamp = datetime.now()
        soup = bs4.BeautifulSoup(html, 'html.parser')
        table = soup.find(id='currencies-all')
        table_body = table.find('tbody')
        rows = table_body.find_all('tr')
        index = 0

        CollectReport = collections.namedtuple(self.CollectName,
                                                    'timestamp, name, symbol, marketcap, price, volume')
        for row in rows:
            reports.append(
                CollectReport(
                    timestamp=timestamp,
                    name=self.cleanup_text(row.find(class_='currency-name').get_text()),
                    symbol=self.cleanup_text(row.find(class_='currency-symbol').get_text()),
                    marketcap=self.cleanup_text(row.find(class_='market-cap').get_text()),
                    price=self.cleanup_text(row.find(class_='price').get_text()),
                    volume=self.cleanup_text(row.find(class_='volume').get_text())
                )
            )
            index = index + 1
            if index > limit:
                return reports
        return reports

    def cleanup_text(self, text):
        if not text:
            return text

        text = re.sub('[^A-Za-z0-9]+', '', text)

        """text = text.strip()
        text = text.replace('$','')
        text = text.replace(',','')
        text = text.replace(' ', '_')
        text = text.replace('\\', '')
        text = text.replace('/', '')
        text = text.replace('\n', '')
        """

        return text