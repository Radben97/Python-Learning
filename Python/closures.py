# it is a function that has access to scope of it's parent function
def parent_function(x):
    coin = x
    def child_function():
        nonlocal coin
        coin -= 1
        if coin > 0:
            print(f"coin left: {coin}")
        else:
            print("no more coins")
    return child_function

tommy = parent_function(3)
jenny = parent_function(5)

tommy()
tommy()
tommy()

jenny()