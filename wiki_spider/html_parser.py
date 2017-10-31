from bs4 import BeautifulSoup as bs
import re
# import spider_main


class HtmlParser(object):

    def _get_new_urls(self, page_url, soup):
        root_url_basic = 'https://en.wikipedia.org'
        new_urls = set()
        links = soup.find_all('a', href=re.compile('^/wiki'))
        for link in links:
            if not re.search('\.(jpg|JPG)$', link['href']):
                new_url = link['href']
            new_full_url = root_url_basic + new_url
            new_urls.add(new_full_url)
        return new_urls

    def _get_new_data(self, page_url, soup):
        res_data = {}

        res_data['url'] = page_url

        # //*[@id="firstHeading"]
        title_node = soup.find('h1', class_='firstHeading')
        res_data['title'] = title_node.text

        # //*[@id="mw-content-text"]/div/p[1]
        summary_node = soup.find('div', class_='mw-parser-output').find('p')
        res_data['summary'] = summary_node.text

        return res_data

    def parse(self, page_url, html_cont):
        if page_url is None or html_cont is None:
            return None

        soup = bs(html_cont, 'lxml')
        new_urls = self._get_new_urls(page_url, soup)
        new_data = self._get_new_data(page_url, soup)
        return new_urls, new_data
