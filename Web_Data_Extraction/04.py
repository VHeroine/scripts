import argparse
import os
from urllib.parse import urlparse, urlunparse
import requests as r
import re
from bs4 import BeautifulSoup as bs
from functools import reduce

def coalesce(*arg):
    return reduce(lambda x, y: x if x is not None else y, arg)

def init(url, folder):
    links = []
    links_dict = {}
    pattern = re.compile(r'\b[a-zA-Z\ -]{4,}\b')
    u = urlparse(url).netloc
    PARAMS={'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9'
           ,'Accept-Encoding': 'gzip, deflate, br'
           ,'Accept-Language': 'ru,en;q=0.9,en-GB;q=0.8,en-US;q=0.7'
           ,'Cache-Control': 'max-age=0'
           ,'Connection': 'close'
           ,'Sec-Fetch-Dest': 'document'
           ,'Sec-Fetch-Mode': 'navigate'
           ,'Sec-Fetch-Site': 'none'
           ,'Sec-Fetch-User': '?1'
           ,'Upgrade-Insecure-Requests': 1
           ,'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36 Edg/89.0.774.50'
           ,
           }
    page = r.get(url=url, params=PARAMS)
    soup = bs(page.content, 'html.parser')
    folder_name = coalesce(folder, pattern.search(soup.title.string).group(), soup.title.string)
    re.purge()
    div = soup.find('div', class_='list-justified-container')
    for a in div.find_all('a'):
        t = list(urlparse(a.get('href')))
        t[1] = u
        links.append(urlunparse(t))
    for i in range(len(links)):
        links_dict[str(i+1).zfill(4) + ('.jpg')] = links[i]
    return links_dict, folder_name

def save_files(links, folder_name):
    fn = folder_name.strip()
    if not os.path.isdir(fn):
        os.mkdir(fn)
    else:
        print(f'Directory {fn} has already existed.')
    for file_name, url in links.items():
        f_name = os.path.normcase(fn+'/'+file_name)
        if not os.path.isfile(f_name):
            with open(f_name, 'bw') as f:
                fw = r.get(url)
                f.write(fw.content)
                print(f'File {file_name} was saved successfully.')
        else:
            print(f'File {file_name} has already existed and will not be downloaded.')
    return None

def main():
    parser = argparse.ArgumentParser(description='Web scraper')
    parser.add_argument('url', type=str, help='url to download images')
    parser.add_argument('folder', type=str, help='folder name', nargs='?', default=None)
    args = parser.parse_args()
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    links, folder_name = init(args.url, args.folder)
    save_files(links, folder_name)
    print('The program has been successfully completed.')
    return None

if __name__ == '__main__':
    main()