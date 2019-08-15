# example web scraping for getting housing data 

import requests
from bs4 import BeautifulSoup
import pandas as pd

def scrape(url, tag, classDescription):
    page = requests.get(url, timeout = 5)
    if (page.status_code == 200):
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
    else:
        print("ERROR: Page request was unsuccessful.")

# successful function call
scrape("https://www.ottawarealestate.ca/search/details/no/4/", "div", "prop-descrip")

# failure function call
scrape("https://www.garbage.com/url", "div", "prop-descrip")