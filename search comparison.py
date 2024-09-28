

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
    left = 0
    right = len(theArray) - 1

    while left <= right:
        mid = left + (right - left) // 2  # Prevents overflow for large arrays
        if theArray[mid] == searchItem:
            return mid  # Target found
        elif theArray[mid] < searchItem:
            left = mid + 1  # Search right half
        else:
            right = mid - 1  # Search left half

    return (False)  # Target not found


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

if r == 1:    #The array is sorted so we can do a binay search on it
    startBinary = time.time()
    fndB = searchArrayBinary(searchItem)
    endBinary = time.time()

if not fnd:
    print ("Item was not found!")
else:
    print ("Time taken: ",end-start)
    
if r ==1: #print result of binary search on the sorted array
    if not fndB:
         print ("Binary Search - Item was not found!")
    else:
        print ("Binary Search Time taken: ",endBinary-startBinary)





