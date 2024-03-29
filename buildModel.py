# file that builds, trains, and tests the ML model

import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

# function to split data into training and test sets
def splitData(data):
    trainData = data.sample(frac=0.8, random_state = 0)
    testData  = data.drop(trainData.index)
    print("Training data shape has x values of %s and y values of shape %s" % (trainData.shape))
    print("Testing data shape has x values of %s and y values of shape %s" % (testData.shape))
    
    return trainData, testData

# function to train model on training set
def train(trainData):
    trainLabels = trainData.pop('List Price')
    # create linear model
    linearModel = LinearRegression()
    linearModel.fit(trainData, trainLabels)
    
    return linearModel

# function to test model on test set
def test(testData, linModel):
    testLabels = testData.pop('List Price')
    actual = testLabels[:1].to_string(index = False)
    predicted = linModel.predict(testData[:1])
    print("Actual price of house is $", actual)
    print("Predicted price of house is $", int(predicted))

# driver code
data = pd.read_csv('cleanedData.csv')
print(data)
trainingData, testingData = splitData(data)
linModel = train(trainingData)
test(testingData, linModel)