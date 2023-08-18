##Visualising the data with matplot lib
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import k_means
import createData
import distance


##Settings and Data Generation
k = 5
data = createData.random_all(50,3)
centroids,assignment = k_means.k_means(distance.distance_euc,k,data)
#print(assignment)


### Colours
colours = ['blue','green','red','cyan','magenta','yellow']
centroid_colour = 'black'

# Create a 3D plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot Centroids
red_x, red_y, red_z = zip(*centroids)
ax.scatter(red_x, red_y, red_z, c= centroid_colour, marker='o', label='Centroids')

# Plot Items
for i in range(k):
    x,y,z = zip(*assignment[i])
    ax.scatter(x,y,z, c = colours[i] ,marker = '^', label= 'Item Class ' + str(i + 1))


# Set labels and title
ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')
ax.set_title('3D Scatter Plot')

# Add a legend
ax.legend()

# Show the plot
plt.show()
