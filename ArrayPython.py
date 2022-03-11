# First method to create a 1 D array
N = 5
arr = [0]*N
print(arr)

# Output: 
# [0, 0, 0, 0, 0]


# Second method to create a 1 D array
N = 5
arr = [0 for i in range(N)]
print(arr)

# Output: 
# [0, 0, 0, 0, 0]

# Using above first method to create a
# 2D array
rows, cols = (5, 5)
arr = [[0]*cols]*rows
print(arr)

# Output
# [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]



# Using above second method to create a
# 2D array
rows, cols = (5, 5)
arr = [[0 for i in range(cols)] for j in range(rows)]
print(arr)

# Ouput
# [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]








# Using above second method to create a
# 2D array
rows, cols = (5, 5)
arr=[]
for i in range(rows):
    col = []
    for j in range(cols):
        col.append(0)
    arr.append(col)
print(arr)


# Output: 
# [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]



#BestWay to declare Arrays, otherwise shallowcopy problem will occur

rows, cols = (5, 5)
arr = [[0 for i in range(cols)] for j in range(rows)]
