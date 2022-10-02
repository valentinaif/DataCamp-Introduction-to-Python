#FUNCTIONS AND PACKAGES

#--------------------

#FUNCTIONS

#Familiar Functions
#Create variables var1 and var2
var1 = [1, 2, 3, 4]
var2 = True
#Print out type of var1
print(type(var1))
#Print out length of var1
print(len(var1))
#Convert var2 to an integer: out2
out2 = int(var2)

#Multiple Arguments
#Create lists first and second
first = [11.25, 18.0, 20.0]
second = [10.75, 9.50]
#Paste together first and second: full
full = first + second
#Sort full in descanding order: full_sorted
full_sorted = sorted(full, reverse = True)
#Print out full_sorted
print(full_sorted)

#--------------------

#METHODS

#String Methods
#String to experiment with: place
place = "poolhouse"
#Use upper() on place: place_up
place_up = (place.upper())
#Print out place and place_up
print(place)
print(place_up)
#Print out the number of o's in place
print(place.count('o'))

#List Methods
#Create list areas
areas = [11.25, 18.0, 20.0, 10.75, 9.50]
#Print out the index of the element 20.0
print(areas.index(20.0))
#Print out how often 9.50 appears in areas
print(areas.count(9.50))

#List Methods(2)
#Creat list areas
areas = [11.25, 18.0, 20.0, 10.75, 9.50]
#Use append twice to add poolhouse and garage size
areas.append(24.5)
areas.append(15.45)
#Print out areas
print(areas)
#Reverse the orders of the elements in areas
areas.reverse()
#Print out areas
print(areas)

#--------------------

#PACKAGES

#Import Package
#Definition of radius
r = 0.43
#Import the math package
import math
pi = math.pi
#Calculate C
C = 2*pi*r
#Calculate A
A = pi*r**2
#Build print out
print("Circumference: " + str(C))
print("Area: " + str(A))

#Selective Import
#Definition of radius
r = 192500
#Import radians function of math package
from math import radians
#Travel distance of Moon over 12 degrees. Store in dist,
phi = radians(12)
dist = r*phi
#Print out dist
print(dist)
