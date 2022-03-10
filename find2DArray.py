import numpy as np


arr = np.array([[1,2],[1,1]])

# apply method
lis = arr.tolist()

rows,columns = arr.shape

list =[*range(0,rows)] 
list1=[*range(columns-1,-1,-1)]
list.extend(list1)

list = [j for sub in arr for j in sub]
count = 0
lis = []
for curr in list:
    for i in range(rows):
        for j in range(columns):
        
            if(curr == arr[i][j]):
                count = count+1
        
    if(count>1):
        lis.append(count)
    else:
        lis.append(count)
    count=0

print(lis)
# lis.reshape(arr.shape)
indices = [index for index, element in enumerate(lis) if element == 1]
print(list)
print(indices)

for i, e in enumerate(arr):
    for j, ee in enumerate(e):
        if list[indices[0]] == ee:
            print(arr[i][j])
            print('{0} and {1}'.format(i,j))