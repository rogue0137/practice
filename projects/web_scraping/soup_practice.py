# https://www.digitalocean.com/community/tutorials/how-to-work-with-web-data-using-requests-and-beautiful-soup-with-python-3
from bs4 import BeautifulSoup
import requests

url = 'https://assets.digitalocean.com/articles/eng_python/beautiful-soup/mockturtle.html'
page = requests.get(url)

soup = BeautifulSoup(page.text, 'html.parser')

p = soup.find_all('p')
third_p = p[2].get_text()

chorus = soup.find_all(class_='chorus')
p_chorus = soup.find_all('p', class_='chorus')

third = soup.find_all(id='third')
print(third)