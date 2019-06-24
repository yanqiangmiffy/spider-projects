import urls_manager, html_downloader, \
    html_parser, html_outputer

class SpiderMain(object):

    def __init__(self):
        self.urls = urls_manager.UrlManager()
        self.downloader = html_downloader.HtmlDownloader()
        self.parser = html_parser.HtmlParser()
        self.outputer = html_outputer.HtmlOutputer()

    def craw(self, root_url):
        '''
        循环爬取新闻页面，可以设置爬取100页结束
        '''
        pass



if __name__ == '__main__':
    root_url = 'http://news.zzuli.edu.cn/'
    obj_spider = SpiderMain()
    obj_spider.craw(root_url)