from icrawler.builtin import GoogleImageCrawler
import resizer
import os

classes=['3m particulate respirator white','blue butyl gloves','industrial safety shoe']

for label in classes:
    '''google_crawler = GoogleImageCrawler(parser_threads=2, downloader_threads=4,storage={'root_dir': label })
    google_crawler.crawl(keyword=label , max_num=200,date_min=None, date_max=None,min_size=(100,100), max_size=None)
    '''
    resizer.rezz(label)
