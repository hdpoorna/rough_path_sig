"""
s_x_lev3.py
@author: Poorna
Python 2.7
"""

def split_x1x2 (data) :
    "Splits data points into X1 and X2 lists"
    X1_temp = []
    X2_temp = []
    for point in data :
        X1_temp.append(float(point[0]))
        X2_temp.append(float(point[1]))
    return X1_temp, X2_temp

def s_x_lev2 (dim1, dim2, i, j, X1_list, X2_list) :
    "Computes members of level 2 signature for any t_i < t_j"
    if dim1 == 1 :
        dim1 = X1_list
    else :
        dim1 = X2_list              # Assuming the user inputs data correctly
        
    if dim2 == 1 :
        dim2 = X1_list
    else :
        dim2 = X2_list              # Assuming the user inputs data correctly
        
    tot = 0
    for m in range (i, j) :
        integ = (dim2[m+1] - dim2[m])*((dim1[m] - dim1[i]) + 0.5*(dim1[m+1] - dim1[m]))
        tot += integ
    return tot

def s_x_lev3 (dim1of3, dim2of3, dim3of3, i_0, j_0, X1_list_0, X2_list_0) :
    "Computes members of level 3 signature for any t_i < t_j"
    if dim1of3 == 1 :
        dim1_list = X1_list_0
    else :
        dim1_list = X2_list_0              # Assuming the user inputs data correctly
        
    if dim2of3 == 1 :
        dim2_list = X1_list_0
    else :
        dim2_list = X2_list_0              # Assuming the user inputs data correctly
        
    if dim3of3 == 1 :
        dim3_list = X1_list_0
    else :
        dim3_list = X2_list_0              # Assuming the user inputs data correctly
        
    tot_0 = 0
    for n in range (i_0, j_0) :
        integ_0 = (dim3_list[n+1] - dim3_list[n])*(s_x_lev2(dim1of3, dim2of3, i_0, n, X1_list_0, X2_list_0)
                                                    +(dim1_list[n] - dim1_list[i_0])*(dim2_list[n+1] - dim2_list[n])/2.0
                                                    +(dim1_list[n+1] - dim1_list[n])*(dim2_list[n+1] - dim2_list[n])/6.0)
        tot_0 += integ_0
    return tot_0

# data_pts = input("Enter data points as a list of tuples : ")
default = [(1,0),(0.707,0.707),(0,1),(-0.707,0.707),(-1,0),(-0.707,-0.707),(0,-1),(0.707,-0.707),(1,0)]
data_pts = default

X1, X2 = split_x1x2(data_pts)
print ""
print "X1 = " + str(X1)
print "X2 = " + str(X2)
print ""

t_i = input("Enter i of t_i (<t_j) : ")
t_j = input("Enter j of t_j (>t_i) : ")
print ""
for k in [1,2] :
    for l in [1,2] :
        for p in [1, 2] :
            print "S(X)_" + str(k) + "," + str(l) + "," + str(p) + " = " + str(s_x_lev3(k,l,p,t_i,t_j,X1,X2))