import time
from random import randint
import getpass

def log(func):
    def inner1(*args, **kwargs):
        t0 = time.time()
        ret = func(*args, **kwargs)
        dt = (time.time() - t0 ) * 1000
        if (dt > 1000):
            dt = dt / 1000
            t = "{:.3f} s".format(dt)
        else:
            t = "{:.3f} ms".format(dt)
        name = (' '.join((func.__name__).split('_'))).title()
        log_file = open("machine.log", "a+")
        log_file.write("({})Running: {: <20} [ exec-time = {: <8} ]\n".format(getpass.getuser(), name, t))
        log_file.close()

        return ret
    return inner1

class CoffeeMachine():

    water_level = 100

    @log
    def start_machine(self):
        if self.water_level > 20:
            return True
        else:
            print("Please add water!")
            return False
        
    @log
    def boil_water(self):
        return "boiling..."

    @log
    def make_coffee(self):
        if self.start_machine():
            for _ in range(20):
                time.sleep(0.1)
                self.water_level -= 1
        print(self.boil_water())
        print("Coffee is ready!")

    @log
    def add_water(self, water_level):
        time.sleep(randint(1, 5))
        self.water_level += water_level
        print("Blub blub blub...")


if __name__ == "__main__":

    machine = CoffeeMachine()
    for i in range(0, 5):
        machine.make_coffee()

    machine.make_coffee()
    machine.add_water(70)