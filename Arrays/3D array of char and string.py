#3d array of string and characters
array3 = [[['a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'h', 'i']],
         [['j', 'k', 'l'], ['m', 'n', 'o'], ['p', 'q', 'r']],
         [['s', 't', 'u'], ['v', 'w', 'x'], ['y', 'z', 'A']]]
for row in array3:
    print(row)

array4 = [[['apple', 'banana', 'cherry'], ['date', 'elderberry', 'fig'], ['grape', 'honeydew', 'kiwi']],
        [['lemon', 'mango', 'nectarine'], ['orange', 'papaya', 'quince'], ['raspberry', 'strawberry', 'tangerine']],
        [['ugli', 'vanilla', 'watermelon'], ['ximenia', 'yuzu', 'zucchini'], ['apricot', 'blueberry', 'cantaloupe']]]

for row in array4:
    print(row)
#Accessing elements in a 3D array
#To access an element in a 3D array, you need to specify the index of the row, column, and depth.
#The row index specifies the row number, the column index specifies the column number, and the depth index specifies the depth number.
#The row index, column index, and depth index are zero-based.
#The row index, column index, and depth index are integers.
#EXAMPLE
#Access the element at row 0, column 0, depth 0
print(array3[0][0][0])

