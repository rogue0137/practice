# https://www.digitalocean.com/community/tutorials/how-to-scrape-web-pages-with-beautiful-soup-and-python-3

import requests
from bs4 import BeautifulSoup 
import csv

# create CSV file
f = csv.writer(open('z-artist-names.csv', 'w'))
f.writerow(['Name','Link'])

# create my header
headers = {
    'User-Agent': 'Krys Flores, web scraping practice',
    'From': 'https://krysflores.com/contact'
}

pages = []

for i in range(1, 5):
    url = 'https://web.archive.org/web/20121007172955/https://www.nga.gov/collection/anZ' + str(i) + '.htm'
    pages.append('url') 


for item in pages:
    page = requests.get(url, headers = headers)

    # BeautifulSoup Object!
    soup = BeautifulSoup(page.text, 'html.parser')

    # Remove bottom links
    last_links = soup.find(class_='AlphaNav')
    last_links.decompose()

    # pull text from BodyText div
    artist_name_list = soup.find(class_='BodyText')

    # pull text from all <a> tags w/in BodyText div
    artist_name_list_items = artist_name_list.find_all('a')

    for artist_name in artist_name_list_items:
        name = artist_name.contents[0]
        link = 'http://web.archive.org' + artist_name.get('href')
        f.writerow([name, link])
