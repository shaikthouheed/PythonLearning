# Two dimensional array is an array within an array. It is an array of arrays. In this type of array the position of an data element is referred by two indices instead of one. So it represents a table with rows an dcolumns of data.

# In the below example of a two dimensional array, observer that each array element itself is also an array.

# Consider the example of recording temperatures 4 times a day, every day. Some times the recording instrument may be faulty and we fail to record data. Such data for 4 days can be presented as a two dimensional array as below.

# Day 1 - 11 12 5 2 
# Day 2 - 15 6 10 
# Day 3 - 10 8 12 5 
# Day 4 - 12 15 8 6 
# The above data can be represented as a two dimensional array as below.

# T = [[11, 12, 5, 2], [15, 6,10], [10, 8, 12, 5], [12,15,8,6]]

from array import *

T = [[11, 12, 5, 2], [15, 6,10], [10, 8, 12, 5], [12,15,8,6]]
for r in T:
   for c in r:
      print(c,end = " ")
   print()
  
#   Inserting Values

from array import *
T = [[11, 12, 5, 2], [15, 6,10], [10, 8, 12, 5], [12,15,8,6]]

T.insert(2, [0,5,11,13,6])

for r in T:
   for c in r:
      print(c,end = " ")
   print()
  
# Updating Values
# We can update the entire inner array or some specific data elements of the inner array by reassigning the values using the array index.

# Example
from array import *

T = [[11, 12, 5, 2], [15, 6,10], [10, 8, 12, 5], [12,15,8,6]]

T[2] = [11,9]
T[0][3] = 7
for r in T:
   for c in r:
      print(c,end = " ")
   print()
  
  
# Deleting the Values
# We can delete the entire inner array or some specific data elements of the inner array by reassigning the values using the del() method with index. But in case you need to remove specific data elements in one of the inner arrays, then use the update process described above.

# Example
from array import *
T = [[11, 12, 5, 2], [15, 6,10], [10, 8, 12, 5], [12,15,8,6]]

del T[3]

for r in T:
   for c in r:
      print(c,end = " ")
   print()
