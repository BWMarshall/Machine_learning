import random
### Creating types of data to be used to check K_means clustering

##Format: ouputs array of items, items are arrays of variables

def random_all(number,dimensions):
    data = []
    for num in range(number):
        point = []
        for dim in range(dimensions):
            point.append(random.randint(0,100))
        data.append(point)
    return data


# def quarters_data(num_in_Quarter, dimensions): #Generates 4 groups of data
#     data = []
#     for segment in range(4):
#         for point in range(num_in_Quarter):
#             point = []