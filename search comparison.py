# This progam compares search algorithms on an array.
# The user is prompted for various inputs
# Currently, the program has to be run twice if you want to compare
# a sorted list vs. an unsorted list. 
# Consider adding a three way comparison in the same run:
#    1. Unsorted list
#    2. Sorted list
#    3. Sorted list with binary search
# But a consideration is if the user should enter the 
# target seacrh value of if it should be chosen randomly
# A good solution might be to allow the user to enter
# a value or choose to have the target chosen randomly.
# Allowing the user to enter a value allows for comparison
# of best, worst, mid cases.

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
        mid = (right - left) // 2 
        numCompares = numCompares + 1
        if theArray[mid] == searchItem:
            return (True, numCompares)  # item found
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

avgCompares = avgTime = TotalCompares = totalTime = avgComparesBinary =  avgTimeBinary = TotalComparesBinary = totalTimeBinary =0

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

    TotalCompares = TotalCompares + numCompares
    avgCompares = TotalCompares/currentIteration
    timeTaken = end-start
    totalTime = totalTime + timeTaken
    avgTime = totalTime / currentIteration
    

    if sortedArray == True:    #The array is sorted so we can do a binay search on it
        startBinary = time.time()
        fndB, numComparesBinary  = searchArrayBinary(searchItem)
        endBinary = time.time()

        TotalComparesBinary = TotalComparesBinary + numComparesBinary
        avgComparesBinary = TotalComparesBinary/currentIteration
        timeTakenBinary = endBinary-startBinary
        totalTimeBinary = totalTimeBinary + timeTakenBinary
        avgTimeBinary = totalTimeBinary / currentIteration

    #print results of search(es)
    print ("\n****************")
    print ("Iteration:  ", currentIteration)
    print ("****************")
    if not fnd:
        print ("Item was not found!")
    else:
        print ("Time taken: ",timeTaken, " Num compares: ", numCompares)
        print ("    Avgs: Time:",  avgTime, "    Compares",avgCompares)
        
    if sortedArray == True: #print result of binary search on the sorted array
        if not fndB:
            print ("Binary Search - Item was not found!")
        else:
            print ("Binary Search Time taken: ",timeTakenBinary, " Num compares: ", numComparesBinary)
            print ("    Avgs Binary: Time:",  avgTimeBinary, "    Compares",avgComparesBinary)

    #empty the array before creating a new one for the next run
    theArray.clear()
#end of for currentIteration loop

print("\n**********************")
print ("Averages of all runs")
print("**********************")
print ("Avg time: ", avgTime, " Avg Compares: ", avgCompares)
print ("Avg time Binary Search: ", avgTimeBinary, " Avg Compares: ", avgComparesBinary)



