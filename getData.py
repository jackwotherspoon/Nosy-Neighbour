# file that web scrapes pages to extract data and then properly formats it to be used by the ML model

import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np

# function to scrape web page for listing details and return dictionary
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

# function to iterate through web pages and extra house listing details
def generateData(size):
    # initialize empty list to store data
    data = []
    for i in range(0, size):
        # loop through different pages of house listings and add to data
        link = "https://www.ottawarealestate.ca/search/details/no/{}/".format(i)
        data.append(scrape(link, "div", "prop-descrip"))
    return data

# function to extract list of all feature names from all pages to be used as columns for dataset
def getFeatures(data):
    # since not all listings have uniform feature details we need to extract every feature name to compare missing data
    allFeatures = []    
    for i in range(0, len(data)):
        features = [*data[i]]
        for feature in features:
            if feature not in allFeatures:
                allFeatures.append(feature)
    return allFeatures

# function to replace missing fields of dataframe with NULL 
def formatData(featureNames, data):
    # loop through data and fill in missing fields with NULL
    for i in range(0, len(data)):
        features = [*data[i]]
        for feature in featureNames:
            if feature not in features:
                data[i][feature] = "NULL"
    return data

# function that checks currently saved CSV and adds data that isn't already in it
def createCSV(data):
    oldData = pd.read_csv('houseData.csv')
    oldData['MLS® #'] = oldData['MLS® #'].astype(str)
    mergedData = pd.concat([data, oldData], ignore_index= True)
    mergedData = mergedData.drop_duplicates(subset = "MLS® #", keep = 'first')
    CSV = data.to_csv(r'houseData.csv', index = None)

# driver code
data = generateData(15)
featureNames = getFeatures(data)
data = formatData(featureNames, data)
data = pd.DataFrame(data)
print(data)
createCSV(data)
