"""
#import numpy as np
"""
"""
baseball = [180, 215, 210, 210, 188, 176, 209, 200]
# Create a NumPy array from baseball: np_baseball
np_baseball = np.array(baseball)
# Print out type of np_baseball
print(type(np_baseball))
"""
"""
import numpy as np
from numpy import array
array([1, 2, 3])
np.array([1, 2, 3])
"""
"""
# Definition of radius
r = 192500
# Import radians function of math package
from math import pi
from math import radians
# Travel distance of Moon over 12 degrees. Store in dist.
dist = r*radians(12)
# Print out dist
print(dist)
Selective import
General imports, like import math, make all functionality from the math package available to you. However, if you decide 
to only use a specific part of a package, you can always make your import more selective:
from math import pi
Let's say the Moon's orbit around planet Earth is a perfect circle, with a radius r (in km) that is defined in the 
script.
Instructions
Perform a selective import from the math package where you only import the radians function.
Calculate the distance travelled by the Moon over 12 degrees of its orbit. Assign the result to dist. You can calculate 
this as r * phi, where r is the radius and phi is the angle in radians. To convert an angle in degrees to an angle in 
radians, use the radians() function, which you just imported.
Print out dist.
"""
"""
# Create a numpy array from height_in: np_height_in
np_height_in = np.array(height_in)

# Print out np_height_in
print(np_height_in)

# Convert np_height_in to m: np_height_m
np_height_m = np_height_in * 0.0254

# Print np_height_m
print(np_height_m)
"""
"""
Baseball player's BMI
The MLB also offers to let you analyze their weight data. Again, both are available as regular Python lists: height_in 
and weight_lb. height_in is in inches and weight_lb is in pounds.

It's now possible to calculate the BMI of each baseball player. Python code to convert height_in to a numpy array with 
'the correct units is already available in the workspace. Follow the instructions step by step and finish the game!


# height_in and weight_lb are available as regular lists

# Import numpy
import numpy as np

# Create array from height_in with metric units: np_height_m
np_height_m = np.array(height_in) * 0.0254

# Create array from weight_lb with metric units: np_weight_kg
np_weight_kg = np.array(weight_lb) * 0.453592

# Calculate the BMI: bmi
bmi = np_weight_kg/np_height_m**2

# Print out bmi
print(bmi)
"""
"""
Lightweight baseball players
To subset both regular Python lists and numpy arrays, you can use square brackets:

x = [4 , 9 , 6, 3, 1]
x[1]
import numpy as np
y = np.array(x)
y[1]
For numpy specifically, you can also use boolean numpy arrays:

high = y > 5
y[high]
The code that calculates the BMI of all baseball players is already included. Follow the instructions and reveal 
interesting things from the data!

Instructions
100 XP
Create a boolean numpy array: the element of the array should be True if the corresponding baseball player's BMI is 
below 21. You can use the < operator for this. Name the array light.
Print the array light.
Print out a numpy array with the BMIs of all baseball players whose BMI is below 21. Use light inside square brackets 
to do a selection on the bmi array.

# height_in and weight_lb are available as a regular lists

# Import numpy
import numpy as np

# Calculate the BMI: bmi
np_height_m = np.array(height_in) * 0.0254
np_weight_kg = np.array(weight_lb) * 0.453592
bmi = np_weight_kg / np_height_m ** 2

# Create the light array
light = bmi < 21
bmi[light]

# Print out light
print(light)

# Print out BMIs of all baseball players whose BMI is below 21
print(bmi[light])
"""
"""
# height_in and weight_lb are available as a regular lists

# Import numpy
import numpy as np

# Store weight and height lists as numpy arrays
np_weight_lb = np.array(weight_lb)
np_height_in = np.array(height_in)

# Print out the weight at index 50
print(np_weight_lb[50])

# Print out sub-array of np_height_in: index 100 up to and including index 110
print(np_height_in[100:111])
"""
"""
# Create baseball, a list of lists
baseball = [[180, 78.4],
            [215, 102.7],
            [210, 98.5],
            [188, 75.2]]
# Import numpy
import numpy as np

# Create a 2D numpy array from baseball: np_baseball
np_baseball = np.array(baseball)

# Print out the type of np_baseball
print(type(np_baseball))

# Print out the shape of np_baseball
print(np_baseball.shape)
"""