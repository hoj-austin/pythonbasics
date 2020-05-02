"""
Script for playing with basic python data structures
"""

#lists - square brackets
listA = [1,2,3]
print("listA ", listA) 

#list methods
listA.append(4)
print("listA appended ", listA) 

listA.remove(2)
print("listA remove ", listA) 

listA.reverse()
print("listA reverse ", listA) 

print("listA length", len(listA))

listA.sort()
print("listA sort ", listA) 

a = listA.index(4) #returns first index of value
print(a)

listA.append(4)
print("index of 4 = ", listA.index(4,0,3)) #returns the index of the first value 4, between indices 0 and 3

listA.pop()
print("listA pop ", listA) 

#sets - unordered structure of unique elements
setA = {10, 20, 30, 40, 50}
print(setA)

#set methods
setA.add(100)
print("setA add ", setA) 

setB = {10, 20, 40, 50, 100}
print("setB and setA difference ", setA.difference(setB))

print("setB max ", max(setB))

print("setA and setB intersection ", setB.intersection(setA))

setB.discard(100)
print("setB discarded 100 ", setB)





