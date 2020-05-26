class Recipe:
    def __init__(self, name, cook_lvl, cook_time, ingred, typ, desc=""):
        "init the class and check values"
        self.name = name
        self.cooking_lvl = cook_lvl
        self.cooking_time = cook_time
        self.ingredients = ingred
        self.recipe_type = typ
        self.description = desc
        self.checkVar()

    def __str__(self):
        "Return the string to print with the recipe info"
        txt = "The recipe for '{}' is a level {} recipe.\n\
            -Cooking time: {}\n\
            -Type: {}\n\
            -Ingredients: {}\n".format(
                                self.name, self.cooking_lvl,
                                self.cooking_time, self.recipe_type,
                                self.ingredients)
        if (self.description != ""):
            txt += "-Description: {}".format(self.description)
        return (txt)

    def checkVar(self):
        flag = 0
        if (self.name == ""):
            print("name is empty")
            flag = 1
        if (self.recipe_type != "starter" and self.recipe_type != "lunch"
                and self.recipe_type != "dessert"):
            print("recipe type is not good")
            flag = 1
        try:
            self.cooking_lvl = int(self.cooking_lvl)
            self.cooking_time = int(self.cooking_time)
        except ValueError:
            print("cooking level and/or cooking time are not an integer")
            flag = 1
        if (self.cooking_lvl < 1 or self.cooking_lvl > 5):
            print("cooking level is to high or too low")
            flag = 1
        if type(self.ingredients) is list:
            True
        else:
            print("your ingredients are not a list")
            flag = 1
        return (flag)
