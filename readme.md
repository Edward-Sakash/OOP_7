# Exercise( Overloading * for Scalar Multiplication):

You can multiplay a number to a vector: (x,y) * c = (x*c, y*c)

use the dunder method __ add__ to add a scalar (number) to an instance of Vector2d (see notes)

vec2d = Vector2d(1,1)
new_vec2d = vec2d * 10
print(vec2d) # --> Vector2d (10, 10)