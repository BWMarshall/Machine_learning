import distance
import normalisation

# x0 = [1,2,3]
# x1 = [3,3,3]
# x2 = [5,0,2]
# x3 = [1,2,2]
# x4 = [3,3,5]

# data = [x0,x1,x2,x3,x4]

# print(data)


# x_new = [5,5,5]

# data.append(x_new)

# ndata = normalisation.min_max_normilsation(data)

# print(ndata)






def k_nearest_calc(distance_function, k, array_of_items, new_item):
    array_of_items.append(new_item)
    normalised_items = normalisation.min_max_normilsation(array_of_items)
    normalised_new_item = normalised_items[-1]
    array_of_distances = []
    for i in range(len(normalised_items)-2):
        array_of_distances.append((i,distance_function(normalised_new_item,normalised_items[i])))
    sorted_array_of_distance = sorted(array_of_distances, key=lambda x: x[1])
    k_nearest_array = sorted_array_of_distance[:k]
    return k_nearest_array,array_of_items

# k_nearest_array, array_of_items = k_nearest(distance.distance_euc,3,data,x_new)
# print(k_nearest_array)
# print(array_of_items)

