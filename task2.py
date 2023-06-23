"""
Exercise 2( Overloading * for Scalar Multiplication II):
In this exercise we now reverse the order of the operands.
You can also multiplay a number to a vector:  c * (x,y)  = (x*c, y*c)
use the dunder method __ rmul__ to add a scalar (number) to an instance of Vector2d
research how __mul__  and __rmul__  work together
vec2d = Vector2d(1,1)
new_vec2d = 10 * vec2d 
print(vec2d) # --> Vector2d (10, 10)

"""
# Solution

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

    def __rmul__(self, scalar):
        """
        Overloads the * operator when the scalar is on the left-hand side.
        Returns a new Vector2d object with coordinates multiplied by the scalar.
        """
        return self.__mul__(scalar)

    def __str__(self):
        """
        Returns a string representation of the Vector2d object.
        """
        return f"Vector2d({self.x}, {self.y})"

vec2d = Vector2d(1, 1)
new_vec2d = 10 * vec2d  # Perform scalar multiplication with the scalar value 10 on the left-hand side

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

print(new_vec2d)  # Output: Vector2d(10, 10)
