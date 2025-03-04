#string manipulation in python
#Strings are sequences of characters.
#Strings are immutable.
#Strings are enclosed in single quotes or double quotes.
#Strings can be concatenated using the + operator.
#Strings can be repeated using the * operator.
#Strings can be accessed using the index operator [].   
#Strings can be sliced using the slice operator [:].
#Strings can be formatted using the format() method.
#Strings can be formatted using f-strings.
#Strings can be formatted using the % operator.
#Strings can be formatted using the format() function.
#Strings can be formatted using the Template class.

#example
#string concatenation
string1 = 'Hello'
string2 = 'World'
string3 = string1 + ' ' + string2
print(string3)

#string repetition
string4 = 'Hello ' * 3
print(string4)

#string access
string5 = 'Hello World'
print(string5[0])
print(string5[1])
print(string5[2])
print(string5[3])
print(string5[4])
print(string5[5])
print(string5[6])
print(string5[7])
print(string5[8])
print(string5[9])
print(string5[10])

#string slicing
string6 = 'Hello World'
print(string6[0:5])
print(string6[6:11])

# Control when displaying Output

num = 188558.566788

print(f"Number: {num:.2f} ")
print(f"Number: {num:,} ")
print(f"Number: {num:b} ")
print(f"Number: {num:o} ")
print(f"Number: {num:X} ")
print(f"Number: {num:E} ")

print()

animal = "cow"
item = "moon"

# print(f"The {animal} jumped over the {item}")
print("The {} jumped over the {}".format(animal,item))

# Positional Arguments
print("The {0} jumped over the {1}".format(animal,item))

# Keyword Arguments
print("The {animal} jumped over the {item}".format(animal= "cow",item="moon"))


animal = "cow"
item = "moon"

text = "The {} jumped over the {}"
print(text.format(animal,item))



name = "Jean"
print("Hello, my name is {} Nice meeting you".format(name))
print("Hello, my name is {:5} Nice meeting you".format(name))
print("Hello, my name is {:<10} Nice meeting you".format(name))
print("Hello, my name is {:>10} Nice meeting you".format(name))
print("Hello, my name is {:^10} Nice meeting you".format(name))





















































































































