from sys import argv

script,filename = argv

txt = open(filename)

print("Here\'s your file {filename}:")
print(txt.read())

print("Tpye the filename again:")
file_again = input("> ")
# python 2.x version
# file_again = raw_input("> ")

txt_again = open(file_again)

print(txt_again.read())
