import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk
from mpl_toolkits.mplot3d import Axes3D

class RandomWalk:
    def __init__(self, master):
        self.master = master
        self.master.title("Random Walk Simulation")

        # Create a frame for the buttons
        self.frame = tk.Frame(self.master)
        self.frame.pack(side=tk.BOTTOM)

        # Button for 2D random walk
        self.button2d = tk.Button(self.frame, text="2D Random Walk", command=self.plot_2d)
        self.button2d.pack(side=tk.LEFT)

        # Button for 3D random walk
        self.button3d = tk.Button(self.frame, text="3D Random Walk", command=self.plot_3d)
        self.button3d.pack(side=tk.LEFT)

        # Set up the plot figure
        self.fig, self.ax = plt.subplots()

        # Embed the plot in the Tkinter window
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.master)
        self.canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        self.canvas.draw()

    def plot_2d(self):
        self.ax.clear()
        steps = 10
        x, y = [0], [0]
        for _ in range(steps):
            dx, dy = np.random.choice([-1, 1]), np.random.choice([-1, 1])
            x.append(x[-1] + dx)
            y.append(y[-1] + dy)

        self.ax.plot(x, y)
        self.ax.set_title('2D Random Walk')
        self.canvas.draw()

    def plot_3d(self):
        self.fig.clf()
        self.ax = self.fig.add_subplot(111, projection='3d')
        steps = 10000
        x, y, z = [0], [0], [0]
        for _ in range(steps):
            dx, dy, dz = np.random.choice([-1, 1]), np.random.choice([-1, 1]), np.random.choice([-1, 1])
            x.append(x[-1] + dx)
            y.append(y[-1] + dy)
            z.append(z[-1] + dz)

        self.ax.plot(x, y, z)
        self.ax.set_title('3D Random Walk')
        self.canvas.draw()


if __name__ == "__main__":
    root = tk.Tk()
    app = RandomWalk(root)
    root.mainloop()
