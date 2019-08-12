import requests
from bs4 import BeautifulSoup
import pandas as pd

def scrape(url, tag, classDescription):
    page = requests.get(url, timeout = 5)
    content = BeautifulSoup(page.content, "html.parser")
    content.prettify()
    textContent = content.find_all(tag, attrs = {"class": classDescription})
    featureNames = [items.dt.get_text() for items in textContent]
    featureValues = [items.dd.get_text() for items in textContent]  
    data = pd.DataFrame({
        "featureNames": featureNames,
        "featureValues": featureValues
    })
    print(data)

scrape("https://www.ottawarealestate.ca/search/details/no/4/", "div", "prop-descrip")