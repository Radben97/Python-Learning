def recursion(num):
    if num >= 9:
        return num + 1
    
    total = num + 1
    print(total)
    return recursion(total) # recursion calls always need to return a value, otherwise it will return None by default

recursion(0)

# even with a continue, the condition in a loop is checked before the next iteration
 
# how to modify a global varaible locally
print(" ")
x = 5

def another():
    global x
    x += 1 
    y = 20
    print(x)
    def again():
        nonlocal y
        y -= 1
        print(y)
    again()

another()