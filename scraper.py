import requests
from bs4 import BeautifulSoup
import pandas as pd

link = "https://www.ottawarealestate.ca/search/details/no/4/"
page = requests.get(link, timeout = 5)
content = BeautifulSoup(page.content, "html.parser")
content.prettify()
textContent = content.find_all('div', attrs = {"class":"prop-descrip"})
filtered = []
featureNames = [items.dt.get_text() for items in textContent]
featureValues = [items.dd.get_text() for items in textContent]  
data = pd.DataFrame({
    "featureNames": featureNames,
    "featureValues": featureValues
})
print(data)