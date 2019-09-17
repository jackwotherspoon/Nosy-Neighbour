# file that builds, trains, and tests the ML model

import pandas as pd
from sklearn.model_selection import train_test_split

# function to split data into training and test sets
def splitData(data):
    x_train, x_test, y_train, y_test = train_test_split(data.drop(columns = ['List Price']), data['List Price'], test_size = 0.2)
    
# function to train model on training set
def train(trainingData):

# function to test model on test set
def test(testData):

# driver code
data = pd.read_csv('cleanedData.csv')
print(data)
splitData(data)