from collections import defaultdict

# ------------ INPUT MATRICES (Edit as needed) ------------ #

# A is m x n
A = [
    [1, 2, 3],
    [4, 5, 6]
]

# B is n x p
B = [
    [7, 8],
    [9, 10],
    [11, 12]
]

# Dimensions
m = len(A)         # rows in A
n = len(A[0])      # cols in A == rows in B
p = len(B[0])      # cols in B

# ------------- MAP PHASE -------------

mapped = []

# Map from A
for i in range(m):
    for j in range(n):
        for k in range(p):
            mapped.append(((i, k), ('A', j, A[i][j])))

# Map from B
for j in range(n):
    for k in range(p):
        for i in range(m):
            mapped.append(((i, k), ('B', j, B[j][k])))

# ------------- SHUFFLE PHASE -------------

shuffle = defaultdict(list)
for key, value in mapped:
    shuffle[key].append(value)

# ------------- REDUCE PHASE -------------

result = defaultdict(int)

for key in shuffle:
    a_dict = defaultdict(int)
    b_dict = defaultdict(int)

    for tag, j, val in shuffle[key]:
        if tag == 'A':
            a_dict[j] = val
        elif tag == 'B':
            b_dict[j] = val

    total = 0
    for j in range(n):
        total += a_dict.get(j, 0) * b_dict.get(j, 0)

    result[key] = total

# ------------- PRINT RESULT MATRIX -------------

print("Resultant Matrix C (A x B):")
for i in range(m):
    row = []
    for k in range(p):
        row.append(result[(i, k)])
    print(row)
