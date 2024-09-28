

import time
import random


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
    numCompares = 0

    while left <= right:
        mid = left + (right - left) // 2  # Prevents overflow for large arrays
        numCompares = numCompares + 1
        if theArray[mid] == searchItem:
            return (True, numCompares)  # Target found
        elif theArray[mid] < searchItem:
            left = mid + 1  # Search right half
        else:
            right = mid - 1  # Search left half

    return (False, numCompares)  # Target not found


#Search for an item in the array
def searchArray(searchItem):
    numCompares = 0
    for curr in range (0, len(theArray)):
        numCompares = numCompares + 1    #count the number of comparisons made
        if theArray[curr] == searchItem:
            return (True, numCompares)   #return found
        
    return (False, numCompares) #if we reach here, the item was not found


##################################
#          Main program
##################################
print ("This program times how long it takes to search for data in an array")

#Get the parameters to run on
num = int (input("How many items in the array? "))
sortedArray = int(input("Should the array be random or sorted? (0, 1)?"))

searchItem = int(input("what number to search for? "))

simulateNumber = int(input("How many runs to simulate? "))

for currentIteration in range (1, simulateNumber+1):
    #Create the array and then run with the input parameters
    createArray(num, sortedArray)
    #printArray() - just for debugging on small array sizes

    #start timer
    start = time.time()
    fnd, numCompares = searchArray(searchItem)
    end = time.time()
    #stop timer

    if sortedArray == True:    #The array is sorted so we can do a binay search on it
        startBinary = time.time()
        fndB, numComparesBinary  = searchArrayBinary(searchItem)
        endBinary = time.time()

    #print results of search(es)
    print ("\n****************")
    print ("Iteration:  ", currentIteration)
    print ("****************")
    if not fnd:
        print ("Item was not found!")
    else:
        print ("Time taken: ",end-start, " Num compares: ", numCompares)
        
    if sortedArray == True: #print result of binary search on the sorted array
        if not fndB:
            print ("Binary Search - Item was not found!")
        else:
            print ("Binary Search Time taken: ",endBinary-startBinary, " Num compares: ", numComparesBinary)

    #empty the array before creating a new one for the next run
    theArray.clear()
#end of for currentIteration loop



