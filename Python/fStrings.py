name = "Dave"
coins = 3

message = "%s has %d coins left" %(name,coins)
print(message)

message = "{} has {} coins left".format(name,coins)
print(message)

message = "{1} has {0} coins left".format(coins,name) # we can choose which variable gets printed at a particular place
print(message)

message = "{person} has {money} coins left".format(person=name,money=coins)
print(message)


player = {
    "person": "dave",
    "money":69
}

message = "{person} has {money} coins left".format(**player) # we can use ** to unpack a dictionary
print(message)

# best way: f strings

message = f"{name} has {coins} coins left"
print(message)

message = f"{name.lower()} has {23*3} coins left"
print(message)

message = f"{player['person']} has {23*3} coins left"
print(message)

message = f"{name.lower()} has {2.25 * player['money']:.1f} coins left"
print(message)

for num in range(1,11):
    message = f"{num*2} is the double of {num}"
    print(message)

for num in range(1,11):
    message = f"{num*2: .1%} is the double of {num}"
    print(message)