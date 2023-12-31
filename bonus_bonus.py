import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.animation import FuncAnimation

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

    def animate(self, vector, duration=10, frame_rate=30):
        """
        Animates the rotation from the original position to the transformed position.
        The animation lasts for the specified duration in seconds.
        """
        num_frames = int(duration * frame_rate)
        angles = np.linspace(0, 2 * np.pi, num_frames)

        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')

        q = ax.quiver(0, 0, 0, vector[0], vector[1], vector[2], color='blue', label='Original')
        q_animation = ax.quiver(0, 0, 0, vector[0], vector[1], vector[2], color='red', label='Transformed')

        def update_frame(frame):
            roll = self.roll * angles[frame] / (2 * np.pi)
            pitch = self.pitch * angles[frame] / (2 * np.pi)
            yaw = self.yaw * angles[frame] / (2 * np.pi)

            R = RotationalMatrix3D(roll, pitch, yaw)

            transformed_vector = R * vector

            q_animation.set_segments([(np.array([0, 0, 0]), transformed_vector)])

            return q_animation

        animation = FuncAnimation(fig, update_frame, frames=num_frames, interval=1000 / frame_rate, blit=False)

        ax.set_xlim([-5, 5])
        ax.set_ylim([-5, 5])
        ax.set_zlim([-5, 5])
        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_zlabel('Z')
        ax.set_title('3D Rotational Matrix Transformation Animation')
        ax.legend()

        plt.grid(True)
        plt.show()

roll = np.pi / 4
pitch = np.pi / 3
yaw = np.pi / 6

vector = np.array([1, 2, 3])

rot_matrix = RotationalMatrix3D(roll, pitch, yaw)
rot_matrix.animate(vector, duration=10, frame_rate=30)
