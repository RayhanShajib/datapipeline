import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import pygame

# Audio setup
pygame.mixer.init()
pygame.mixer.music.load("masseffect_map_music.mp3")

# 1. Data preparation (NumPy)
frames = 200
countdown_end = 60
time = np.linspace(0, 10, frames)
moon_pos = [8, 8]
start_pos = [0, 3]

flight_frames = frames - countdown_end

# Ernest-1: Linear path
e1_x = np.linspace(0, moon_pos[0], frames)
e1_y = np.linspace(0, moon_pos[1], frames)

# Kernest-2: Curvy, faster path (using a sine wave for 'wobble')
k2_x = np.linspace(2, moon_pos[0], frames)
k2_y = (time**2 / 12.5) + 0.5 * np.sin(time) 

# 2. Setup Plot
fig, ax = plt.subplots(figsize=(7, 7))
ax.set_xlim(-1, 10)
ax.set_ylim(-1, 10)
ax.scatter(*moon_pos, s=250, color='gray', label='Moon') # The Goal

# Initialize the rocket markers (empty at first)
ernest_plot, = ax.plot([], [], 'ro', markersize=10, label='Ernest-1')
kernest_plot, = ax.plot([], [], 'b^', markersize=10, label='Kernest-2')

countdown_text = ax.text(5, 2, '', fontsize=20, ha='center', color='darkorange', fontweight='bold')
status_msg = ax.text(5, -6.5, 'Status: Pre-launch', ha='center', fontsize=10, bbox=dict(facecolor='white', alpha=0.5))

# 3. The Update Function
def update(i):
# Start the music on the first frame
    if i == 0:
        pygame.mixer.music.play()

    # Countdown Logic: Frames 0 to 30
    if i < 10:
        countdown_text.set_text("3...")
    elif i < 20:
        countdown_text.set_text("2...")
    elif i < 30:
        countdown_text.set_text("1...")
    elif i < 40:
        countdown_text.set_text("LIFT OFF!")
    else:
        # After frame 40, clear the text and move the rockets
        countdown_text.set_text("") 
        
        # We subtract 40 from 'i' so the rockets start at the 
        # first index of our arrays once the countdown is done.
        idx = i - 40
        if idx < frames:
            ernest_plot.set_data([e1_x[idx]], [e1_y[idx]])
            kernest_plot.set_data([k2_x[idx]], [k2_y[idx]])

    return ernest_plot, kernest_plot, countdown_text

# Run the animation
# We increase 'frames' in the animation to account for the countdown time
ani = FuncAnimation(fig, update, frames=frames + 40, interval=50, blit=True)

plt.legend()
plt.title("Simple Rocket Race")
plt.show()

'''import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import pygame # To play your soundtrack

# --- 1. SETUP THE MUSIC ---
pygame.mixer.init()
pygame.mixer.music.load("Projekti_2/NumPy_laskurit/masseffect_map_music.mp3") # Ensure this file is in your folder!

# --- 2. SETUP THE DATA (The NumPy part) ---
frames = 100
moon_x, moon_y = 10, 10

# Simple linear paths from 0 to 10
e1_x = np.linspace(0, moon_x, frames)
e1_y = np.linspace(0, moon_y, frames)

k2_x = np.linspace(3, moon_x, frames)
k2_y = np.linspace(0, moon_y, frames)

# --- 3. SETUP THE PLOT (The Matplotlib part) ---
fig, ax = plt.subplots(figsize=(6, 8))
ax.set_xlim(-2, 12)
ax.set_ylim(-2, 12)

# Plot the Moon as a big gray circle
ax.scatter(moon_x, moon_y, s=400, color='gray', label='Moon')

# Create the empty rocket markers
ernest_plot, = ax.plot([], [], 'ro', markersize=10, label='Ernest-1')
kernest_plot, = ax.plot([], [], 'b^', markersize=10, label='Kernest-2')

# Create a text object for the countdown
countdown_text = ax.text(5, 5, '', fontsize=30, ha='center', color='red')

# --- 4. THE ANIMATION FUNCTION ---
def update(i):
    # Start the music on the first frame
    if i == 0:
        pygame.mixer.music.play()

    # Countdown Logic: Frames 0 to 30
    if i < 10:
        countdown_text.set_text("3...")
    elif i < 20:
        countdown_text.set_text("2...")
    elif i < 30:
        countdown_text.set_text("1...")
    elif i < 40:
        countdown_text.set_text("LIFT OFF!")
    else:
        # After frame 40, clear the text and move the rockets
        countdown_text.set_text("") 
        
        # We subtract 40 from 'i' so the rockets start at the 
        # first index of our arrays once the countdown is done.
        idx = i - 40
        if idx < frames:
            ernest_plot.set_data([e1_x[idx]], [e1_y[idx]])
            kernest_plot.set_data([k2_x[idx]], [k2_y[idx]])

    return ernest_plot, kernest_plot, countdown_text

# Run the animation
# We increase 'frames' in the animation to account for the countdown time
ani = FuncAnimation(fig, update, frames=frames + 40, interval=50, blit=True)

plt.legend()
plt.title("Simple Rocket Race")
plt.show()'''