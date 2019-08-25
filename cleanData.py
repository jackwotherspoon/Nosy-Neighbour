# file that cleans and preprocesses data in order to be used effectively by the ML model
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# function to clean data
def clean(data):
    # drop unneeded columns from dataframe
    newData = data.drop(columns = ['MLS® #', 'Status', 'Subtype', 'Country', 'Community Features', 'Heating', 'Sewer', 'Frontage Length', 'Flooring', 'Fencing', 'Architectural Style', 'View', 'Ownership'], axis = 1)
   
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
    plt.show()
    missingData(newData)
    return newData

# function that calculates percentage of missing data in each column
def missingData(data):
    data_na = (data.isnull().sum() / len(data)) * 100
    data_na = data_na.drop(data_na[data_na == 0].index).sort_values(ascending = False)[:len(data)]
    missing = pd.DataFrame({'Missing Data Percentage' : data_na})
    print(missing)
    return missing

data = pd.read_csv('houseData.csv')
data = clean(data)
#print(data)
#print(data.dtypes)
