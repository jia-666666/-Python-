from proxypool.crawlers.base import BaseCrawler
from proxypool.schemas.proxy import Proxy
import re
from pyquery import PyQuery as pq


BASE_URL = 'https://www.kuaidaili.com/free/inha/{page}/'


class KuaidailiCrawler(BaseCrawler):
    """
    kuaidaili crawler, https://www.kuaidaili.com/
    """
    urls = [BASE_URL.format(page=page) for page in range(1, 200)]
    
    def parse(self, html):
        """
        parse HTML file to get proxies
        :return:
        """
        doc = pq(html)
        for item in doc('table tr').items():
            td_ip = item.find('td[data-title="IP"]').text()
            td_port = item.find('td[data-title="PORT"]').text()
            if td_ip and td_port:
                yield Proxy(host=td_ip, port=td_port)


if __name__ == '__main__':
    crawler = KuaidailiCrawler()
    for proxy in crawler.crawl():
        print(proxy)
