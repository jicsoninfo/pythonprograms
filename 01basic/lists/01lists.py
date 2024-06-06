#List items are ordered, changeable, and allow duplicate values.
'''When we say that lists are ordered, it means that the items have a defined order, and that order will not change.
If you add new items to a list, the new items will be placed at the end of the list.'''


#The list is changeable, meaning that we can change, add, and remove items in a list after it has been created.
#Since lists are indexed, lists can have items with the same value:

thislist = ["apple", "banana", "cherry"]
print(thislist)

#Since lists are indexed, lists can have items with the same value:
thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print(thislist)

#To determine how many items a list has, use the len() function:
thislist = ["apple", "banana", "cherry"]
print(len(thislist))

#List items can be of any data type:
list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]

print(list1)
print(list2)
print(list3)

#A list can contain different data types:
list1 = ["abc", 34, True, 40, "male"]
print(list1)

#From Python's perspective, lists are defined as objects with the data type 'list':
mylist = ["apple", "banana", "cherry"]
print(type(mylist))

#It is also possible to use the list() constructor when creating a new list.
thislist = list(("apple", "banana", "cherry"))
print(thislist)
