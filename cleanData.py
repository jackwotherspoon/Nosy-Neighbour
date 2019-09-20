# file that cleans and preprocesses data in order to be used effectively by the ML model
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# function to clean data
def clean(data):
    # drop unneeded columns from dataframe (TODO: Find way to get 'Lot Size' back in dataset)
    newData = data.drop(columns = ['MLS® #', 'Lot Size', 'Status', 'Subtype', 'Country', 'Community Features', 'Heating', 'Sewer', 'Frontage Length', 'Flooring', 'Fencing', 'Architectural Style', 'View', 'Ownership', 'Lot Features', 'Construction Materials', 'Attached Garage', 'Levels'], axis = 1)
   
    # need to perform multivariable analysis as features are categorical and numerical
    categorical = newData.select_dtypes(include = ['object']).columns
    numerical   = newData.select_dtypes(include = ['int64', 'float64']).columns
    print("The categorical features are: ", list(categorical))
    print("The numerical features are: ", list(numerical))
    cat = len(categorical)
    num = len(numerical)
    print('Total features: %d features (%d categorical + %d numerical)' % (cat+num, cat, num))

    # correlation matrix heatmap for numerical features
    corrmat = newData.corr()
    f, ax = plt.subplots(figsize = (12,9))
    sns.heatmap(corrmat, vmax =.8, square = True)
    # plt.show()

    # call missing data function on data
    missingData(newData)
    
    # fill in missing data fields
    newData['Pool'] = newData['Pool'].fillna('No')
    newData['Waterfront'] = newData['Waterfront'].fillna('No')
    newData['Fireplaces'] = newData['Fireplaces'].fillna('0')
    newData['Parking Spaces'] = newData['Parking Spaces'].fillna('0')
    newData['Garage'] = newData['Garage'].fillna('No')
    storiesMedian = newData['Stories'].median() # compute median for number of stories in the data set
    newData['Stories'] = newData['Stories'].fillna(storiesMedian) # fill missing stories field with median
    newData['Cooling'] = newData['Cooling'].fillna('Central air conditioning') # fill missing cooling data with most common result
    
    # call missing data function again to compare to previous time
    missingData(newData)

    # convert columns with yes/no entries to 0 and 1s
    newData['Pool'] = newData['Pool'].map(dict(Yes=1, No=0))
    newData['Garage'] = newData['Garage'].map(dict(Yes=1, No=0))
    newData['Waterfront'] = newData['Waterfront'].map(dict(Yes=1, No=0))
    
    return newData

# function that calculates percentage of missing data in each column
def missingData(data):
    data_na = (data.isnull().sum() / len(data)) * 100
    data_na = data_na.drop(data_na[data_na == 0].index).sort_values(ascending = False)[:len(data)]
    missing = pd.DataFrame({'Missing Data Percentage' : data_na})
    print(missing)
    return missing

# driver code
data = pd.read_csv('houseData.csv')
data = clean(data)
data.to_csv(r'cleanedData.csv', index = None)
print(data)
