import requests
from bs4 import BeautifulSoup

link = 'https://www.ottawarealestate.ca/search/details/no/4/' 
response = requests.get(link, timeout = 5).text
content = BeautifulSoup(response, "html.parser")
textContent = content.findAll('div', attrs = {"class":"prop-descrip"})
print(textContent)
