#2D arrays are arrays of arrays.
#  In this example, we have a 2D array that contains 3 arrays with 3 elements each.
# 2D arrays are also known as matrices.
# 2D arrays are used to represent a table of values that have two dimensions.
# 2D arrays are used to represent a matrix.
# 2D arrays are used to represent a grid of values.
# 2D arrays are used to represent a table of values.

#example
# 2D array of integers
array1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(array1)

# 2D array of floating point numbers
array2 = [[1.1, 2.2, 3.3], [4.4, 5.5, 6.6], [7.7, 8.8, 9.9]]
print(array2)

# 2D array of characters
array3 = [['a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'h', 'i']]
print(array3)

# 2D array of strings
array4 = [['apple', 'banana', 'cherry'], ['date', 'elderberry', 'fig'], ['grape', 'honeydew', 'kiwi']]
print(array4)


#print the 2D array in a matrix format
for row in array1:
    print(row)

for row in array2:
    print(row)

for row in array3:
    print(row)

for row in array4:
    print(row)

#Accessing elements in a 2D array
#To access an element in a 2D array, you need to specify the row and column index.
#The row index specifies the row number, and the column index specifies the column number.
#The row index and column index are zero-based.
#The row index and column index are integers.
#The row index and column index are separated by a comma.
#The row index and column index are enclosed in square brackets.
#The row index is specified first, followed by the column index.
#The row index is specified before the column index.
#The row index is specified first, followed by the column index.
#The row index is specified before the column index.

#example
#Accessing elements in a 2D array
#Access the element at row 0, column 0
print(array1[0][0])

#Access the element at row 0, column 1
print(array1[0][1])


#Access the element at row 0, column 2
print(array1[0][2])
