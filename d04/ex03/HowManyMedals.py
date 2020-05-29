import pandas as pd
from FileLoader import FileLoader


def howManyMedals(data, name):
    dic = {}
    d = data[data["Name"] == name]
    year_list = d.drop_duplicates("Year")["Year"].values
    for year in year_list:
        y = d[d["Year"] == year]
        try:
            g = y["Medal"].value_counts()["Gold"]
        except Exception:
            g = 0
        try:
            s = y["Medal"].value_counts()["Silver"]
        except Exception:
            s = 0
        try:
            b = y["Medal"].value_counts()["Bronze"]
        except Exception:
            b = 0
        dic[year] = {'G': g, 'S': s, 'B': b}
    return (dic)


fl = FileLoader()
data = fl.load("athlete_events.csv")
dic = howManyMedals(data, 'Kjetil Andr Aamodt')
print(dic)
