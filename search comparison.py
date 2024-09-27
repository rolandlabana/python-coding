

import time
import random


print ("This program times how long it takes to search for data in an array")
theArray = []

#Create the array of ints
def createArray (numItems, r):
    global theArray
    for counter in range (0, numItems):
            theArray.append(counter)   #fill array

    if r == 0: #array is random, so shuffle it
            random.shuffle(theArray)

    return

#Print the array - caution if large array!
def printArray():
    global theArray
    for counter in range (0, len(theArray)):
        print(theArray[counter])
    return

#Search for an item in the array using binary search
def searchArrayBinary(searchItem):
     #todo - implement binary search here
     pass
     return (False)

#Search for an item in the array
def searchArray(searchItem):
    for curr in range (0, len(theArray)):
        if theArray[curr] == searchItem:
            return (True)   #return found
        
    return (False) #if we reach here, the item was not found

#Main program
num = int (input("How many items in the array? "))
r = int(input("Should the array be random or sorted? (0, 1)?"))


createArray(num, r)
#printArray()

searchItem = int(input("what number to search for? "))

#start timer
start = time.time()
fnd = searchArray(searchItem)
end = time.time()
#stop timer

#todo - implement binary search on the array too if it's sorted
#startBinary = time.time()
#searchArrayBinay(searchItem)
#endBinary = time.time()

if not fnd:
    print ("Item was not found!")
else:
    print ("Time taken: ",end-start)
    #todo - print binary search time taken if used





