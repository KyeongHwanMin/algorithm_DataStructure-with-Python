# 리스트의 모든 원소를 스캔하기(인덱스값을 사용하지 않음)

x = ['John', 'George', 'Paul', 'Ringo']

for i in x:
    print(i)

l = ['a', 'b', 'c']
t = ('a', 'b', 'c')
d = {'a': 1, 'b': 2, 'c': 3}
s = 'abc'

l.reverse()  # list의 순서를 뒤집어줌
print(l)
#t.reverse()  # AttributeError: 'tuple' object has no attribute 'reverse'
#d.reverse()  # AttributeError: 'dict' object has no attribute 'reverse'
#s.reverse()  # AttributeError: 'str' object has no attribute 'reverse'

y = list(reversed(l))
print(y)