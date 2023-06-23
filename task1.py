"""
Exercise( Overloading * for Scalar Multiplication):
You can multiplay a number to a vector: (x,y) * c = (xc, yc)

use the dunder method __ add__ to add a scalar (number) to an instance of Vector2d (see notes)

vec2d = Vector2d(1,1)
new_vec2d = vec2d * 10
print(vec2d) # --> Vector2d (10, 10)

"""

# Solution

class Vector2d:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __mul__(self, scalar):
        return Vector2d(self.x * scalar, self.y * scalar)

    def __str__(self):
        return f"Vector2d({self.x}, {self.y})"

vec2d = Vector2d(1, 1)
new_vec2d = vec2d * 10
print(new_vec2d)  # Output: Vector2d(10, 10)

print("________________________________________")

class Vector2d:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __mul__(self, scalar):
        """
        Overloads the * operator to perform scalar multiplication on a Vector2d instance.
        Returns a new Vector2d object with coordinates multiplied by the scalar.
        """
        return Vector2d(self.x * scalar, self.y * scalar)

    def __str__(self):
        """
        Returns a string representation of the Vector2d object.
        """
        return f"Vector2d({self.x}, {self.y})"

vec2d = Vector2d(1, 1)
new_vec2d = vec2d * 10  # Perform scalar multiplication on vec2d with the scalar value 10
print(new_vec2d)  # Output: Vector2d(10, 10)

print("______________________________________")

import matplotlib.pyplot as plt

class Vector2d:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __mul__(self, scalar):
        """
        Overloads the * operator to perform scalar multiplication on a Vector2d instance.
        Returns a new Vector2d object with coordinates multiplied by the scalar.
        """
        return Vector2d(self.x * scalar, self.y * scalar)

    def __str__(self):
        """
        Returns a string representation of the Vector2d object.
        """
        return f"Vector2d({self.x}, {self.y})"

vec2d = Vector2d(1, 1)
new_vec2d = vec2d * 10  # Perform scalar multiplication on vec2d with the scalar value 10

# Plotting the vectors
plt.quiver(0, 0, vec2d.x, vec2d.y, angles='xy', scale_units='xy', scale=1, color='blue', label='Original')
plt.quiver(0, 0, new_vec2d.x, new_vec2d.y, angles='xy', scale_units='xy', scale=1, color='red', label='Multiplied')

plt.xlim(0, 15)
plt.ylim(0, 15)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Vector2d Multiplication')
plt.legend()
plt.grid(True)
plt.show()
