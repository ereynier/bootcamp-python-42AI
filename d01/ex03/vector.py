class Vector:
    def __init__(self, arg):
        self.size = 0
        self.values = []
        if isinstance(arg, list):
            if all(isinstance(x, (float)) for x in arg):
                self.size = len(arg)
                self.values = arg
        elif isinstance(arg, int):
            self.size = arg
            for i in range(0, self.size):
                self.values.append(float(i))
        elif isinstance(arg, range):
            self.size = abs(arg.stop - arg.start)
            for i in arg:
                self.values.append(float(i))
        elif (isinstance(arg, tuple) and len(arg) == 2):
            flag = 1
            for i in arg:
                if not isinstance(i, int):
                    flag = 0
            if (flag):
                self.size = abs(arg[0] - arg[1])
                for i in range(0, self.size):
                    self.values.append(float(i + arg[0]))

    def __add__(self, rhs):
        out = []
        if (isinstance(rhs, Vector)):
            if (self.size != rhs.size):
                print("vectors haven't the same size")
                return (Vector(0))
            for i in range(0, self.size):
                out.append(self.values[i] + rhs.values[i])
        elif (isinstance(rhs, int) or isinstance(rhs, float)):
            for i in range(0, self.size):
                out.append(self.values[i] + rhs)
        else:
            print("ERROR: problem to adding {} to vector".format(rhs))
            return (Vector(0))
        return (Vector(out))

    def __radd__(self, rhs):
        out = []
        if (isinstance(rhs, Vector)):
            if (self.size != rhs.size):
                print("vectors haven't the same size")
                return (Vector(0))
            for i in range(0, self.size):
                out.append(self.values[i] + rhs.values[i])
        elif (isinstance(rhs, int) or isinstance(rhs, float)):
            for i in range(0, self.size):
                out.append(self.values[i] + rhs)
        else:
            print("ERROR: problem to adding {} to vector".format(rhs))
            return (Vector(0))
        return (Vector(out))

    def __sub__(self, rhs):
        out = []
        if (isinstance(rhs, Vector)):
            if (self.size != rhs.size):
                print("vectors haven't the same size")
                return (Vector(0))
            for i in range(0, self.size):
                out.append(self.values[i] - rhs.values[i])
        elif (isinstance(rhs, int) or isinstance(rhs, float)):
            for i in range(0, self.size):
                out.append(self.values[i] - rhs)
        else:
            print("ERROR: problem to adding {} to vector".format(rhs))
            return (Vector(0))
        return (Vector(out))

    def __rsub__(self, rhs):
        out = []
        if (isinstance(rhs, Vector)):
            if (self.size != rhs.size):
                print("vectors haven't the same size")
                return (Vector(0))
            for i in range(0, self.size):
                out.append(rhs.values[i] - self.values[i])
        elif (isinstance(rhs, int) or isinstance(rhs, float)):
            for i in range(0, self.size):
                out.append(rhs - self.values[i])
        else:
            print("ERROR: problem to adding {} to vector".format(rhs))
            return (Vector(0))
        return (Vector(out))

    def __truediv__(self, rhs):
        out = []
        if (rhs == 0):
            print("div by 0 impossible")
            return (Vector(0))
        elif (isinstance(rhs, int) or isinstance(rhs, float)):
            for i in range(0, self.size):
                out.append(self.values[i] / rhs)
        else:
            print("ERROR: problem to adding {} to vector".format(rhs))
            return (Vector(0))
        return (Vector(out))

    def __rtruediv__(self, rhs):
        out = []
        if (rhs == 0):
            print("div by 0 impossible")
            return (Vector(0))
        elif (isinstance(rhs, int) or isinstance(rhs, float)):
            for i in range(0, self.size):
                if (self.values[i] == 0):
                    print("div by 0 impossible")
                    return (Vector(0))
                out.append(rhs / self.values[i])
        else:
            print("ERROR: problem to adding {} to vector".format(rhs))
            return (Vector(0))
        return (Vector(out))

    def __mul__(self, rhs):
        out = []
        x = 0
        if (isinstance(rhs, Vector)):
            if (self.size != rhs.size):
                print("vectors haven't the same size")
                return (Vector(0))
            for i in range(0, self.size):
                x += self.values[i] * rhs.values[i]
                return (x)
        elif (isinstance(rhs, int) or isinstance(rhs, float)):
            for i in range(0, self.size):
                out.append(self.values[i] * rhs)
        else:
            print("ERROR: problem to adding {} to vector".format(rhs))
            return (Vector(0))
        return (Vector(out))

    def __rmul__(self, rhs):
        out = []
        x = 0
        if (isinstance(rhs, Vector)):
            if (self.size != rhs.size):
                print("vectors haven't the same size")
                return (Vector(0))
            for i in range(0, self.size):
                x += self.values[i] * rhs.values[i]
                return (x)
        elif (isinstance(rhs, int) or isinstance(rhs, float)):
            for i in range(0, self.size):
                out.append(self.values[i] * rhs)
        else:
            print("ERROR: problem to adding {} to vector".format(rhs))
            return (Vector(0))
        return (Vector(out))

    def __str__(self):
        return ("vector: {} size: {}".format(self.values, self.size))

    def __repr__(self):
        return (self.values)
