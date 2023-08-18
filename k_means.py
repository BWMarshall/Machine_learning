import normalisation
import distance
import random
import k_nearest
import numpy


def select_initial_centroids(n, array_of_items):
    initial_centroids = random.choices(array_of_items,k=n)
    return initial_centroids

    

def new_centroids_calc(distance_function,array_of_centroids,array_of_items):
    k = len(array_of_centroids)
    ##Normalise all values
    array_of_all = array_of_items + array_of_centroids
    norm_array_of_all = normalisation.min_max_normilsation(array_of_all)
    norm_array_of_centroids = norm_array_of_all[-k:]
    norm_array_of_items = norm_array_of_all[:-k]
    
    ### Calculate Closest Points
    distance_matrix = [] #2d array w items as [i] and centroid as [j]
    for item in norm_array_of_items:
        item_distance = []
        for centroid in norm_array_of_centroids:
            item_distance.append(distance_function(centroid,item))
        distance_matrix.append(item_distance)
    #print(distance_matrix)

    ### Assign groups - in array 1d is assigned centroid, 2d is items, 3d is variables
    ## Make empty assignment array
    assignment_array = []
    for column in range(k):
        assignment_array.append([])

    for i in range(len(distance_matrix)-1):
        min_distance = min(distance_matrix[i])
        assigned_centroid = distance_matrix[i].index(min_distance)
        assignment_array[assigned_centroid].append(array_of_items[i])
    #print(assignment_array)

    ### Adjust Centroids
    adjusted_centroids = []
    for assigmnment in assignment_array:
        centroid_values = []
        variables = numpy.transpose(assigmnment)
        for variable in variables:
            centroid_value = numpy.average(variable)
            centroid_values.append(centroid_value)
        adjusted_centroids.append(centroid_values)
    
    #print(adjusted_centroids)
    return adjusted_centroids,assignment_array




def k_means(distance_function,k,array_of_items):
    current_centroids = select_initial_centroids(k,array_of_items)
    #print(current_centroids)
    new_centroids = None
    #while current_centroids != new_centroids:
    for x in range(10):
        new_centroids, assignment_array = new_centroids_calc(distance_function, current_centroids, array_of_items)
    return new_centroids, assignment_array


#new_centroids(distance.distance_euc,[[5,5,5],[1,1,1]],data)


# x0 = [1,2,3]
# x1 = [3,3,3]
# x2 = [5,0,2]
# x3 = [1,2,2]
# x4 = [3,3,5]
# x5 = [5,5,5]

# data = [x0,x1,x2,x3,x4,x5]

# centroids,assigment = k_means(distance.distance_euc, 2, data)
# print("Centroids: " + str(centroids))
# print("Assignment: " + str(assigment))
