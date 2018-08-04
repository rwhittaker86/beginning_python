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
