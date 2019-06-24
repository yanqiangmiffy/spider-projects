import re
from bs4 import BeautifulSoup
from urllib.parse import urljoin

class HtmlParser(object):

    def _get_new_urls(self, page_url, soup):
        pass


    def _get_new_data(self, page_url, soup):
        '''
        返回res_data,res_data是字典数据，
        包含url, title, datetime, visitcount这四个键
        '''
        pass
    
    def parse(self, page_url, html_cont):
        if page_url is None or html_cont is None:
            return 
        
        soup = BeautifulSoup(html_cont, 'html.parser', from_encoding='utf-8')
        new_urls = self._get_new_urls(page_url, soup)
        new_data = self._get_new_data(page_url, soup)
        return new_urls, new_data