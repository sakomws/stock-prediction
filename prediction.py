import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn import preprocessing, svm
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import datetime
import main

# Predict 60 days stock price based on close price
class Prediction:
    def __init__(self):
        self.data = pd.read_csv('Stock_prices_'+main.company+'.csv', parse_dates=True)
        predict_out = int(60)
        self.data['Prediction'] = self.data[['adjclose']].shift(-predict_out)
        X = np.array(self.data.drop(['Date','Prediction'], 1))
        X = preprocessing.scale(X)
        self.X_forecast = X[-predict_out:]
        X = X[:-predict_out]
        y = np.array(self.data['Prediction'])
        y = y[:-predict_out]
        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(X, y, test_size=0.2)

    # Training
    def training_data(self):
        self.clf = LinearRegression()
        self.clf.fit(self.X_train, self.y_train)

    # Testing
    def testing_data(self):
        confidence = self.clf.score(self.X_test, self.y_test)
        self.forecast_prediction = self.clf.predict(self.X_forecast)
        print("confidence: ", int(confidence*100),'%')
        print("Forecast for coming 60 days: ")
        print(main.mark)
        print(self.forecast_prediction)

    # Predicting
    def predict_price(self):
        plt.figure(1)
        plt.subplot(221)
        plt.plot(self.data['adjclose'])
        plt.title('Google Stock Exchange History graph')
        plt.grid(True)
        plt.ylabel('Stock price')
        plt.xlabel('Between:1/2/2008 - 12/29/2017, 2758 days.')
        plt.subplot(222)
        plt.title('Google Stock Exchange Prediction graph')
        plt.grid(True)
        plt.plot(self.forecast_prediction)
        current_date=datetime.datetime.today().strftime('%Y-%m-%d')
        plt.xlabel('Starting from '+str(current_date)+' till coming 60 days.')
        plt.show()