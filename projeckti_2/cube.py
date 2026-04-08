import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk

# --- Rotation Matrices ---
def rotation_x(theta):
    return np.array([
        [1, 0, 0],
        [0, np.cos(theta), -np.sin(theta)],
        [0, np.sin(theta),  np.cos(theta)]
    ])

def rotation_y(theta):
    return np.array([
        [ np.cos(theta), 0, np.sin(theta)],
        [0, 1, 0],
        [-np.sin(theta), 0, np.cos(theta)]
    ])

def rotation_z(theta):
    return np.array([
        [np.cos(theta), -np.sin(theta), 0],
        [np.sin(theta),  np.cos(theta), 0],
        [0, 0, 1]
    ])

# --- Cube vertices ---
cube = np.array([
    [-0.5, -0.5, -0.5],
    [ 0.5, -0.5, -0.5],
    [ 0.5,  0.5, -0.5],
    [-0.5,  0.5, -0.5],
    [-0.5, -0.5,  0.5],
    [ 0.5, -0.5,  0.5],
    [ 0.5,  0.5,  0.5],
    [-0.5,  0.5,  0.5]
])

# --- Cube edges (pairs of vertex indices) ---
edges = [
    (0,1), (1,2), (2,3), (3,0),  # bottom square
    (4,5), (5,6), (6,7), (7,4),  # top square
    (0,4), (1,5), (2,6), (3,7)   # vertical lines
]

# --- Update Plot ---
def update(val=None):
    x = np.radians(x_slider.get())
    y = np.radians(y_slider.get())
    z = np.radians(z_slider.get())

    Rx = rotation_x(x)
    Ry = rotation_y(y)
    Rz = rotation_z(z)

    R = Rz @ Ry @ Rx
    rotated = cube @ R.T

    ax.clear()

    # Draw edges
    for edge in edges:
        p1 = rotated[edge[0]]
        p2 = rotated[edge[1]]
        ax.plot(
            [p1[0], p2[0]],
            [p1[1], p2[1]],
            [p1[2], p2[2]],
            'g'
        )

    # Axis limits
    ax.set_xlim([-1,1])
    ax.set_ylim([-1,1])
    ax.set_zlim([-1,1])

    ax.view_init(elev=20, azim=30)
    ax.set_title("Rotating Cube")

    canvas.draw()

# --- Tkinter setup ---
root = tk.Tk()
root.title("3D Cube Rotation")

fig = plt.figure(figsize=(5,5))
ax = fig.add_subplot(111, projection='3d')

canvas = FigureCanvasTkAgg(fig, master=root)
canvas.get_tk_widget().pack()

# --- Sliders ---
slider_frame = tk.Frame(root)
slider_frame.pack(side="bottom", fill="x")

x_slider = tk.Scale(slider_frame, from_=0, to=360,
                    orient=tk.HORIZONTAL, label="X°", command=update)
x_slider.pack(fill="x", padx=10, pady=2)

y_slider = tk.Scale(slider_frame, from_=0, to=360,
                    orient=tk.HORIZONTAL, label="Y°", command=update)
y_slider.pack(fill="x", padx=10, pady=2)

z_slider = tk.Scale(slider_frame, from_=0, to=360,
                    orient=tk.HORIZONTAL, label="Z°", command=update)
z_slider.pack(fill="x", padx=10, pady=2)

update()
root.mainloop()