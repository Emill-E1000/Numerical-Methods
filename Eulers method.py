#%% Eulers method
#approximate y value for any x given y', x0 and y0
#first order diferential equations
import matplotlib.pyplot as plt
import math

#define the first derivative of Y
def Yprim(x, y):
    return 2 * x * y

def euler_method(Yprim, x0, y0, xf, h):
    # Calculate number of steps
    n = int((xf - x0) / h)
    
    # Initialize x and y variables and lists
    x, y = x0, y0
    X, Y = [x0], [y0]
    
    for i in range(1, n + 1):
        # Calculate value of yn
        y += h * Yprim(x, y)
        Y.append(y)
        
        # Calculate value of xn
        x += h
        X.append(x)

    return X, Y

#Initial values
x0 = 1
y0 = 1
xf = 1.5
h = 0.1

# Call the Euler method
X, Y = euler_method(Yprim, x0, y0, xf, h)

#%%Compare to value of y
Yreal = []
for i in range(len(X)):
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