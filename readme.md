# Exercise 1 ( Overloading * for Scalar Multiplication):

You can multiplay a number to a vector: (x,y) * c = (x*c, y*c)

use the dunder method __ add__ to add a scalar (number) to an instance of Vector2d (see notes)

vec2d = Vector2d(1,1)
new_vec2d = vec2d * 10
print(vec2d) # --> Vector2d (10, 10)

# Exercise 2 ( Overloading * for Scalar Multiplication II):
In this exercise we now reverse the order of the operands.
You can also multiplay a number to a vector:  c * (x,y)  = (x*c, y*c)
use the dunder method __ rmul__ to add a scalar (number) to an instance of Vector2d
research how __mul__  and __rmul__  work together


# Exercise 3 (Unary Operators):
Look at the following expression:
-(x,y) = (-x,-y)
use __ neg__ to achieve the same behavior for our vector instances
vec2d = Vector2d(1,1)
neg_vec2d = -vec2d


# Exercise 4 (Overloading + for Vector Addition):
- implement +  mathematical vector operation
(x1,y1) + (x2,y2) = (x1+x2, y1+y2)
   v1 = Vector2d([3,4,5])
   v2 = Vector2d([6,7,8])
   v3  = v1 + v2 #---> Vector2d([9, 11, 13])


# Exercise 5 (Overloading + for Vector AdditionII):
extend our Vector2d class so that we can do the following operation:
   list_v1 = [3,4,5]
   v2 = Vector2d([6,7,8])
   v3  = list_v1 + v2 #---> Vector2d([9, 11, 13])


# Bonus (Rotational Matrix 2d):

define a class which takes phi
and depending  on phi  you can construct your rotational matrix in 2D:

R = matrix with 1st row [cos 0 sin 0] and 2nd row [sin 0 cos 0]


the instance of your class should be able to be apply to a 2 dimensional Vector, list or tuple: vec = R * [1,2]
visulize it with matplotlib (quiver)