from FileLoader import FileLoader
import pandas as pd
import matplotlib.pyplot as p
import seaborn as sns
from pandas.plotting import scatter_matrix


class MyPlotLib():
    def __init__(self):
        pass

    def histogram(self, data, features):
        for feat in features:
            d = data.drop_duplicates(['Name', feat])
            try:
                d.hist(feat)
            except Exception:
                print("ERROR: {} not found or not numerical".format(feat))
        p.show()

    def density(self, data, features):
        for feat in features:
            d = data.drop_duplicates(['Name', feat])
            try:
                sns.distplot(d[feat], hist=False, kde=True)
            except Exception:
                print("ERROR: {} not found or not numerical".format(feat))
        p.show()

    def pair_plot(self, data, features):
        d = data
        for feat in features:
            d = d.drop_duplicates(['Name', feat])
        d = d[features]
        for feat in features:
            d = d[d[feat].notna()]
        try:
            scatter_matrix(d, diagonal='hist')
        except Exception:
            print("ERROR: features not found or not numerical")
        p.show()

    def box_plot(self, data, features):
        d = data
        for feat in features:
            d = d.drop_duplicates(['Name', feat])
        d = d[features]
        for feat in features:
            d = d[d[feat].notna()]
        try:
            d.plot.box()
        except Exception:
            print("ERROR: features not found or not numerical")
        p.show()


fl = FileLoader()
data = fl.load("athlete_events.csv")
plot = MyPlotLib()
plot.histogram(data, ['Weight', 'Height', 'Age', 'City'])
plot.density(data, ['Weight', 'Height'])
plot.pair_plot(data, ['Weight', 'Height'])
plot.box_plot(data, ['Weight', 'Height'])
