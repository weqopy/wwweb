from bs4 import BeautifulSoup as bs
import re


class HtmlParser(object):

    def _get_new_urls(self, page_url, soup):
        root_url_basic = 'https://en.wikipedia.org'
        new_urls = set()
        links = soup.find_all('a', href=re.compile('^/wiki'))
        for link in links:
            # 排除图片链接
            if not re.search('\.(jpg|JPG)$', link['href']):
                new_url = link['href']
                new_full_url = root_url_basic + new_url
                new_urls.add(new_full_url)
        return new_urls

    def _get_new_data(self, page_url, soup):
        res_data = {}

        res_data['url'] = page_url

        # 通过 Chrome 获得 XPath 结构
        # //*[@id="firstHeading"]
        title_node = soup.find('h1', class_='firstHeading')
        res_data['title'] = title_node.text

        # //*[@id="mw-content-text"]/div/p[1]
        summary_node_b = soup.find('div', class_='mw-parser-output')
        # 避免"AttributeError: 'NoneType' object has no attribute 'text' & 'find' "错误
        # TODO: 上述错误在此处避免，但输出到文件中时仍然会报错
        if summary_node_b is not None:
            summary_node = summary_node_b.find('p')
            if summary_node is not None:
                res_data['summary'] = summary_node.text

        return res_data

    def parse(self, page_url, html_cont):
        if page_url is None or html_cont is None:
            return None

        soup = bs(html_cont, 'lxml')
        if soup is not None:
            new_urls = self._get_new_urls(page_url, soup)
            new_data = self._get_new_data(page_url, soup)

        return new_urls, new_data
