# example web scraping for getting housing data 

import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np

def scrape(url, tag, classDescription):
    page = requests.get(url, timeout = 5)
    if (page.status_code == 200):
        content = BeautifulSoup(page.content, "html.parser")
        content.prettify()
        textContent = content.find_all(tag, attrs = {"class": classDescription})
        featureNames = [items.dt.get_text() for items in textContent]
        featureValues = [items.dd.get_text() for items in textContent]
        dataset = dict(zip(featureNames, featureValues))
        return dataset
    else:
        print("ERROR: Page request was unsuccessful.")

def generateData(size):
    # initialize empty list to store data
    data = []
    for i in range(0, size):
        # loop through different pages of house listings and add to data
        link = "https://www.ottawarealestate.ca/search/details/no/{}/".format(i)
        data.append(scrape(link, "div", "prop-descrip"))
    return data

# driver code
data = generateData(5)
