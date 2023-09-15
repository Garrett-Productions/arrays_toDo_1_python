import random

def shuffle(arr):
    for i in range(len(arr)):
        rand_index=random.randint(0,len(arr)-1)
        temp=arr[i]
        arr[i]=arr[rand_index]
        arr[rand_index]=temp
    return arr
print(shuffle([2,5,65,92]))
#Number 1 is completed in Python and i just need to translate to JS, we need to return arr



# Array [-1,7,3] would represent three buildings: first is actually out of view below street level, 
# behind it is second at 7 stories high, third is 3 stories high (hidden behind the 7-story). You are situated at street level. 
# Return array containing heights of buildings you can see, in order. Given [-1,1,1,7,3] return [1,7]. Given [0,4] return [4]. 

def skyline_heights(building_heights):
    max_building_height=0
    visible_buildings=[]
    for building_height in building_heights:
        if building_height>max_building_height:
            visible_buildings.append(building_height)
            max_building_height=building_height
    return visible_buildings

print(skyline_heights([-1,1,1,7,3]))
#This is done for Pyhton I just need to translate to JS



# Create a standalone function that accepts two arrays and combines their values sequentially into a new array. 
# Extra values from either array should be included afterward. 
# Given [4,15,100] and [10,20,30,40], return new array containing [4,10,15,20,30,40,100].

def zip_it(arr1, arr2):
    larger_arr= arr1 if len(arr1)> len(arr2) else arr2
    new_arr=[]
    for i in range(len(larger_arr)):
        if i <= (len(arr1))-1:
            new_arr.append(arr1[i])
        if i <= (len(arr2))-1:
            new_arr.append(arr2[i])
    return new_arr

print(zip_it([5,98,3],[6,73,45]))

#3 Functions
#we already imported random

def shuffle(arr):
    for i in range(len(arr)):
        rand_index=random.randint(0,len(arr)-1) #the randit function selects a random number within the range of its parameters
        temp=arr[i] #here we are creating a temp variable for each position or each time we iterate through through our array, 
        arr[i]=arr[rand_index] #each integer at each position gets multipled by that random number from our var rand_index and gets a new outcome
        arr[rand_index]=temp # we just set that number equal to the temp variable 
    return arr
print(shuffle([2,5,65,92]))

def shuffle(arr):
    for i in range(len(arr)):
        rand_index=random.randint(0,len(arr)-1)
        temp = arr[i]
        arr[i]= arr[rand_index]
        arr[rand_index]= temp 
    return arr
print(shuffle([2,5,65,92]))


#My goal is to shuffle an array [2,5,65,92]

