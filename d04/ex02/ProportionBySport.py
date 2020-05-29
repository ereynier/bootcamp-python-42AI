from FileLoader import FileLoader
import pandas as pd


def proportionBySport(data, year, sport, gender):
    d = data[data["Year"] == year]
    d = d[d["Sex"] == gender]
    d = d.drop_duplicates("Name")
    total = len(d)
    d = d[d["Sport"] == sport]
    nb = len(d)
    return(nb / total)


fl = FileLoader()
df = fl.load("athlete_events.csv")
prop = proportionBySport(df, 2004, 'Tennis', 'F')
print(prop)
