# dicts: same as objects in javascript
band = {
    "vocals": "plant",
    "guitar": "page",
    "fans": 3
}

print(band["vocals"])
print(band.get("guitar"))

# list all keys and values and return it as lists
print(band.keys())
print(band.values())
# return the keys value pair in a tuple
print(band.items())
print("tr" in band)

# change values in dicts
band["fans"] = 30000
band.update({"vocals":"tree", "suburu": "car"})
print(band)

# remove a key value pair
print(band.pop('suburu')) # returns only the value 
print(band)

band["drums"] = "bonham"
print(band)

print(band.popitem()) # returns the last key value pair as a tuple unlike pop which only returns the value

# delete and clear
del band["vocals"]
print(band)

""" band.clear()
print(band) """

# copy a dict
""" band2 = band  """# creates a reference
band2 = band.copy()
print(band2)
band3 = dict(band)

# nested dicts
member1 = {
    "name": "xyz",
    "age": 30
}
member2 = {
    "name": "wer",
    "age": 24
}

band = {
    "member1":member1,
    "member2":member2
}
print(band)
print(band["member1"]["age"])

# sets: no duplicates are allowed
numbers = {1,2,3,4,5,6,6}
print(numbers)
numbers2 = {1, True, False,0}
print(numbers2) # True is equal to 1 and False is equal to 0
print(1 in numbers2)
# cannot refer to a set by index or key

# add an element to a set
numbers.add(7)
print(numbers)
# adding elements from another set
numbers.update({9,10,11})
print(numbers)

numbers.update([12,13,14])
print(numbers)
# update works with all lists sets tuples dicts etc

# merge 2 sets to create a new set without changing the original sets
one = {1,2,3,4}
two = {5,6,7,8}

newSet = one.union(two)
print(newSet)

# keep only the dups

three = {5,6,7,8}
four = {5,6,9,10}
three.intersection_update(four) # modifies three
print(three)
 # keep everything except the dups
five = {1,2,3,4}
six = {3,4,5,6}

five.symmetric_difference_update(six) # modifies five
print(five)
