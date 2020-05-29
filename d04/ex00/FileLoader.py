import pandas as pd


class FileLoader():
    def __init__(self):
        pass

    def load(self, path):
        try:
            data = pd.read_csv(path)
            print(("({} x {})").format(data.shape[0], data.shape[1]))
            return(data)
        except Exception:
            print("Can't open the path: {}".format(path))
            return (None)

    def display(self, df, n):
        try:
            if (n >= 0):
                print(df[:n])
            else:
                print(df[n:])
        except Exception:
            print("ERROR")


fl = FileLoader()
df = fl.load("good.csv")
fl.display(df, -1)
