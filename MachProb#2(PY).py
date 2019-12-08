import numpy as np
import pandas as pd
import math as m
print("**Use spaces in between inputting numbers**\n")
x1,y1 = map(float, input('Please input x1,y1: ').split())
x2,y2 = map(float, input('Please input x2,y2: ').split())
x3,y3 = map(float, input('Please input x3,y3: ').split())
#Lets the user input their x and y together

c = (x1-x2)**2 + (y1-y2)**2
a = (x2-x3)**2 + (y2-y3)**2
b = (x3-x1)**2 + (y3-y1)**2
s = 2*(a*b + b*c + c*a) - (a**2 + b**2 + c**2) 
px1 = (a*(b+c-a)*x1 + b*(c+a-b)*x2 + c*(a+b-c)*x3) / s
#Equations for the center of the circle
x = float(round(px1,3))
y = float(round(((a*(b+c-a)*y1 + b*(c+a-b)*y2 + c*(a+b-c)*y3) / s),3))

r1 = m.sqrt((x-x1)**2 + (y-y1)**2)
#Equations for the radius of the circle

r = float(round(r1,3))

D1=np.array([((x1**2)+(y1**2),y1,1),
             ((x2**2)+(y2**2),y2,1),
             ((x3**2)+(y3**2),y3,1)])

E1=np.array([((x1**2)+(y1**2),x1,1),
             ((x2**2)+(y2**2),x2,1),
             ((x3**2)+(y3**2),x3,1)])

F1=np.array([((x1**2)+(y1**2),x1,y1),
             ((x2**2)+(y2**2),x2,y2),
             ((x3**2)+(y3**2),x3,y3)])

L1 = np.array([(x1,y1,1),
               (x2,y2,1),
               (x3,y3,1)])

L = np.linalg.det(L1)
D = (-1*(np.linalg.det(D1)))/L
E = np.linalg.det(E1)/L
F = -1*(np.linalg.det(F1))/L

D = float(round(D,3))
E = float(round(E,3))
F = float(round(F,3))
#Solving for the coefficients, using the determinants to solve for the system of equations

CF = {'D':[D],'E':[E],'F':[F]}
Coefficients = pd.DataFrame(CF,columns=['D','E','F'])
#Using Pandas to create a dataframe to have the coefficients labeled 

print()
print()
print()
print("Radius of the said circle: \n", r,'\n')
print("Central coordinate (x, y) of the circle:\n (",x ,",", y,")\n")
print(Coefficients)
print("")
print("General Equation: \n")
print("x^2 + y^2 +",D,"x +",E,"y +",F,"=0")

