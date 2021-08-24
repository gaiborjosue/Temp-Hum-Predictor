import joblib
import argparse
from numpy import real
import requests

temp_predictor = joblib.load('Predicciones_Finales\\Models\\temp_predictor.joblib')

get_data_1 = requests.get(
    "https://api.thingspeak.com/channels/1439127/fields/1.json?api_key=KDZ8NQ5X5GQBLD62&results=1")

get_data_2 = requests.get(
    "https://api.thingspeak.com/channels/1439127/fields/2.json?api_key=KDZ8NQ5X5GQBLD62&results=1")
    
data_f1 = get_data_1.json()
data_f2 = get_data_2.json()

temp_field_data = [data_f1['feeds'][0]['field1']]

hum_field_data = [data_f2['feeds'][0]['field2']]

temp_field_data = [float(i) for i in temp_field_data] #  convert with for loop
predict_temp = temp_predictor.predict([hum_field_data])

predicted_value = int(predict_temp[0][0])
real_value = int(float(temp_field_data[0]))

if predicted_value == real_value:
    print("Exito! El algoritmo predijo el valor real de humedad!")
    print(f"El valor que predijo el algoritmo es: {predicted_value}")
    print(f"El valor real es: {real_value}")

if predicted_value != real_value:
    res_1 = (predicted_value * 100) / real_value
    if res_1 > 100:
        dif_percent = res_1 - 100
        dif_percent_res = 100 - dif_percent
        print(f"El porcentaje de Precisión del valor estimado es: {dif_percent_res}")

    print(f"El valor que predijo el algoritmo es: {predicted_value}")
    print(f"El valor real es: {real_value}")
    print(f"La diferencia es de {abs(predicted_value-real_value)}")