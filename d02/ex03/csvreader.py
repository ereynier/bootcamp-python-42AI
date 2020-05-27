class CsvReader():
    def __init__(self, filename=None, sep=',', header=False, skip_top=0, skip_bottom=0):
        self.filename = filename
        self.sep = sep
        self.header = header
        self.skip_top = skip_top
        self.skip_bottom = skip_bottom
        self.head = ""
        self.data = []

    def __enter__(self):
        try:
            self.file = open(self.filename, "r")
            Lines = self.file.readlines()
            if (self.header):
                self.head = (Lines[0].rstrip('\n')).split(self.sep)
                self.skip_top += 1
            else:
                self.head = (Lines[self.skip_top].rstrip('\n')).split(self.sep)
            for i in range(self.skip_top, len(Lines) - self.skip_bottom):
                if (len(Lines[i].split(self.sep)) != len(self.head)):
                    return (None)
                else:
                    self.data.append(Lines[i].rstrip('\n').split(self.sep))
            return (self)
        except:
            return (None)

    def __exit__(self, type, value, traceback):
        self.file.close()

    def getheader(self):
        if (self.header):
            return (self.head)
        return (None)
    
    def getdata(self):
        return (self.data)

if __name__ == "__main__":
    with CsvReader('good.csv', ',', True, 0, 1) as file:
        data = file.getdata()
        header = file.getheader()
        print(data)
        print(header)