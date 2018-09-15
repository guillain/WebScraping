import re
import time
import bs4
import requests

class Scraping:
    def __init__(self, conf):
        self.conf = conf
        self.debug("scraping", "__init__")
        self.data = []

    def get_html(self):
        self.debug("scraping", "get_html")
        response = requests.get(self.conf['collect_url'])
        return response.text

    def get(self, html, limit):
        self.debug("scraping", "get")

        timestamp = time.gmtime()
        soup = bs4.BeautifulSoup(html, 'html.parser')
        table = soup.find(id='currencies-all')
        table_body = table.find('tbody')
        rows = table_body.find_all('tr')
        index = 0

        for row in rows:
            data = {}
            data["timestamp"] = time.strftime('%Y-%m-%d %H:%M:%S', timestamp)
            data["name"] = self.cleanup_text(row.find(class_='currency-name').get_text())
            data["symbol"] = self.cleanup_text(row.find(class_='currency-symbol').get_text())
            data["marketcap"] = self.cleanup_text(row.find(class_='market-cap').get_text())
            data["price"] = self.cleanup_text(row.find(class_='price').get_text())
            data["volume"] = self.cleanup_text(row.find(class_='volume').get_text())

            self.data.append(data)

            index = index + 1
            if index > limit:
                return self.data
        return self.data

    def cleanup_text(self, text):
        if not text:
            return text

        text = re.sub('[^A-Za-z0-9\.]+', '', text)

        return text

    def display(self):
        self.debug("scraping", "display")
        for line in self.data:
            print("scraping.display", line)

    def debug(self, clas, fct, data = None):
        if self.conf['debug']:
            print(">>>>>", clas, " - ", fct, " - ", data)