import tkinter
import joblib
import os
import sklearn

ventana = tkinter.Tk()
ventana.title("Predictor del Clima")
ventana.geometry("400x400")

etiqueta = tkinter.Label(ventana)
etiqueta.pack(pady=40)

cajaTexto = tkinter.Entry(ventana)
cajaTexto.insert(1, "Ingresa tu valor de temperatura.")
cajaTexto.pack(fill='x', padx=50)

def textoDeHumedad():
    hum_predictor = joblib.load(rf"{os.getcwd()}\Models\hum_predictor.joblib")
    hum_usuario = cajaTexto.get()
    predict_hum = hum_predictor.predict([[float(hum_usuario)]])

    etiqueta["text"] = f"El valor de humedad estimado sería: {int(predict_hum[0][0])}%"

boton1 = tkinter.Button(ventana, text = "Predecir Humedad", command = textoDeHumedad, font='Raleway', bg="#20bebe", fg="white", height=2, width=20, )
boton1.pack()

etiqueta_2 = tkinter.Label(ventana)
etiqueta_2.pack(pady=40)

cajaTexto_2 = tkinter.Entry(ventana)
cajaTexto_2.insert(0, "O ingresa tu valor de humedad.")
cajaTexto_2.pack(fill='x', padx=50)

def textoDeTemperatura():
    temp_predictor = joblib.load(rf"{os.getcwd()}\Models\temp_predictor.joblib")
    temp_usuario = cajaTexto_2.get()
    predict_temp = temp_predictor.predict([[float(temp_usuario)]])
    etiqueta_2["text"] = f"El valor de temperatura estimado sería: {int(predict_temp[0][0])} °C"

boton2 = tkinter.Button(ventana, text = "Predecir Temperatura", command = textoDeTemperatura, font='Raleway', bg="#20bebe", fg="white", height=2, width=20)
boton2.pack()

ventana.mainloop()