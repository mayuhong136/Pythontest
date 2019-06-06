import urllib.request
from bst import BeautifulSoup

class Scraper:
    def _init_(self,site):
      self.site = site
    def scrape(self):
        r = urllib.request.urlopen(self.site)
        html = r.read()
        parser = "html.parser"
        sp = BeautifulSoup(html,parser)
        for tag in sp.find_all("a")
             url = tag.get("href")
             if url is None:
                  continue
             if "html" in url:
                  print("\n" + url)
news = "https://news.baidu.com/"
Scraper(news).scrape()
