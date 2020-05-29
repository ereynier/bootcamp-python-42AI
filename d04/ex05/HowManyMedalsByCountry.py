import pandas as pd
from FileLoader import FileLoader


def howManyMedalsByCountry(data, name):
    dic = {}
    d = data[data["Team"] == name]
    year_list = d.drop_duplicates("Year")["Year"].values
    for year in year_list:
        y = d[d["Year"] == year]
        y = y.drop_duplicates(subset=["Event", "Medal"])
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
dic = howManyMedalsByCountry(data, 'China')
print(dic)
