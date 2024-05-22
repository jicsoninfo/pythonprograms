print ("Paris rabbit got your back :)! Yay!")
print('C:\some\name')
print(r'C:\some\name')
print("""\
Usage: thingy [OPTIONS]
     -h                        Display this usage message
     -H hostname               Hostname to connect to
""")

s = 'supercalifragilisticexpialidocious'
print(len(s))
squares = [1, 4, 9, 16, 25]
print(squares)
print(squares[0])
print(squares[-1])
print(squares[-3])
print(squares + [36, 49, 64, 81, 100])

cubes = [1, 8, 27, 65, 125]
cubes[3] = 64
print(cubes)

cubes.append(216)
cubes.append(7 ** 3)
print(cubes)


#Simple assignment in Python never copies data. When you assign a list to a variable, the variable refers to the existing list. 
#Any changes you make to the list through one variable will be seen through all other variables that refer to it.:
rgb = ["Red", "Green", "Blue"]
rgba = rgb
print(id(rgb) == id(rgba))  # they reference the same object
rgba.append("Alph")
print(rgb)

#All slice operations return a new list containing the requested elements. 
# This means that the following slice returns a shallow copy of the list:
correct_rgba = rgba[:]
correct_rgba[-1] = "Alpha"
print(correct_rgba) #["Red", "Green", "Blue", "Alpha"]
print(rgba) #["Red", "Green", "Blue", "Alph"]

#Assignment to slices is also possible, and this can even change the size of the list or clear it entirely:
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
print(letters)  #['a', 'b', 'c', 'd', 'e', 'f', 'g']
# replace some values
letters[2:5] = ['C', 'D', 'E']
print(letters) #['a', 'b', 'C', 'D', 'E', 'f', 'g']
# now remove them
letters[2:5] = []
print(letters) #['a', 'b', 'f', 'g']
# clear the list by replacing all the elements with an empty list
letters[:] = []
print(letters)

#The built-in function len() also applies to lists:
letters = ['a', 'b', 'c', 'd']
print(len(letters)) #4


# It is possible to nest lists (create lists containing other lists), for example:
a = ['a', 'b', 'c']
n = [1, 2, 3]
x = [a, n]
print(x) #[['a', 'b', 'c'], [1, 2, 3]]
print(x[0]) #['a', 'b', 'c']
print(x[0][1]) #'b'


# 3.2. First Steps Towards Programming
# Of course, we can use Python for more complicated tasks than adding two and two together. 
# For instance, we can write an initial sub-sequence of the Fibonacci series as follows:
# Fibonacci series:
# the sum of two elements defines the next
a, b = 0, 1
while a < 10:
    print(a)
    a, b = b, a+b # 0 1 1 2 3 5 8

