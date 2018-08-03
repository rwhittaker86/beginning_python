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
