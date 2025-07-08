x = 2

class justNotCoolMan(Exception):
    pass

""" try:
    print(x)
except NameError: # exxcept catches all errors so we can corner it down to a specfic error
    print("there is an error") """

try:
    """ print(x/0) """
    """ if not type(x) is str:
        raise TypeError("only strings are allowed") """
    """ raise Exception("lol") """
    raise justNotCoolMan("not cool")

except ZeroDivisionError: 
    print("there is an error")
except Exception as error:
    print(error)
else: 
    print("no error")
finally:
    print("2+2 = 5 change my mind")