import pandas as pd
from FileLoader import FileLoader


def youngestFellah(data, year):
    dic = {'f': None, 'm': None}
    if (isinstance(data, pd.DataFrame) and isinstance(year, int)):
        crop = data[data["Year"] == year]
        crop_m = crop[crop["Sex"] == 'M']
        crop_f = crop[crop["Sex"] == 'F']
        dic['f'] = crop_f.Age.min()
        dic['m'] = crop_m.Age.min()
        return (dic)
    else:
        print("ERROR: year is not an int or data is not good")


fl = FileLoader()
df = fl.load("athlete_events.csv")
dic = youngestFellah(df, 1992)
print(dic)
