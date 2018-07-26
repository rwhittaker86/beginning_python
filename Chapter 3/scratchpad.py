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
