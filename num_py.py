
import numpy as np

print("--")
arr=np.array([1,2,3,4,5])
print(np.__version__)
print(arr)
print(type(arr))

#0d array
ar=np.array(32)
print(ar)
#2d array
ar=np.array([ [1,2,3] ,[3,2,1]])
print(ar)
for i in ar:
    print(i,'p')


#1d array
ar=np.array([1,9,3,4,5])
for i in ar:
    print(i)

#3d array
arr=np.array( [  [[1,2,3], [2,89] ] ,  [ [12,45],[90,70] ]  ])
print(arr[0,1,2])

#checking the dimension of an array

ar=np.array( [ [ 1,4,5,6 ] , [ 3,6,7,8 ] , [ 1 ] ] )
print(ar)
print(ar[1],"--",ar[0])
ar[0]=[9,9,9,9]
print(ar[1],"--",ar[0])
print(ar[2]+ar[0]+ar[1])

#seperating rows and column
ar=np.array([ [ [1,2,3],[88,99] ],
            [[32,32],[9,8]]
]
)
print(ar)
print(ar[0,2])

#SLICING

arr=np.array( [1,2,3,5,6,7] )
print(arr[1:2])
print(arr[:4])
print(arr[::4])
print(arr[-3:-1])
print(arr[2:5:1])
ar2=np.array([[1,3,5,7,87],[7,9,11,12,123]])
print(ar2[1, 1:2])
print(ar2[0:2,2])
print(ar2.dtype)

#COPYING

arr=np.array( [21,32,43,54] )
x=arr.copy()
y=arr.view()
z=x.view()
print(arr,"--",x)
arr[0]=90
print(arr,"--",x)
x[0]=222
print(arr,"--",x)
# IF THE DATA BELONGS TO THE ARRAY
print(x.base)
print(y.base,"_",z.base)


