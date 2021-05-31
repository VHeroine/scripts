import argparse
import os
import requests
import re
from urllib.parse import urlparse
from bs4 import BeautifulSoup as bs

PARAMS = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36'}

def init(url, folder):
    """  """
    links = []
    pattern = re.compile(r'\b[a-zA-Z\ -]{4,}\b')
    u = urlparse(url)
    scn = u.scheme + '://' + u.netloc
    page = requests.get(url=url, params=PARAMS)
    soup = bs(page.content, 'html.parser')
    for _ in (folder, pattern.search(soup.title.string).group(), soup.title.string):
        folder_name = _
        if folder_name is not None:
            break
    re.purge()
    for link in soup.find_all('a', class_='sigFreeLink fancybox-gallery'):
        links.append(scn + link.get('href'))
    return links, folder_name

def save_files(links, folder_name):
    """  """
    pattern = re.compile('[0-9]+')
    norm_folder_name = folder_name.strip().strip('-').strip()
    if not os.path.isdir(norm_folder_name):
        os.mkdir(norm_folder_name)
    else:
        print(f'Directory {norm_folder_name} has already existed.')
    for link in links:
        string = link.split('//')[-1]
        name = pattern.search(string).group().zfill(3)
        file_name = os.path.normcase(norm_folder_name+'/'+name+'.jpg')
        if not os.path.isfile(file_name):
            with open(file_name, 'bw') as f:
                file_content = requests.get(link)
                f.write(file_content.content)
                print(f'File {name}.jpg was saved successfully.')
        else:
            print(f'File {name}.jpg has already existed and will not be downloaded.')
    re.purge()

def main():
    """  """
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