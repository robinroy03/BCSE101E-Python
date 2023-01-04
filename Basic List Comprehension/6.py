# to find matrix transpose

row_count=int(input("Enter the number of rows in the matrix : "))
column_count=int(input("Enter the number of columns in the matrix : "))

matrix=[]   # elements are rows

for i in range(row_count):
    matrix.append(list(map(int,input("Enter the matrix_1 rows : ").split())))

matrix_transpose=[[matrix[r][c] for r in range(row_count)] for c in range(column_count)]

print("Original Matrix : ")
for i in matrix:
    print(*i,sep="\t")

print("Transpose Matrix : ")

for i in matrix_transpose:
    print(*i,sep="\t")

print("Robin Roy\n22BRS1114")