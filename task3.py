"""
Exercise 3 (Unary Operators):
Look at the following expression:
-(x,y) = (-x,-y)
use __ neg__ to achieve the same behavior for our vector instances
vec2d = Vector2d(1,1)
neg_vec2d = -vec2d

"""

# Solution
"""
In this code, we have implemented the __neg__ dunder method, which overloads the unary
negation operator (-). The method returns a new Vector2d object with the negated
coordinates by changing the sign of self.x and self.y.
The rest of the code is similar to the previous examples. We plot the original vector vec2d
in blue and the negated vector neg_vec2d in red. Then, we display the plot using plt.show().
Finally, we print the value of neg_vec2d, which should be Vector2d(-1, -1).
When you run the code, it will negate the Vector2d instance,
create the plot with two colors, and produce the desired output.

"""
import matplotlib.pyplot as plt

class Vector2d:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __neg__(self):
        """
        Overloads the unary negation operator (-) to change the sign of the coordinates.
        Returns a new Vector2d object with negated coordinates.
        """
        return Vector2d(-self.x, -self.y)

    def __str__(self):
        """
        Returns a string representation of the Vector2d object.
        """
        return f"Vector2d({self.x}, {self.y})"

vec2d = Vector2d(1, 1)
neg_vec2d = -vec2d  # Negate the Vector2d instance

# Plotting the vectors
plt.quiver(0, 0, vec2d.x, vec2d.y, angles='xy', scale_units='xy', scale=1, color='blue', label='Original')
plt.quiver(0, 0, neg_vec2d.x, neg_vec2d.y, angles='xy', scale_units='xy', scale=1, color='red', label='Negated')

plt.xlim(-2, 2)
plt.ylim(-2, 2)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Vector2d Negation')
plt.legend()
plt.grid(True)
plt.show()

print(neg_vec2d)  # Output: Vector2d(-1, -1)
