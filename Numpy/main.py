import numpy as np

# Creating the matrix
m1 = np.array([[1,2,3],[4,5,6]])


# # checking the shape size and dimesion of the matrix
# print("shape of the matrix",m1.shape)
# print("size of the matrix",m1.size)
# print("dimension of the matrix",m1.ndim)


# creating matrix with one and zeros
zero = np.zeros((3,3))
ones = np.ones((2,5))


# as we created add function in matrix calculater it is more optimize in numpy
array_1 = np.array([1,2,3])
array_2 = np.array([4,5,6])
sum_of_array = array_1 + array_2

# print(sum_of_array)



'''
🎯 Your First "Project Unknown" ChallengeTo officially kick off Month 2, I want you to try this without my help first.
Task: 1. Create a $4 \times 4$ matrix where every number is a 5.
2. Using indexing (no loops!), change the four numbers in the very middle to 0.
3. Print the result.
Hint: Think of it like slicing a list, but with a comma: matrix[row_start:row_end, col_start:col_end].

'''
# array_new = np.array([[5 for _ in range(4)] for _ in range(4)])
# array_new[1:2,0:4] = 0
# print(array_new)

# array_new = np.full((4,4),5)
# array_new[1:3,1:3] = 0
# # print(array_new)


# check = np.full((5,5),1)
# # Fill every 2nd col of even rows (0, 2, 4) starting at col 1
# check[0::2, 1::2] = 0

# # Fill every 2nd col of odd rows (1, 3) starting at col 0
# check[1::2, 0::2] = 0
# print(check)


