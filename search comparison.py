

import time



print ("This program times how long it takes to search for data in an array")
theArray = []

#Create the array of ints
def createArray (numItems):
    global theArray
    for counter in range (0, numItems):
        theArray.append(counter)
    return

#Print the array - caution if large array!
def printArray():
    global theArray
    for counter in range (0, len(theArray)):
        print(theArray[counter])
    return

#Search for an item in the array
def searchArray(searchItem):
    for curr in range (0, len(theArray)):
        if theArray[curr] == searchItem:
            return (True)   #return found
        
    return (False) #if we reach here, the item was not found

#Main program
num = int (input("How many items in the array? "))

createArray(num)
#printArray()

searchItem = int(input("what number to search for? "))

#start timer
start = time.time()
fnd = searchArray(searchItem)
end = time.time()
#stop timer

if not fnd:
    print ("Item was not found!")
else:
    print ("Time taken: ",end-start)



