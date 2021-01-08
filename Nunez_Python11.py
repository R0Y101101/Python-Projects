#-*- coding: utf-8 -*-
"""
Created on Fri Dec 18 11:05:04 2020

@author: roynu
"""
#1
a = []
for x in range(30, 10-1, -2):
    if(x%2 == 0):
        a.append(x)
        print(x)
print(a)

print()

b = []
for y in range(40, 20-1, -2):
    if(y%2 == 0):
        b.append(y)
        print(y)
print(b)

#2
c = []
for i in range(len(a)):
    print(a[i])
    for j in range(len(b)):
        if a[i] == b[j]:
            c.append(a[i])
print(c)

print()

d = []
for l in range(len(a)):
    print(a[l])
    for n in range(len(b)):
        if a[l] not in d:
            d.append(a[l])
            if b[n] not in d:
                d.append(b[n])
print(d)

print()

#3
setA = {""}
setB = {""}
setC = {""}
for seta in range(len(a)):
    setA.remove("")
    setA.add(a[seta])
    for setb in range(len(b)):
        setB.remove("")
        setB.add(b[setb])
setC = setB.intersection(setA)
print(setC)

for i in range(1):
    if setC == c:
        print("YAY")
    else:
        print("nope, try again")
print(c)
print("this set c")
print(setC)

#4


#5
# numberTuple = (1,2,3,4,5,6,7,8)
# letterTuple = ("a","b","c","d","e","f","g","h")
# boardTuple = ('a1', 'b1', 'c1', 'd1', 'e1', 'f1','g1', 'h1', 'a2', 'b2', 'c2', 'd2', 'e2', 'f2', 'g2', 'h2', 'a3', 'b3', 'c3', 'd3', 'e3', 'f3', 'g3', 'h3', 'a4', 'b4', 'c4', 'd4','e4', 'f4', 'g4', 'h4', 'a5', 'b5', 'c5', 'd5', 'e5', 'f5', 'g5', 'h5', 'a6', 'b6', 'c6', 'd6', 'e6', 'f6', 'g6', 'h6', 'a7', 'b7','c7', 'd7', 'e7', 'f7', 'g7', 'h7', 'a8', 'b8', 'c8', 'd8', 'e8', 'f8', 'g8', 'h8')

# #6
# nestedBoardTuple = (('a1', 'b1', 'c1', 'd1', 'e1', 'f1', 'g1', 'h1'), 
#                     ('a2', 'b2', 'c2','d2', 'e2', 'f2', 'g2', 'h2'),
#                     ('a3', 'b3', 'c3', 'd3', 'e3', 'f3', 'g3', 'h3'),
#                     ('a4', 'b4', 'c4', 'd4', 'e4', 'f4', 'g4', 'h4'),
#                     ('a5', 'b5', 'c5', 'd5', 'e5', 'f5', 'g5', 'h5'),
#                     ('a6', 'b6', 'c6', 'd6', 'e6', 'f6', 'g6', 'h6'),
#                     ('a7', 'b7', 'c7', 'd7', 'e7','f7', 'g7', 'h7'),
#                     ('a8', 'b8', 'c8', 'd8', 'e8', 'f8', 'g8', 'h8'))