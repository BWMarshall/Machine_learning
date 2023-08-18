import matplotlib.pyplot as plt
import random
import createData
import k_means
import distance


# Settings and Data Gen
k = 5
data = createData.random_all(50,2)
centroids,assignment = k_means.k_means(distance.distance_euc,k,data)
##print(assignment)

### Colours
colours = ['blue','green','red','cyan','magenta','yellow']
centroid_colour = 'black'

## Plot Centroids
for centroid in centroids:
    plt.scatter(centroid[0], centroid[1], color = centroid_colour, marker="x")

## Plot data
for i in range(k):
    x,y = zip(*assignment[i])
    plt.scatter(x,y, c = colours[i] ,marker = 'o', label= 'Item Class ' + str(i + 1))



# Set labels and title
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('2D Scatter Plot with Multiple Colors')

# Show the plot
plt.show()
