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

# --- Square (in XY plane) ---
square = np.array([
    [-0.5, -0.5, 0],
    [ 0.5, -0.5, 0],
    [ 0.5,  0.5, 0],
    [-0.5,  0.5, 0]
])

# --- Update Plot ---
def update(val=None):
    # Get slider values (degrees → radians)
    x = np.radians(x_slider.get())
    y = np.radians(y_slider.get())
    z = np.radians(z_slider.get())

    # Combine rotations
    Rx = rotation_x(x)
    Ry = rotation_y(y)
    Rz = rotation_z(z)

    R = Rz @ Ry @ Rx
    rotated = square @ R.T

    # Close the square
    pts = np.vstack([rotated, rotated[0]])

    # Clear and redraw
    ax.clear()
    ax.plot(pts[:,0], pts[:,1], pts[:,2], 'g--o')

    # Set axes limits
    ax.set_xlim([-1, 1])
    ax.set_ylim([-1, 1])
    ax.set_zlim([-1, 1])

    # Match viewing angle
    ax.view_init(elev=20, azim=30)

    ax.set_title("Rotate The Square")
    canvas.draw()

# --- Tkinter Window ---
root = tk.Tk()
root.title("Rotate The Square")

# --- Matplotlib Figure ---
fig = plt.figure(figsize=(5,5))
ax = fig.add_subplot(111, projection='3d')

canvas = FigureCanvasTkAgg(fig, master=root)
canvas.get_tk_widget().pack()

# Frame for sliders
slider_frame = tk.Frame(root)
slider_frame.pack(side="bottom", fill="x")


x_slider = tk.Scale(slider_frame, from_=0, to=360,
                    orient=tk.HORIZONTAL, label="X°", command=update)
x_slider.pack(fill="x", padx=10)

y_slider = tk.Scale(slider_frame, from_=0, to=360,
                    orient=tk.HORIZONTAL, label="Y°", command=update)
y_slider.pack(fill="x", padx=10)

z_slider = tk.Scale(slider_frame, from_=0, to=360,
                    orient=tk.HORIZONTAL, label="Z°", command=update)
z_slider.pack(fill="x", padx=10)

slider_frame.grid_columnconfigure(1, weight=1)

# Initial draw
update()

root.mainloop()