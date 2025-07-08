users = ['sarah', 'john', 'mike', 'anna']
dave = [42,True]
emptyList = []

print('sarah' in dave)
print(users[2])
print(users[1:])

# to find the index of an element
print(users.index('anna'))

print(len(users))
users.append('java')
print(users)

#concatenation of two lists

users += dave
print(users)
users.extend(['jason']) # needs to be a list else each individual character will be added seperately
print(users)

# to insert an element at a specific index

users.insert(0,69)
print(users)

# to add element without replacing the existing item

users[2:2] = ['kai','kate']
print(users)

# to replace multiple elements at once
users[1:3] = ['james','julia']
print(users)

# to remove an element

users.remove('anna')
print(users)

users.pop()
print(users)

del users[0]
print(users)

""" del emptyList
print(emptyList) """

# to empty a list

dave.clear()
print(dave)

users.remove(42)
users.remove(True)
print(users)
# to sort a list
users.sort()
print(users)

users.extend(['Zephyr','Candice'])

users.sort()
print(users)

users.sort(key=str.lower)
print(users)

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 21, 66, 23]
nums.reverse()
print(nums)

""" nums.sort(reverse=True) #reverse here means descending order
print(nums) """

# to keep the original list unchanged

print(sorted(nums,reverse=True))
print(nums)

numscopy = nums.copy()
myNums = list(nums)
myCopy = nums[:]

#tuples: same as lists but immutable
myTuple = (1,2,3,4,5,5,8,2,2)
print(type(myTuple))

#create a list from a tuple and to add an element to a tuple
newList = list(myTuple)
newList.append('elem')
newTuple = tuple(newList)
print(newTuple)
print(myTuple)

# unpacking a tuple

(a,*b,c,d) = myTuple # asterisks is important
print(a)
print(b)
print(c)
print(d)

print(myTuple.count(2))
