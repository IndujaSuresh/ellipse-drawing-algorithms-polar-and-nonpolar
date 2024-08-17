# **Ellipse Drawing with OpenGL**
This repository contains a Python script that uses OpenGL to draw ellipses based on polar and nonpolar coordinates. The script provides a basic demonstration of how to render 2D shapes using OpenGL and user inputs.

## **Features**
* Polar Coordinates: Draws an ellipse using polar coordinates.
* Nonpolar Coordinates: Draws an ellipse using Cartesian coordinates.
## **Prerequisites**
To run this script, you need to have Python and the following libraries installed:
* PyOpenGL (for OpenGL bindings in Python)
* math (part of the Python standard library)
## **Code Description**
* init(): Initializes OpenGL settings, including background color, point size, and projection.
* plot(x, y): Plots a point on the screen at the coordinates (x, y).
* uinput(): Handles user input and chooses which ellipse drawing function to use.
* polar(x, y, xr, yr): Draws an ellipse using polar coordinates.
* nonpolar(x, y, xr, yr): Draws an ellipse using Cartesian coordinates.
* main(): Sets up the OpenGL window and starts the main loop.
