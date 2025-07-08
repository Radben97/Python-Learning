import math

#Literal assignment
a =10
name = "mahesh"
he = False
print(type(he))
print(type(name)== str)
print(isinstance(he, bool))

# constructors
pizza = str(10)
print(isinstance(pizza, str))
print(pizza)

# concatenation
fullName = name + pizza
print(fullName)
fullName += "!!!"
print(fullName)

# casting
num = str(1980)
print(type(num))

# multiline
multiLine = ''' 
you can write
multiple lines
'''
print(multiLine)

# escaping special characters
sentence = 'this is a can\'t be\t HEY!!\n LOL\\get rekt'
print(sentence)

# string methods
print(sentence.upper())
print(sentence.lower())
print(sentence.title()) # capitalizes the first letter of each word
print(sentence.replace("rekt","rekted")) # og value of sentence won't change after all these methods
print(len(sentence))
sentence += "                          "
sentence = "        " + sentence
print(len(sentence))
print(len(sentence.strip())) # removes leading and trailing spaces
print(len(sentence.lstrip())) # removes leading and trailing spaces from left
print(len(sentence.rstrip())) # removes leading and trailing spaces from right

# build a menu
menu = "menu".upper()
print(menu.center(20, "="))
print("coffee".ljust(16, ".") + "20$".rjust(4))
print("tea".ljust(16, ".")+"15$".rjust(4))
print("bread".ljust(16, ".") + "17$".rjust(4))
print("marmelade".ljust(16, ".") + "8$".rjust(4))
print("espresso".ljust(16, ".") + "12$".rjust(4))

# string index value
print(sentence[19])
print(name[-1])  # last character
print (name[1:-1])
print (name[1:])

# methods returning boolean values
print(name.startswith("dah"))
print(name.endswith("h"))
# numeric datatypes

x = 10
y = 4.24
print(type(y))
# complex type
comp_value = 3+4j
print(type(comp_value))
print(comp_value.real) # outputs a float
print(comp_value.imag) 

# built in functions for numbers

print(abs(y)) # modulus symbol

# math module

print(math.pi)
print(math.asinh(3*math.pi))
print(math.sqrt(81))
print(math.ceil(y))