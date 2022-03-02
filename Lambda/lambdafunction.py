'''
def myfunction(n):
    return lambda a : a * n
mydoubler = myfunction(2)
print(mydoubler(11))
'''

def my_function(n):
    return lambda a : a * n
mydoubler = my_function(2)
mytripler = my_function(3)

print(mydoubler(11))
print(mytripler(12))