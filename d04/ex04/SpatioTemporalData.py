import pandas as pd
from FileLoader import FileLoader


class SpatioTemporalData():
    def __init__(self, data):
        self.data = data

    def when(self, location):
        d = self.data[self.data["City"] == location]
        year_list = d.drop_duplicates("Year")["Year"].values
        return [year_list.tolist()]

    def where(self, date):
        d = self.data[self.data["Year"] == date]
        location = d.drop_duplicates("City")["City"]
        return (location.tolist())


fl = FileLoader()
data = fl.load("athlete_events.csv")
spatio = SpatioTemporalData(data)
print(spatio.when("Athina"))
print(spatio.where(2016))
