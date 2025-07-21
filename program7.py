import numpy as np
a=np.array([[1,2,3,4],[5,6,7,8],[4,3,2,1]])
print("array elements are: ",a)
print("sum of array")
print(np.sum(a))
print("sum of each column")
print(np.sum(a,axis=0))
print("sum of each row")
print(np.sum(a,axis=1))

