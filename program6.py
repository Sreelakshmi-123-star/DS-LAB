import numpy as np
a=np.array([[1,2,3,4],[4,3,2,1]])
b=np.array([[5,6,7,8],[8,7,6,5]])
print("first array",a)
print("second array",b)
if np.array_equal(a,b):
	print("equal")
else:
	print("not equal")

