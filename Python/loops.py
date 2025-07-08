value = 1 
while value < 10:
    value += 1
    if value == 5:
        continue  # skips the rest of the loop when value is 5
    print(value)
    
else:
    print("value is equal to " + str(value))

# iterating through a list
users = ['dave','anamika','anna']
for x in users:
    print(x)

for x in "mississippi":
    print(x)

for x in users:
    if x == "anamika":
        break
    print(x)

for x in range(1,10):
    print(x)

for x in range(1,10,2):
    print(x)

actions = ['run','jump','swim0']

for x in users:
    for y in actions:
        print(x + " " + y)