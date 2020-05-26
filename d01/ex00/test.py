from book import Book
from recipe import Recipe

ob = Recipe("salut", 5, 65, ["salut", "toi"], "starter")
p = str(ob)
print(p)

b = Book("slt")
b.add_recipe(ob)
b.add_recipe(ob)
b.add_recipe(ob)
b.add_recipe(ob)
b.get_recipes_by_types("starter")
b.get_recipe_by_name("salut")
