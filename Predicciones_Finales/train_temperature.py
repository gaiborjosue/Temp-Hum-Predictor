from sklearn.model_selection import train_test_split
import pandas as pd
import numpy as numpy
import matplotlib.pyplot as plt
from sklearn import linear_model
import joblib

df = pd.read_csv(
    "Predicciones_Finales\\Data\\th_station_3rd_data.csv", delimiter=",")

x = df[["field2"]]
y = df[["field1"]]

X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.3)

reg_2 = linear_model.LinearRegression()
reg_2.fit(X_train, y_train)

joblib.dump(reg_2, 'Predicciones_Finales\\Models\\3rd_release\\temp_predictor.joblib')

# predict_hum = reg.predict(X_test)
# print(predict_hum)

# from sklearn.metrics import r2_score
# print(r2_score(predict_hum, y_test))
