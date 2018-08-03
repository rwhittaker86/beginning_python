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
by_letter = {}
by_letter[last_names[0][0]] = last_names[0]
by_letter[last_names[1][0]] = last_names[1]
by_letter[last_names[2][0]] = last_names[2]
by_letter[last_names[3][0]] = last_names[3]
by_letter[last_names[4][0]] = last_names[4]
print(len(last_names))
last_element = len(last_names) - 1
print("%s" % last_names[last_element])
print("%s" % last_names[-1])
print("%s" % last_names[-2])
print("%s" % last_names[-3])

slice_me = ("The", "next", "time", "we", "meet", "drinks", "are", "on", "me")
sliced_tuple = slice_me[5:9]
print(sliced_tuple)
slice_this_list = ["The", "next", "time", "we", "meet", "drinks", "are", "on", "me"]
sliced_list = slice_this_list[5:9]
print(sliced_list)
slice_this_string = "The next time we meet, drinks are on me"
sliced_string = slice_this_string[5:9]
print(sliced_string)

living_room = ("rug","table","chair","TV","dustbin","shelf")
apartment = []
apartment.append(living_room)
print(apartment)
apartment = []
apartment.extend(living_room)
print(apartment)

todays_temperatures = [23, 32, 33, 31]
todays_temperatures.append(29)
print(todays_temperatures)
morning = todays_temperatures.pop(0)
print("This mornings temperature was %.02f" % morning)
late_morning = todays_temperatures.pop(0)
print("Todays late morning temperature was %.02f"  % late_morning)
noon = todays_temperatures.pop(0)
print("Todays noon temperature as %.02f" % noon)
print(todays_temperatures)
print("Afternoon temperature was %.02f" % todays_temperatures.pop(0))
print(todays_temperatures)

alphabet = ['a', 'b', 'b', 'c', 'a', 'd', 'e']
print(alphabet)
alph2 = set(alphabet)
print(alph2)
