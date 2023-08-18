import matplotlib.pyplot as plt
import random

# Sample data
num_points = 5

# Generate random 2D points
points = [(random.uniform(0, 10), random.uniform(0, 10)) for _ in range(num_points)]

# Available marker options
marker_options = ['o', 's', 'D', '^', 'v', 'p', '*', '+', 'x']

# Create a scatter plot with random points and marker options
for point in points:
    marker = random.choice(marker_options)
    plt.scatter(point[0], point[1], marker=marker, label=f'Marker {marker}')

# Set labels and title
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Scatter Plot with Different Marker Options')

# Show legend
plt.legend()

# Show the plot
plt.show()
