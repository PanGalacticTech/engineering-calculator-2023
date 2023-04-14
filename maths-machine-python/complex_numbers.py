'''
complex-numbers

Rectangular Form:   z = x+iy
Polar Form      :   z = r(cos(theta) + i sin(theta))
Where r = |z|= SQRT(x^2 + y^2)
x = r cos(theta)
y = r sin(theta)
θ=tan-1(y/x) for x>0
θ=tan-1(y/x)+π or
θ=tan-1(y/x)+180° for x<0 .


https://byjus.com/maths/polar-form-of-complex-numbers/#:~:text=The%20polar%20form%20of%20a,combination%20of%20modulus%20and%20argument.
'''

'''
https://www.tutorialspoint.com/how-to-plot-a-function-defined-with-def-in-python-matplotlib
'''

import math
import matplotlib
import numpy as np
from matplotlib import pyplot as plt

plt.rcParams["figure.figsize"] = [10, 10]
plt.rcParams["figure.autolayout"] = True



real = 7
imaginary =7

def complex_num_main():
    print("Complex Number Calculations")
    print(return_r(real, imaginary))
    print(return_r_as_square(real,imaginary))
    print(return_theta(real,imaginary))
    print(return_polar(real, imaginary))
    print(return_exponential(real,imaginary))
    plot_xy(real,imaginary)


def return_r(real, imaginary):
    r = math.sqrt((real**2)+(imaginary**2))
    return r

def return_r_as_square(real, imaginary):
    r = (real**2)+(imaginary**2)
    output = f"sqrt({r})"
    return output

def return_theta(real, imaginary):
    theta = math.atan(imaginary/real)
    if real < 0:
        theta += math.pi
    return theta




'''
The polar form
z = r(cos(theta) + i sin(theta))
'''
def return_polar(real, imaginary):
    r = return_r(real, imaginary)
    #r = return_r_as_square(real, imaginary)
    try:
        r = round(r, 4)
    except:
        print()
    theta = return_theta(real, imaginary)
    theta = round(theta, 4)
    Z = f"{r}(cos({theta}) + i sin({theta}))"
    return Z


def make_exponential(r,theta):
    Z = f"{r}e^(i{theta})"
    return Z

def return_exponential(real, imaginary):
    r = return_r(real,imaginary)
    r = round(r, 4)
    theta = return_theta(real, imaginary)
    theta = round(theta, 4)
    Z = make_exponential(r, theta)
    return Z

def plot_xy(x, y):
    #size and colour
    size = 20
    color = np.arange(-8,8)*20
    #plot
    fig, ax = plt.subplots()
    gridlinex = np.arange(-8,8)
    gridliney= np.arange(-8,8)

    ax.scatter(gridlinex, gridliney, s=size, c=color, vmin=0, vmax=100)
    #ax.scatter(x,y, s=size, c=color, vmin=0,vmax=100)
    ax.set(xlim=(-8,8),xticks=np.arange(-8,9),ylim=(-8,8), yticks=np.arange(-8,9))
    plt.show()


complex_num_main()