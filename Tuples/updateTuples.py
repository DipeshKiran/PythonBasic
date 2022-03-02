'''Add Items in Tuples'''
'''
mytuple = ("apple", "banana", "cherry")
mylist = list(mytuple)
mylist[1] = "kiwi"
mytuple = tuple(mylist)

print(mytuple)

'''

'''
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)
print(thistuple)

'''

'''Add tuple to tuple'''
'''
thistuple = ("apple", "banana", "cherry")
thistuple1 = ("orange",)
thistuple += thistuple1

print(thistuple)
'''
'''Remove items in tuple'''
'''
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.remove("apple")
thistuple = tuple(y)

print(thistuple)

'''