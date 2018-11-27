# Simple Pong in Python 3 for Beginners
# By @kyleandjoe
# Part 1: Getting Started

import turtle

wn = turtle.Screen()
wn.title("Pong by @kyleandjoe")
wn.bgcolor("black")
wn.setup(width=800, height=800)
wn.tracer(0)



# Main game loop
while True:
    wn.update()
