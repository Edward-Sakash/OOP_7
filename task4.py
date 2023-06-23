"""
# Exercise 4 (Overloading + for Vector Addition):
- implement +  mathematical vector operation
(x1,y1) + (x2,y2) = (x1+x2, y1+y2)
   v1 = Vector2d([3,4,5])
   v2 = Vector2d([6,7,8])
   v3  = v1 + v2 #---> Vector2d([9, 11, 13])

"""
# Solution
"""
In this code, the Vector2d class has been modified to accept a list of coordinates and convert it
into a NumPy array for vector operations. The __add__ dunder method is implemented to overload
the + operator for vector addition. It performs element-wise addition of the coordinates
and returns a new Vector2d object with the resulting coordinates.
The rest of the code is similar to the previous examples. We create two Vector2d instances, v1 and v2,
and perform vector addition by using the + operator to add them together, storing the result in v3.
We then plot all three vectors, v1, v2, and v3, with different colors.
When you run the code, it will perform vector addition, create the plot with three colors,
and produce the desired output.

"""

import matplotlib.pyplot as plt
import numpy as np

class Vector2d:
    def __init__(self, coordinates):
        self.coordinates = np.array(coordinates)

    def __add__(self, other):
        """
        Overloads the + operator to perform vector addition on two Vector2d instances.
        Returns a new Vector2d object with the coordinates added element-wise.
        """
        return Vector2d(self.coordinates + other.coordinates)

    def __str__(self):
        """
        Returns a string representation of the Vector2d object.
        """
        return f"Vector2d({self.coordinates.tolist()})"

v1 = Vector2d([3, 4, 5])
v2 = Vector2d([6, 7, 8])
v3 = v1 + v2  # Perform vector addition on v1 and v2

# Plotting the vectors
plt.quiver(0, 0, v1.coordinates[0], v1.coordinates[1], angles='xy', scale_units='xy', scale=1, color='blue', label='v1')
plt.quiver(0, 0, v2.coordinates[0], v2.coordinates[1], angles='xy', scale_units='xy', scale=1, color='red', label='v2')
plt.quiver(0, 0, v3.coordinates[0], v3.coordinates[1], angles='xy', scale_units='xy', scale=1, color='green', label='v3')

plt.xlim(0, 15)
plt.ylim(0, 15)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Vector2d Addition')
plt.legend()
plt.grid(True)
plt.show()

print(v3)  # Output: Vector2d([9, 11, 13])
