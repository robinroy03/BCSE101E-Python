"""
Write a Python program for matrix addition and Multiplication using list comprehension
"""

#matrix multiplication
def matrix_multiplication():
    #for matrix_1
    row_count_1=int(input("Enter the number of rows for matrix 1 : "))
    column_count_1=int(input("Enter the number of columns  for matrix 1 : "))
    matrix_1=[] #initializing the matrix
    for i in range(1,row_count_1+1):
        row=[int(x) for x in input(f"Enter the elements in row {i} with space : ").split()]
        matrix_1.append(row)
    #matrix 1 is now ready
    #for matrix_2
    row_count_2=int(input("Enter the number of rows for matrix 2 : "))
    column_count_2=int(input("Enter the number of columns for matrix_2 : "))
    matrix_2=[] #initializing the matrix
    for i in range(1,row_count_2+1):
        row=[int(x) for x in input(f"Enter the elements in row {i} with space : ").split()]
        matrix_2.append(row)
    #matrix 2 is now ready
    #now the main logic :
    def element(r1,r2):
        """
        What this function does is it takes 2 rows, multiply them and returns value, row 2 is the transpose matrix_2
        """
        for i in range(len(r1)):
            yield (r1[i]*r2[i])
    def main():
        new_matrix=[]
        new_matrix.append([[sum(element(i,j)) for j in matrix_2_transpose] for i in matrix_1])
        return new_matrix
    if column_count_1==row_count_2:
        matrix_2_transpose=[[matrix_2[r][c] for r in range(row_count_2)] for c in range(column_count_2)]  #taking the transpose of matrix_2
        for i in main():
            for j in i:
                print(*j)
    else:
        print("Matrix multiplication not possible")
matrix_multiplication()

# matrix addition

row_count=int(input("Enter the number of rows in the matrix : "))
column_count=int(input("Enter the number of columns in the matrix : "))

matrix_1=[]   # elements are rows
matrix_2=[]

for i in range(row_count):
    matrix_1.append(list(map(int,input("Enter the matrix_1 rows : ").split())))

for i in range(row_count):
    matrix_2.append(list(map(int,input("Enter the matrix_2 rows : ").split())))

new_matrix = [[matrix_1[i][j] + matrix_2[i][j]  for j in range(len(matrix_1[0]))] for i in range(len(matrix_1))]

for i in new_matrix:
    print(*i,sep="\t")
print("Robin Roy\n22BRS1114")