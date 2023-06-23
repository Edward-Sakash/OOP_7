"""
# Exercise 5 (Overloading + for Vector AdditionII):
extend our Vector2d class so that we can do the following operation:
   list_v1 = [3,4,5]
   v2 = Vector2d([6,7,8])
   v3  = list_v1 + v2 #---> Vector2d([9, 11, 13])

"""

# Solution

import matplotlib.pyplot as plt
import numpy as np

class Vector2d:
    def __init__(self, coordinates):
        self.coordinates = np.array(coordinates)

    def __add__(self, other):
        """
        Overloads the + operator to perform vector addition on two Vector2d instances or a Vector2d instance and a list.
        Returns a new Vector2d object with the coordinates added element-wise.
        """
        if isinstance(other, Vector2d):
            return Vector2d(self.coordinates + other.coordinates)
        elif isinstance(other, list):
            return Vector2d(self.coordinates + np.array(other))
        else:
            raise TypeError("Unsupported operand type")

    def __str__(self):
        """
        Returns a string representation of the Vector2d object.
        """
        return f"Vector2d({self.coordinates.tolist()})"

list_v1 = [3, 4, 5]
v2 = Vector2d([6, 7, 8])
v3 = Vector2d(list_v1) + v2  # Perform vector addition with a list converted to a Vector2d instance

# Plotting the vectors
plt.quiver(0, 0, list_v1[0], list_v1[1], angles='xy', scale_units='xy', scale=1, color='blue', label='list_v1')
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
