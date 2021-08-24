import requests
import csv

get_data_1 = requests.get(
    "https://api.thingspeak.com/channels/1439127/fields/1.json?api_key=KDZ8NQ5X5GQBLD62&results=1")
get_data_2 = requests.get(
    "https://api.thingspeak.com/channels/1439127/fields/2.json?api_key=KDZ8NQ5X5GQBLD62&results=10")

data_f1 = get_data_1.json()
data_f2 = get_data_2.json()

temp_field_data = [data_f1['feeds'][0]['field1']]

hum_field_data = [data_f2['feeds'][0]['field2']]

with open("th_data.csv", "a", newline="") as f:
    tupl = temp_field_data[0], hum_field_data[0]
    csv_writer = csv.writer(f, delimiter=",")
    csv_writer.writerow(tupl)
    f.close()

import pandas as pd
import numpy as numpy
import matplotlib.pyplot as plt
from sklearn import linear_model

df = pd.read_csv("th_data.csv", delimiter=',')

cdf = df[["TEMPERATURE", "HUMIDITY"]]

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(df[["HUMIDITY"]], df[["TEMPERATURE"]], test_size=0.2)
reg = linear_model.LinearRegression()
reg.fit(X_train, y_train)

predict_temp = reg.predict(df[["HUMIDITY"]])
print(predict_temp)

from sklearn.metrics import r2_score
print(r2_score(predict_temp, y_test))