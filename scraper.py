# example web scraping for getting housing data 

import requests
from bs4 import BeautifulSoup
import pandas as pd

def scrape(url, tag, classDescription, dataset):
    page = requests.get(url, timeout = 5)
    if (page.status_code == 200):
        content = BeautifulSoup(page.content, "html.parser")
        content.prettify()
        textContent = content.find_all(tag, attrs = {"class": classDescription})
        featureNames = [items.dt.get_text() for items in textContent]
        featureValues = [items.dd.get_text() for items in textContent]
        dataset = dataset.append(pd.DataFrame([featureValues], columns = featureNames, index = [0]), ignore_index = True)
        return dataset
    else:
        print("ERROR: Page request was unsuccessful.")

# create dataframe and run function to grow dataframe
data = pd.DataFrame([])

# successful function call
data = scrape("https://www.ottawarealestate.ca/search/details/no/10/", "div", "prop-descrip", data)
data = scrape("https://www.ottawarealestate.ca/search/details/no/9/", "div", "prop-descrip", data)
print(data)

# failure function call
scrape("https://www.garbage.com/url", "div", "prop-descrip", data)
