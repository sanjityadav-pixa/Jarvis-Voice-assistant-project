from vpython import *
import time
import random

# Set up the 3D scene
scene.background = color.black
scene.title = "Happy Holi Animation"

# Create the 3D Text
text_obj = text(text="HAPPY HOLI", align='center', depth=0.5, color=color.red, height=2)

# Animate the text with rotation and color changes
angle = 0
colors = [color.red, color.green, color.blue, color.yellow, color.cyan, color.magenta]

while True:
    rate(20)  # Control animation speed
    angle += 0.05  # Increment rotation
    text_obj.rotate(angle=0.05, axis=vector(0,1,0))  # Rotate around Y-axis
    text_obj.color = random.choice(colors)  # Change colors dynamically
