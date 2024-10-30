#Improved Eulers Method
#approximate y value for any x given y', x0 and y0
#first order diferential equations
import matplotlib.pyplot as plt
import math


#initial x value
x0 = 1
#initial y value
y0 = 1
#final value of x
xf = 1.5
#step size
h = 0.1
#number of steps
n = (xf-x0)/h

#Initialize x and y variables and vectors 
x, y = x0, y0
yapprox = y0
X, Y = [x0], [y0]
for i in range(1,int(n)+1):
    print(i)
    #function for y'
    Yprim = 2*x*y
    yapprox += h*(2*x*y)
    #calculate value of yn
    y += h*((2*(x+h)*yapprox)+(2*x*y))/2
    Y.append(y)
    #calculate value of xn
    x += h
    X.append(x)

#%%Compare to value of y
Yreal = []
for i in range(0,int(n)+1):
    x= X[i]
    Yreal.append(math.exp((x**2)-1))

yreal = math.exp(xf**2-1)

#%%Plot graphs
plt.figure(1)
plt.plot(X,Y,label="eulers method")
plt.plot(X,Yreal,label="Expected Value")
plt.xlim(x0, xf+h)
plt.xlabel("X values")      
plt.ylabel("Y values")    
plt.legend()  
plt.show

#%%Print results
print("Expected y value = ",yreal)
print("Approximated y value = ",Y[-1])
print("Absolut error = ",yreal-Y[-1])
print("Relative error % = ", (yreal-Y[-1])/yreal*100)