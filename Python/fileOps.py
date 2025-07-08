# read = r
# write = w
# append = a
# create = x
import os

f = open("names.txt","rt")

""" print(f.read(25)) """
""" print(f.readline())
print(f.readline())
 """

""" for line in f:
    print(line)
f.close() """

try: 
    f = open("names.txt")
    print(f.read())
except:
    print("this file doesn't exists")
finally:
    f.close()

# append- creates a file if it doesn't exist

""" s = open("namesake.txt","a")
s.write("neil")
s.close() """

# write-overwrites a file

d = open("namesake.txt","w")
d.write("i deleted it all xd")
d.close()

# two ways to create a file
# one already discussed at append
# another way is to create a file but it returns a error if file already exists in that name

if not os.path.exists("namesake.txt"):
    f = open("namesake.txt","x")
    f.close()

# delete a file

if os.path.exists("namesake.txt"):
    os.remove("namesake.txt")

with open("requirements.txt") as f:
    content = f.read()

with open("names.txt","w") as f:
    f.write(content)