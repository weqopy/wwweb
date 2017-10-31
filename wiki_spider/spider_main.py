import html_downloader
import html_outputer
import html_parser
import url_manager


class SpiderMain(object):
    """docstring for SpiderMain"""

    def __init__(self):
        # 引入相应模块中的类
        self.urls = url_manager.UrlManager()
        self.downloader = html_downloader.HtmlDownLoader()
        self.parser = html_parser.HtmlParser()
        self.outputer = html_outputer.HtmlOutputer()

    def craw(self, root_url):
        # 爬取页面数量
        count = 1
        self.urls.get_new_url(root_url)
        while self.urls.has_new_url():
            try:
                new_url = self.urls.get_new_url(root_url)
                # 显示当前爬取数、链接
                print('Craw {}: {}'.format(count, new_url))
                # 下载页面
                html_cont = self.downloader.download(new_url)
                # 解析页面
                new_urls, new_data = self.parser.parse(new_url, html_cont)
                # 将新页面中的新链接存入 urls
                self.urls.add_new_urls(new_urls)
                self.outputer.collect_data(new_data)

                if count == 10:
                    break
                count += 1
            except:
                print('Craw failed at {}: {}'.format(count, new_url))
        # 输出
        self.outputer.out_html()


if __name__ == '__main__':
    root_url = 'https://en.wikipedia.org/wiki/Python_(programming_language)'
    obj_spider = SpiderMain()
    obj_spider.craw(root_url)
