"""
# Bonus (Rotational Matrix 2d):

define a class which takes phi
and depending  on phi  you can construct your rotational matrix in 2D:

R = matrix with 1st row [cos 0 sin 0] and 2nd row [sin 0 cos 0]

the instance of your class should be able to be apply to a 2 dimensional Vector,
list or tuple: vec = R * [1,2]
visulize it with matplotlib (quiver)

"""
# Solution


import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

class RotationalMatrix3D:
    def __init__(self, roll, pitch, yaw):
        self.roll = roll
        self.pitch = pitch
        self.yaw = yaw

    def __mul__(self, vector):
        """
        Applies the rotational matrix to a 3D vector, list, or tuple.
        Returns the transformed vector as a NumPy array.
        """
        R_roll = np.array([[1, 0, 0],
                           [0, np.cos(self.roll), -np.sin(self.roll)],
                           [0, np.sin(self.roll), np.cos(self.roll)]])

        R_pitch = np.array([[np.cos(self.pitch), 0, np.sin(self.pitch)],
                            [0, 1, 0],
                            [-np.sin(self.pitch), 0, np.cos(self.pitch)]])

        R_yaw = np.array([[np.cos(self.yaw), -np.sin(self.yaw), 0],
                          [np.sin(self.yaw), np.cos(self.yaw), 0],
                          [0, 0, 1]])

        R = np.dot(R_roll, np.dot(R_pitch, R_yaw))

        return np.dot(R, vector)

    def visualize(self, vector):
        """
        Visualizes the original and transformed vectors using matplotlib's quiver3D plot.
        The original vector is plotted in blue, and the transformed vector is plotted in red.
        """
        transformed_vector = self.__mul__(vector)

        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')

        ax.quiver(0, 0, 0, vector[0], vector[1], vector[2], color='blue', label='Original')
        ax.quiver(0, 0, 0, transformed_vector[0], transformed_vector[1], transformed_vector[2], color='red', label='Transformed')

        ax.set_xlim([-5, 5])
        ax.set_ylim([-5, 5])
        ax.set_zlim([-5, 5])
        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_zlabel('Z')
        ax.set_title('3D Rotational Matrix Transformation')
        ax.legend()
        plt.grid(True)
        plt.show()

# Example usage
roll = np.pi / 4
pitch = np.pi / 3
yaw = np.pi / 6

vector = np.array([1, 2, 3])

# Create an instance of the RotationalMatrix3D class with the given roll, pitch, and yaw
rot_matrix = RotationalMatrix3D(roll, pitch, yaw)

# Apply the rotation matrix to the vector
transformed_vector = rot_matrix * vector

# Visualize the original and transformed vectors
rot_matrix.visualize(vector)
