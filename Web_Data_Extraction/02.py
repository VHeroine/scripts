import argparse
import os
import requests as r
import re
from bs4 import BeautifulSoup as bs

PARAMS={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36'}

def init(url, folder):
    """   """
    links = []
    links_dict = {}
    pattern = re.compile(r'\b[a-zA-Z\ ]{4,}\b')
    page = r.get(url=url, params=PARAMS)
    soup = bs(page.content, 'html.parser')
    for folder_name in (folder, pattern.search(soup.title.string).group(), soup.title.string):
        if folder_name is not None:
            break
    re.purge()
    for link in soup.find_all('div', class_='photo-item', attrs={"itemtype":"http://schema.org/ImageObject"}):
        for a in link.find_all('a'):
            links.append(a.get('href'))
    for i in range(len(links)):
        links_dict[str(i+1).zfill(2) + ('.jpg')] = links[i]
    return links_dict, folder_name

def save_files(links, folder_name):
    """   """
    fn = folder_name.strip()
    if not os.path.isdir(fn):
        os.mkdir(fn)
    else:
        print(f'Directory {fn} has already existed.')
    for key, url in links.items():
        page = r.get(url)
        soup = bs(page.content, 'html.parser')
        link = soup.find('a', class_='full-size-photo').get('href')
        f_name = os.path.normcase(fn + '/' + key)
        if not os.path.isfile(f_name):
            with open(f_name, 'bw') as f:
                fw = r.get(link)
                f.write(fw.content)
                print(f'File {key} was saved successfully.')
        else:
            print(f'File {key} has already existed and will not be downloaded.')

def main():
    """   """
    parser = argparse.ArgumentParser(description='Web scraper')
    parser.add_argument('url', type=str, help='url to download images')
    parser.add_argument('folder', type=str, help='folder name', nargs='?', default=None)
    args = parser.parse_args()
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    links, folder_name = init(args.url, args.folder)
    save_files(links, folder_name)
    print('The program has been successfully completed.')

if __name__ == '__main__':
    """ Launch the main process. """
    main()