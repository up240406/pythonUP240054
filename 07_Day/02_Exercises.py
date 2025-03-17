#LEVEL 2 
#1- Join A and B
A = {'1', '2', '3', '4', '5', '6',}
B = {'4', '5', '6', '7', '8', '9',}
print (A.union(B))

#2- Find A Intersection B
print (A.intersection (B))

#3- Is A subset of B
print(A.issubset (B))

#4- Are A and B disjoint sets
print (A.isdisjoint (B))

#5- Join A with B and B with A
print (A.union (B))
print (B.union (A))

#6- What is the symmetric difference between A and B
print (A.symmetric_difference (B))

#7- Delete the sets completely
del A
del B