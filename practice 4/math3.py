import math
num_s=int(input("Input number of sides: "))
len=float(input("Input the length of a side: "))
area=(num_s*len**2)/(4*math.tan(math.pi/num_s))
print("The area of the polygon is: ", area)