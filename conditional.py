# if 
answer = "left"
if answer == "left" :
    print("left hand")
# if else
def name():
    name = "Sophia"
    if name == "Sophia" :
        print("Her name is Sophia.")
    else :
        print("Her name is not Sophia.")

name()

# if elif
def greater_less_equal_5(num):
    if num > 5 :
        return 1
    elif num < 5 :          
        return -1
    else :
        return 0
        
print greater_less_equal_5(4)
print greater_less_equal_5(5)
print greater_less_equal_5(6)
