# file that cleans and preprocesses data in order to be used effectively by the ML model
import pandas as pd

# function to clean data
def clean(data):
    # drop unneeded columns from dataframe
    newData = data.drop(columns = ['MLS® #', 'Status', 'Subtype', 'Country', 'Community Features'], axis = 1)
    return newData

data = pd.read_csv('houseData.csv')
data = clean(data)
print(data)
