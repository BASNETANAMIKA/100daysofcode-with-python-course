numlist = [1,2,3,4,5]
print(numlist)
# reverse
numlist.reverse()
print(numlist)
# sort values
numlist.sort()
print(numlist)

for num in numlist:
    print(str(num))

mystring = "abracadabra"
print(list(mystring))

l = list(mystring)
# return and remove the last element
returned_var = l.pop()
print("value returned due to pop {0}".format(returned_var))
print("list now {0}".format(l))

# insert value at the end
l.insert(len(l), "a")
print("reformed list {0}".format(l))

del l[0]
print("list after deletion {0}".format(l))

l.insert(0, "a")
print("l after insert is {0}".format(l))

# pop using index
a = l.pop(0)
print("return value in pop {0}".format(a))

new_tuple = tuple(mystring)
print(new_tuple)

for letter in new_tuple:
    print(letter)