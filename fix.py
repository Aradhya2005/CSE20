m, n = 3, 3       # matrix dimensions
scalar = 5
A = [ [1, 0, 0],
      [0, 1, 0],
      [0, 0, 1] ]
B = []

for i in range(m):
    row = []  # Fixed: Initialize an empty list for each row in B
    for j in range(n):
        row.append(A[i][j] * scalar)  # Fixed: Calculate the scalar multiplication and append it to the row
    B.append(row)  # Fixed: Append the row to matrix B
    A.copy(row)

# Print the resultant matrix B
for row in B:
    print(row)
