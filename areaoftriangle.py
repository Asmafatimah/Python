import sys
#need it to access command-line arguments
import math
#to use math.sqrt() (square root function)
#float() converts the arguments from string to number
s1=float(sys.argv[1])
s2=float(sys.argv[2])
s3=float(sys.argv[3])
s=(s1+s2+s3)/2
area=math.sqrt(s*(s-s1)*(s-s2)*(s-s3))
print(f"area of triangle is: {area:.2f}")
