# numpy func
import numpy as np

a= np.array([1,2,3])

print("One Dimensional",a)

b=np.array([[2,3,4,8,9,10,1],[5,6,7,9,12,11,10]])


print("two dimensional",b)
#get element-second row ,6th
print(b[1,5])
#get row first
print(b[0, :])
#get column third
print(b[:,2])
# getting alternative element of first row starting from 2pos
print(b[0,1:-1:2])
print("Dimension of a",a.ndim)

print("Shape of b",b.shape)
