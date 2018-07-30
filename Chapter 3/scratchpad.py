breakfast= [ "coffee", "tea", "toast", "egg"]
count = 0
print("Today's breakfast is %s" % breakfast[count])
count = 1
print("Today's breakfast is %s" % breakfast[count])
count = 2
print("Today's breakfast is %s" % breakfast[count])
count = 3
print("Today's breakfast is %s" % breakfast[count])
#When accessing more than one element of a list apparently it's "essential" to use a variable to hold the numbered position(?)
print(breakfast[0])
#hmm "essential" maybe I'm guessing the book just wants to let the reader know about using iterator variables since it's not actually necessary
breakfast[count]= "sausage" # apparently adhoc adding an entry to the breakfast list causes an error but we can overwrite one of the existing values
print("Today's breakfast is %s" % breakfast[count])
#but you can use a python method to easily add a list element
breakfast.append("waffles")
count = 4
print("Today's breakfast is %s" % breakfast[count])
breakfast.extend(["juice", "decaf", "oatmeal"])
print(breakfast)
menus_specials = {}
menus_specials["breakfast"] = "Canadian ham"
menus_specials["lunch"] = "tuna surprise"
menus_specials["dinner"] = "Cheeseburger Deluxe"
print(menus_specials)
menus_specials = {"breakfast":"sausage and eggs","lunch":"split pea soup and garlic bread","dinner":"2 hot dogs and onion rings"}
print(menus_specials)

print("%s" % menus_specials["breakfast"])
print("%s" % menus_specials["lunch"])
print("%s" % menus_specials["dinner"])

hungry = menus_specials.keys()
print(list(hungry))
starving = menus_specials.values()
print(list(starving))

menu={"breakfast":"spam","lunch":"spam","dinner":"spam"}
print(menu)
print(menu.get("lunch"))
print(menu.get("breakfast"))

last_names = ["Douglas", "Jefferson", "Williams", "Frank", "Thomas"]
print("%s" % last_names[0])
print("%s" % last_names[0][0])
print("%s" % last_names[1])
print("%s" % last_names[1][0])
print("%s" % last_names[2])
print("%s" % last_names[2][0])
