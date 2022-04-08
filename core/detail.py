import lxml
from lxml import html
import os
import requests
from enum import Enum
from utils.utils import(
    sizeof_fmt
)


class detailType:
    DIRECTORY = 1
    FILE = 2
    VIDEO = 3
    AUDIO = 4
    UNKNOW = 0


class detailLink(object):
    def __init__(self, data, url):
        self.data = data
        self.url = url
        self.type = None
        self.link = None
        self.title = None
        self.size = None
        self.parser()
    def get_content_length(self):
        if not self.type in (detailType.AUDIO, detailType.VIDEO):
            return False
        try:
            r = requests.head(self.link)
            self.size = sizeof_fmt(int(r.headers.get('Content-Length', 0)))
        except Exception as err:
            print('Exception get content length ... {}'.format(err))
    def parser(self):
        type_apache = self.data.xpath('./td')[0].xpath('./img')[0].attrib['alt'].replace('[', '').replace(']', '')
        if type_apache == 'VID':
            self.type = detailType.VIDEO
        elif type_apache == 'DIR':
            self.type = detailType.DIRECTORY
        else:
            self.type = detailType.UNKNOW
        self.title = self.data.xpath('./td')[1].text_content()
        self.link = os.path.join(self.url, self.title)
        if self.type in (detailType.AUDIO, detailType.VIDEO):
            self.get_content_length()




class detailApacheFolder(object):
    def __init__(self, url):
        self.url = url
        self.archives = []
        self.get_details_folder()
    def get_details_folder(self):
        try:
            r = requests.get(self.url)
            x = lxml.html.fromstring(r.text)
            t = x.xpath('//table/tr')
            for td in t:
                if len(td.xpath('./td')) > 0:
                    if td.xpath('./td')[0].xpath('./img')[0].attrib['alt'].replace('[', '').replace(']', '') in ['VID', 'DIR']:
                        self.archives.append(detailLink(td, self.url))
        except Exception as err:
            print('Exception obtain details folder ... {}'.format(err))



