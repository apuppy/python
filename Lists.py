zoo_animals = ["wolf","tiger","panda"]
# empty list
zoo = []
#print(type(zoo))
# access by index,index start at zero
print(zoo_animals[2])
# reassign value
zoo_animals[1] = "dolphin"
print(zoo_animals[1])

# append value to a list
suitcase = []
suitcase.append("underware")
suitcase.append("skirt")
suitcase.append("hat")
suitcase.append("scarf")
print(len(suitcase))

# slice list
suitcase = ["sunglasses", "hat", "passport", "laptop", "suit", "shoes"]
first = suitcase[0:2]
middle = suitcase[2:4]
last = suitcase[4:6]
print(first)
print(middle)
print(last)

# slicing list and string
animals = "catdogfrog"
cat = animals[:3]
dog = animals[3:6]
frog = animals[6:]
print('cat:%s,dog:%s,frog:%s.' %(cat,dog,frog))

# maintain list's order
animals = ["dog","cat","fish","horse"]
fish_index = animals.index("fish")
animals.insert(fish_index,"crab")
print(animals)

# for loop
number_list = [1,3,5,7,9]
for number in number_list:
    print(2*number)

# sort string or list
numbers = [1,2,3,7,5]
square_list = []
for x in numbers:
    square_list.append(x**2)

print(square_list.sort())

# remove item
IDEs = ["eclipse","NetBeans","Visual Stutio","PhpStorm","Zend Stutio","PyCharm"]
IDEs.remove("Zend Stutio")
IDEs.remove("eclipse")
print(IDEs)