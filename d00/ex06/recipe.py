cookbook = {
    "sandwich": {
        "ingredients": ("ham", "bread", "cheese", "tomatoes"),
        "meal": "lunch",
        "prep_time": 10
    },
    "cake": {
        "ingredients": ("flour", "sugar", "egg"),
        "meal": "dessert",
        "prep_time": 60
    },
    "salad": {
        "ingredients": ("avocado", "arugula", "tomatoes", "spinach"),
        "meal": "lunch",
        "prep_time": 15
    }
}


def getRecipe(name):
    if name in cookbook:
        print("Recipe for " + name + ":")
        print("Ingredients list: {}".format(cookbook[name].get("ingredients")))
        print("To be eaten for {}".format(cookbook[name].get("meal")))
        print("Takes {} minutes \
of cooking.".format(cookbook[name].get("prep_time")))
    else:
        print("Recipe is not in cookbook")


def delRecipe(name):
    if name in cookbook:
        del cookbook[name]
    else:
        print("Recipe is not in cookbook")


def addRecipe(name, ingredients, meal, prep_time):
    cookbook[name] = {
        "ingredients": ingredients,
        "meal": meal,
        "prep_time": prep_time
    }


def recipeName():
    s = "Recipes names are : "
    for i in cookbook:
        s += "{}, ".format(i)
    print(s)


def main():
    while (1):
        print("Select an option:\n1: print book\n2: print one recipe\n\
3: adding recipe\n4: delete recipe\n5: quit the book")
        i = input()
        if (i == "1"):
            recipeName()
            print("\n")
        elif (i == "2"):
            print("Enter recipe to print : ")
            s = input()
            getRecipe(s)
            print("\n")
        elif (i == "3"):
            print("Enter recipe name to add : ")
            name = input()
            print("Enter recipe meal type : ")
            meal = input()
            print("Enter preparation time : ")
            prep_time = input()
            print("Enter recipe ingredients (separate with comma ','): ")
            ingredients = input()
            ingredients = tuple(ingredients.split(","))
            addRecipe(name, ingredients, meal, prep_time)
            print("\n")
        elif (i == "4"):
            print("Enter recipe name to delete : ")
            name = input()
            delRecipe(name)
            print("\n")
        elif (i == "5"):
            return
        else:
            print("Enter a valid option\n")


if __name__ == "__main__":
    main()
