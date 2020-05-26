import time
from recipe import Recipe


class Book:
    def __init__(self, name):
        self.name = name
        self.last_update = time.time()
        self.creation_date = time.time()
        self.recipes_list = dict.fromkeys(["starter", "lunch", "dessert"])
        self.recipes_list["starter"] = []
        self.recipes_list["lunch"] = []
        self.recipes_list["dessert"] = []

    def get_recipe_by_name(self, name):
        """Print a recipe with the name 'name' and return the instance"""
        for i in self.recipes_list:
            for j in self.recipes_list[i]:
                if (j.name == name):
                    print(j.__str__())
                    return (j)

    def get_recipes_by_types(self, recipe_type):
        """Get all recipe names for a given recipe_type"""
        if (recipe_type != "starter" and recipe_type != "lunch"
                and recipe_type != "dessert"):
            print("type " + recipe_type + " doesn't exist")
            return
        print("The recipe stored as '" + recipe_type + "' are :")
        for i in self.recipes_list[recipe_type]:
            print("    -" + i.name)

    def add_recipe(self, recipe):
        """"Add a recipe to the book and updtae last_update"""
        if isinstance(recipe, Recipe):
            if (recipe.checkVar() == 0):
                self.last_update = time.time()
                self.recipes_list[recipe.recipe_type].append(recipe)
            else:
                print("Impossible to store an object with bad values")
        else:
            print("Recipe object needed")
