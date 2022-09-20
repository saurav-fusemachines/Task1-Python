#NESTED LOOP WITHOUT LIST COMPHRESION
transposed = []
matrix = [[1, 2, 3, 4], [4, 5, 6, 8]]

for i in range(len(matrix[0])):
    transposed_row = []

    for row in matrix:
        transposed_row.append(row[i])
    transposed.append(transposed_row)

print(transposed)
print("*"*60)
# The above code use two for loops to find transpose of the matrix.
# We can also perform nested iteration inside a list comprehension. In this section, we will find transpose of a matrix using nested loop inside list comprehensio



#NESTED LOOP WITH LIST COMPRENSHION
matrix = [[1, 2], [3,4], [5,6], [7,8]]
transpose = [[row[i] for row in matrix] for i in range(2)]
print (transpose)

# In above program, we have a variable matrix which have 4 rows and 2 columns.
# We need to find transpose of the matrix. For that, we used list comprehension