from numpy import *

# Coordinates of the 2D points

# x = r_[  9, 35, -13,  10,  23,   0]
# y = r_[ 34, 10,   6, -14,  27, -10]

x = r_[249, 461, 254, 462, 256, 461, 259, 459, 255, 455, 257, 453]
y = r_[640, 640, 645, 645, 650, 650, 655, 655, 660, 660, 665, 665]

# R0 = 25
# nb_pts = 8
# dR = 2
# angle =9*pi/5
# x = (10 + R0*cos(theta0) + dR*random.normal(size=nb_pts)).round()
# y = (10 + R0*sin(theta0) + dR*random.normal(size=nb_pts)).round()


# == METHOD 1 ==
method_1 = 'algebraic'

# coordinates of the barycenter
x_m = mean(x)
y_m = mean(y)

# calculation of the reduced coordinates
u = x - x_m
v = y - y_m

# linear system defining the center in reduced coordinates (uc, vc):
#    Suu * uc +  Suv * vc = (Suuu + Suvv)/2
#    Suv * uc +  Svv * vc = (Suuv + Svvv)/2

Suv = sum(u*v)
Suu = sum(u**2)
Svv = sum(v**2)
Suuv = sum(u**2 * v)
Suvv = sum(u * v**2)
Suuu = sum(u**3)
Svvv = sum(v**3)

# Solving the linear system
A = array([ [ Suu, Suv ], [Suv, Svv]])
B = array([ Suuu + Suvv, Svvv + Suuv ])/2.0
uc, vc = linalg.solve(A, B)

xc_1 = x_m + uc
yc_1 = y_m + vc

# Calculation of all distances from the center (xc_1, yc_1)
Ri_1 = sqrt((x-xc_1)**2 + (y-yc_1)**2)
R_1 = mean(Ri_1)
residu_1 = sum((Ri_1-R_1)**2)
residu2_1= sum((Ri_1**2-R_1**2)**2)

# Decorator to count functions calls
import functools
def countcalls(fn):
    "decorator function count function calls "

    @functools.wraps(fn)
    def wrapped(*args):
        wrapped.ncalls +=1
        return fn(*args)

    wrapped.ncalls = 0
    return wrapped

print(Ri_1)
print(R_1)
print(residu_1)
print(residu2_1)
