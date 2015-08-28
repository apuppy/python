# dictionary structure
stature = {"height":"170cm","weight":"65kg","figure":"fit"}
print(stature["height"])
print(stature['weight'])
print(stature["figure"])

# add key-value pairs into the dictionaries

menu = {}
menu['dish'] = '10RMB'
menu['bowl'] = '6RMB'
menu["fork"] = "5RMB"
print(menu)

# remove key-value pairs
del menu['bowl']
print(menu)

# try
inventory = {
    'gold' : 500,
    'pouch' : ['flint', 'twine', 'gemstone'], # Assigned a new list to 'pouch' key
    'backpack' : ['xylophone','dagger', 'bedroll','bread loaf']
}

inventory['burlap bag'] = ['apple', 'small ruby', 'three-toed sloth']

# Sorting the list found under the key 'pouch'
inventory['pouch'].sort()

# Your code here
inventory['pocket'] = ['seashell','strange berry','lint']
inventory['pocket'].sort()
inventory['backpack'].sort()
inventory['backpack'].remove('dagger')
inventory['gold'] += 50
print(inventory['gold'])

# for loop in strings lists dictionaries
str = 'abcdefg'
for x in str:
    print(x)

list = ['Tom','Bob','Maria','Sophia','Cristopher']
for x in list:
    print(x)

dict = {'name':'Kevin','sex':'male','age':22,'job':'software engineer'}
for index in dict:
    print(dict[index])

# for and if
numbers = [1,2,3,4,5,6,7,8,9,0]
for n in numbers:
    if n % 2 == 0:
        print(n/2)
    elif n % 2 != 0:
        print(n*2)

# function accept datatype
def fizz_count(x):
    count = 0
    for item in x:
        if item == 'fizz':
            count = count + 1
    return count

print(fizz_count(['fizz','fizz','cat','fizz']))

# different loop,loop the other dictionary at the same time
prices = {
    "banana" : 4,
    "apple"  : 2,
    "orange" : 1.5,
    "pear"   : 3,
}
stock = {
    "banana" : 6,
    "apple"  : 0,
    "orange" : 32,
    "pear"   : 15,
}

total = 0
for key in prices:
    print(key)
    print("price: %s" % prices[key])
    print("stock: %s" % stock[key])
    total = total + stock[key]*prices[key]

print(total)