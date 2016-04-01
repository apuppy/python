# max()
maximum = max(-1,-3,-13)
print(maximum)

# min()
minimum = min(0,3,9)
print(minimum)

# abs()
absolute = abs(-7)
print(absolute)

# type() returns the type of the data it receives as an argument
print(type(12))
print(type(1.2))
print(type("information"))

# review function
def shut_down(s) :
    if s == "yes" :
        return "Shutting down"
    elif s == "no" :
        return "Shutdown aborted"

    else :
        return "Sorry"

shut_down_result=shut_down("yes")
print(shut_down_result)