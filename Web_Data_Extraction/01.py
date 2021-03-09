import argparse
import os
import requests as r
import re
from shutil import rmtree
from urllib.parse import urlparse
from bs4 import BeautifulSoup as bs
from functools import reduce

def coalesce(*arg):
    return reduce(lambda x, y: x if x is not None else y, arg)

def init(url, folder):
    links = []
    pattern = re.compile(r'\b[a-zA-Z\ -]{4,}\b')
    u = urlparse(url)
    scn = u.scheme + '://' + u.netloc
    page = r.get(url)
    soup = bs(page.content, 'html.parser')
    folder_name = coalesce(folder, pattern.search(soup.title.string).group(), soup.title.string)
    re.purge()
    for link in soup.find_all('a', class_='sigFreeLink fancybox-gallery'):
        links.append(scn + link.get('href'))
    return links, folder_name

def save_files(links, folder_name):
    pattern = re.compile('[0-9]+')
    fn = folder_name.strip().strip('-').strip()
    if not os.path.isdir(fn):
        os.mkdir(fn)
    else:
        print(f'Directory {fn} has already existed.')
    for i in range(len(links)):
        string = links[i].split('//')[-1]
        res = pattern.search(string).group()
        f_name = os.path.normcase(fn+'/'+res+'.jpg')
        if not os.path.isfile(f_name):
            with open(f_name, 'bw') as f:
                fw = r.get(links[i])
                f.write(fw.content)
                print(f'File {res}.jpg was saved successfully.')
        else:
            print(f'File {res}.jpg has already existed and will not be downloaded.')
    re.purge()
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