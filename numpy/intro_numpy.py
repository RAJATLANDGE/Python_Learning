import numpy as np
# importance of numpy array
#1) less memory
#2)fast
#3)convinient

myarr = np.array([12,23,5,6,98])                             # crete numpy array #1D array
print(myarr)

myarr2 = np.array([[12,23,56,89,75,52],[12,25,58,69,63,85],[1,2,3,5,9,8]],dtype=np.int32)#crete numpy array with 32bytes #2D array
print(myarr2)
print(myarr2.ndim)                       #to know the dimention of the array
print(myarr2.itemsize)                   #to know the size of any one element
print(myarr2.dtype)                      # to know the type of array

print(myarr[2])                        #accessing 1D array element
print(myarr2[0,2])                     #accessing 2D array element
print(myarr2[0:2,2])                   # accessing the element of first and second row of 3rd(2nd index) element at one time

print(myarr2.shape)                    #give the info of (row,column)
print(myarr.dtype)                     # give the info of array in  byte

myarr2[0,1] = 32                        #to change array element
print(myarr2)

# iteration on array
for item in myarr2:
    print("item",item)

for item in myarr2.flatten():                            #flat give each element separately
    print("flat",item)

for x in np.nditer(myarr2,order="f",flags=["external_loop"]):                  #order C= row by row   F= column by column
    print(x)                                                     #flags give bunch of element

# for x in np.nditer(myarr2,op_flags=["readwrite"]):
#     print(x)

# print(myarr2)
a = np.arange(16,40,2).reshape(3,4)             #.reshape(row,column)   row-->, column |
b = np.arange(3,15,4).reshape(3,1)
print(a)
print(b)
for x,y in np.nditer([a,b]):                             #iterate two array simultaneously
    print("x and y",x,y)


#array creation method
"""
There are 6 general mechanisms for creating arrays:
    1)Conversion from other Python structures (i.e. lists and tuples)
    2)Intrinsic NumPy array creation functions (e.g. arange, ones, zeros, etc.) 
    3)Replicating, joining, or mutating existing arrays
    4)Reading arrays from disk, either from standard or custom formats
    5)Creating arrays from raw bytes through the use of strings or buffer
    6)Use of special library functions (e.g., random)
"""
# Conversion from other Python structures
listarray = np.array([[1,2,3],[5,8,5],[0,3,1]])                  #generally array created only with integer or float
print(listarray)
print("array dtype =", listarray.dtype)
print("array shape", listarray.shape)
print("array size", listarray.size)

# Intrinsic NumPy array creation functions (e.g. arange, ones, zeros, etc.)

zeros = np.zeros((2,6))                                         #create array with pass zero as element(row, column)
print(zeros)

ones = np.ones((2,6))                                         #create array with one as element (row, column)
print(ones)

rng = np.arange(12)                                             #create array with n-1 range
print(rng)

sst = np.arange(1,10,2)                                      # here we pass start stop and step parameter
print("sst", sst)

lspace = np.linspace(1,5,12)                           # create array with 12 element between 1 to 5 with equally linearly space.
print(lspace)

epm = np.empty((4,6))                              # create array with pass row and column values with random element
print("epm",epm)

emp_like = np.empty_like(lspace)          # Return a new array with the same shape and type as a given array.
print(emp_like)

idn = np.identity(10)                                # return the identity matrix with n*n88
print(idn)

reshp = rng.reshape((3,4))                          # reshape the array with equally distributed array
print(reshp)
arrr = np.arange(99)
arrr = arrr.reshape((3,33))                     # here arrr change in shape to 2d array
print(arrr)

print("**********")
arr2 = arrr.ravel()    # for flatten your array i.e make 1d array # it does not change on original data it return the new data
print(arrr)
print(arr2)
# row = x- axis = axis 1
# column = y- axis = axis 0

x = [[1,2,3], [4,5,6], [7,1,0]]
ar = np.array(x)
print(ar)

sm = ar.sum(axis=0)       #0 =  coloumn   1 = row
print(sm)
sm1 = ar.sum(axis=1)
print(sm1)

print(np.std(ar))            #standard deviation

tpt = ar.T                 #transpose the array
print(tpt)

print(ar.flat)                                   #give iterator type object on which we can iterate loop

print(ar.ndim)                                   # give dimension of pass array

print(ar.size)                                   # give the element of pass array

print(ar.nbytes)                                 # give the no. of bytes consume by pass array

# on 1D array
one = np.array([1,3,4,634,2])
print(one.argmax())                              # give the index of max element
print(one.argmin())                              # give the index of min element
print(one.argsort())                             # give the sorted index of given array

# on 2D array
print(ar)
print(ar.argmax())
print(ar.argmin())
print(ar.argmax(axis = 0))
print(ar.argmin(axis=1))
print(ar.argsort(axis=0))

print("rrr",ar.ravel())
print(ar.reshape(9,1))

ar2 = np.array([[1,2,1],[4,0,6],[8,1,0]])
print(ar2)
print(ar + ar2)                   #add row wise
print(ar * ar2)
print(ar.dot(ar2))                # give matrix product

print(np.sqrt(ar))                                # give squareroot of each element
print(ar.sum())
print(ar.max())
print(ar.min())
print(np.where(ar>5))                                           # give the index of (r,c) of element greater than 5.
print(np.count_nonzero(ar))

import sys
py_ar = [0,4,55,2]
np_ar = np.array([0,4,55,2])              #convert python list to numpy array

print(sys.getsizeof(py_ar))
print(np_ar.itemsize * np_ar.size)

print(np_ar.tolist())                           # convert numpy array to python list

a = np.arange(6).reshape(3,2)
b = np.arange(6,12).reshape(3,2)
print(a)
print(b)
vst = np.vstack((a,b))                                  # join two array vertically
hst = np.hstack((a,b))                                  # join two array horizontally
print(vst)
print(hst)


a= np.arange(30).reshape(2,15)
print(a)
result = np.hsplit(a,3)                              # 3 means to split array into 3 equal parts in horizontal
print(result)
print(result[0])
print(result[1])
print(result[2])

rst = np.vsplit(a,2)                                 # vertically split in 2 equal parts
print(rst[0])
print(rst[1])

p = np.arange(12).reshape(3,4)
print(p)
q= p>4
print(q)
print(p[q])             # by this way we only access true value element of the q
p[q]=-8                 # by this way we can replace the true value with pass value
print(p)