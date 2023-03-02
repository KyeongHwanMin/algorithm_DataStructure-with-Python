x = [[1,2,3],[4,5,6]]
y = x.copy()
x[0][1]=9
print(id(x))
print(id(y))

import copy
# x = [[1,2,3],[4,5,6]]
y = copy.deepcopy(x)
print(id(x))
print(id(y))