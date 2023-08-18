import math

###Base distance Calculations -----------------------------------------------

## Euclidian Distance - sqrt of (a1 - b1)^2 + (a2 - b2)^2 + ....
def distance_euc(a,b): 
    total = 0
    for i in range(len(a)):
        total += (a[i] - b[i]) * (a[i] - b[i])
    distance = math.sqrt(total)
    return distance


## Manhatten Distance - sum of absolue difference |a1 - b1| + |a2 - b2| + ...
def distance_man(a,b):    
    distance = 0
    for i in range(len(a)):
        distance += abs(a[i] - b[i])
    return distance

## Chebychev Distance - Max distance btwn item values
def distance_che(a,b):   
    max_val = 0
    for i in range(len(a)):
        check_val = abs(a[i] - b[i])
        if check_val > max_val:
            max_val = check_val
    return max_val


#### Distance Matrix Calc --------------------------------------------------------
## distance_setting = distance function, array_of_items = 2d array, array of each item as array
def distance_matrix(distance_setting, array_of_items):
    ## distance function check
    if callable(distance_setting) == False:
        return False
    

    rows = []
    for i in range(len(array_of_items)):
        column = []
        for j in range(len(array_of_items)):
            column.append(distance_setting(array_of_items[i],array_of_items[j]))
        rows.append(column)
    return rows






# arr1 = [1,1,1,1,1]
# arr2 = [1,2,3,4,5]
# arr3 = [1,2,3,4,5]
# items = [arr1,arr2,arr3]
# a = 0
# distance = distance_che(arr1, arr2)
# print(distance)

# matrix = distance_matrix(distance_man,items)
# print(matrix)