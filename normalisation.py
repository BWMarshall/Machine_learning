import math
import numpy


#array = [[1,10,100],[2,20,200],[3,30,300],[5,20,400]]


def min_max_normilsation(array_of_items):
    array_of_variables = numpy.transpose(array_of_items)
    new_array_of_variables = []
    for vars in array_of_variables:
        new_vars = []
        max_var = max(vars)
        min_var = min(vars)
        var_denom = max_var - min_var
        for var in vars:
            new_var = (var - min_var) / var_denom
            new_vars.append(new_var)
        new_array_of_variables.append(new_vars)
    new_array_of_items = numpy.transpose(new_array_of_variables)
    return new_array_of_items


#print(array)
#print(min_max_normilsation(array))
   
            
##[[75,10,50],
##[25,5,30],
##[10,3,20]]