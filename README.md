# Temperature & Humidity Predictor

This predictor uses an algorithm trained with local collected Data. For this reason, the predictor will give results according to the location: Cashapamba, Ambato, Ecuador.

## Installation

You can clone this repository and inside the folder, you will find four folders, the first one is exclusive for our desktop app (You can run the .exe file). Inside the second folder "Predicciones_Finales", you can find all the code used, including the training files, the database, the interface code, and the "real_life_testing" (Which will be explained further on this readme file).

```bash
git clone https://github.com/gaiborjosue/Temp-Hum-Predictor.git
```

## Usage for the Desktop app

1. Navigate to the "Desktop App" folder.
2. Open CMD
3. Type "interface_prediction.exe"

or 

1. Navigate to the "Desktop App" folder.
2. Double Click the "interface_prediction" file.

Then you will be displayed the next app:

![Predictor del Clima 8_24_2021 1_13_18 PM](https://user-images.githubusercontent.com/78832141/130669370-e7522a7c-a240-4936-b4e2-2f8c091448f2.png)

## Usage of the Real-life testing Humidity / Temperature 

1. Navigate to the folder "Predicciones_Finales"
2. Open CMD in that folder.
3. Type: 
```bash
python real_life_testing_humidity.py
```
or

```bash
python real_life_testing_temperature.py
```

4. You will get this prompt (Its an example, it depends on which file you run):

```bash
El valor que predijo el algoritmo es: 32
El valor real es: 37
La diferencia es de 5
```
The first value is the one that the algorithm predicted in real-time for the last value collected from our Weather station.

The second value tells you the real value collected, what this means is that it shows the value collected from our Weather Station.

The third value compares the predicted value and the real collected value and tells you the difference. 


## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)
