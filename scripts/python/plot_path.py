"""
Created on Mon Apr 02 22:59:53 2018
@author: Poorna
"""

import matplotlib.pyplot as plt

def split_x1x2 (data) :
    "Splits data points into X1 and X2 lists"
    X1_temp = []
    X2_temp = []
    for point in data :
        X1_temp.append(float(point[0]))
        X2_temp.append(float(point[1]))
    return X1_temp, X2_temp

def plot_path (X1_list, X2_list) :
    "Plots a 2D path obtained from piecewise linear interpolation"
    plt.plot(X1_list,X2_list,'b-')
    plt.plot(X1_list,X2_list,'ro')
    plt.xlabel('X1')
    plt.ylabel('X2')
    plt.grid(True)
    plt.show()
    return

data_pts = input("Enter data points as a list of tuples : ")
# default = [(1,0),(0.707,0.707),(0,1),(-0.707,0.707),(-1,0),(-0.707,-0.707),(0,-1),(0.707,-0.707),(1,0)]
X1, X2 = split_x1x2(data_pts)
print ""
print "X1 = " + str(X1)
print "X2 = " + str(X2)
plot_path(X1, X2)