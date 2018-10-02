#Comparing values for sameness
print(1==1)
print(1==2)
print(1.23==1)
print(1.0==1)

a = "Mackintosh apples"
b = "Black Berries"
c = "Golden Delicious apples"
print(a==b)
print(b==c)
print(a[-len("apples"):-1]==c[-len("apples"):-1])

apples = ["Mackintosh", "Golden Delicious", "Fuji", "Mitsu"]
apple_trees = ["Golden Delicious", "Fuji", "Mitsu", "Mackintosh"]
print(apples == apple_trees)
apple_trees = ["Mackintosh", "Golden Delicious", "Fuji", "Mitsu"]
print(apples == apple_trees)
#example 2
tuesday_breakfast_sold = {"pancakes":10, "french toast":4, "bagels":32, "omlets":12, "eggs and sausage":13}
wednesday_breakfast_sold = {"pancakes":8, "french toast":5, "bagels":22, "omlets":16, "eggs and sausage":22}
print(tuesday_breakfast_sold == wednesday_breakfast_sold)
thursday_breakfast_sold = {"pancakes":10, "french toast":4, "bagels":32, "omlets": 12, "eggs and sausage":13}
print(tuesday_breakfast_sold == thursday_breakfast_sold)
#Comparing Values for Difference
print(3 == 3)
print(3 != 3)
print(5 != 4)
print(tuesday_breakfast_sold != wednesday_breakfast_sold)
print(tuesday_breakfast_sold != thursday_breakfast_sold)
#Comparing Values For Greater Than an d Less Than
print(5 < 3)
print(10 > 2)
print("a" > "b")
print("A" > "b")
print("A" > "a")
print("b" > "A")
print("Z" > "a")
print("Zebra" > "aardvark")
print("Zebra" > "Zebrb")
print("Zebra" < "Zebrb")
print("Pumpkin" == "pumpkin")
print("Pumpkin".lower() == "pumpkin".lower())
print("Pumpkin".lower())
print("Pumpkin".upper() == "pumpkin".upper())
print("pumpkin".upper())
print("Pumkpin".lower() == "puMpkin")
print("Pumpkin".lower() == "puMpkin".lower())
gourd = "Calabash"
print(gourd)
print(gourd.lower())
print(gourd.upper())
#More Then os Equal, Less Than or Equal
print(1 > 1)
print(1 >= 2)
print(10 < 10)
print(10 <= 10)
#Reversine the Outcome of a Test
print(not True)
print(not 5)
print(not 0)
print(not 5 > 2)
# ommited because it causes a type error in pytthon 3.6 print(not "A" < 3)
print(not "A" < "z")
#Combinging multiple comparisons
print(True and True)
print(False and True)
print(True and False)
print(False and False)
print(True or True)
print(True or False)
print(False or True)
print(False or False)
#Decisions
if 1 > 2 :
    print("No it is not!")
if 2 > 1 :
    print("Yes it is!")

#More complex example
omelet_ingredients = {"egg":2, "mushroom":5, "pepper":1, "cheese":1, "milk":1}
fridge_contents = {"egg":10, "mushroom":20, "pepper":3, "cheese":2, "tomato":4, "milk":15}
have_ingredients = [False]
if fridge_contents["egg"] > omelet_ingredients["egg"]:
    have_ingredients[0] = True
have_ingredients.append("egg")
print(have_ingredients)
if fridge_contents["mushroom"] > omelet_ingredients["mushroom"]:
    if have_ingredients[0] == False:
        have_ingredients[0] = True
    have_ingredients.append("mushroom")
print(have_ingredients)
if fridge_contents["pepper"] > omelet_ingredients["pepper"]:
    if have_ingredients[0] == True:
        have_ingredients[0] = False
    have_ingredients.append("pepper")
if fridge_contents["cheese"] > omelet_ingredients["cheese"]:
    if have_ingredients[0] == False:
        have_ingredients[0] = True
    have_ingredients.append("cheese")
if fridge_contents["milk"] > omelet_ingredients["milk"]:
    if have_ingredients[0] == True:
        have_ingredients[0] = False
    have_ingredients.append("milk")
#elif example - simple
if have_ingredients[0] == True:
    print("I have the ingredients to make an omelet!")
milk_price = 1.50
if milk_price < 1.25:
    print("Buy two cartons of milk, they're on sale")
elif milk_price < 2.00:
    print("Buy one carton of milk, prices are normal")
elif milk_price > 2.00:
    print("Go somewhere else! Milk costs too much here")
#else example - simple
OJ_price = 2.50
if OJ_price < 1.25:
    print("Get once, I'm thirsty'")
elif OJ_price <= 2.00:
    print("Umm... sure, but I'll drink it slowly.")
else:
    print("I don't have enough money. Never mind.")
