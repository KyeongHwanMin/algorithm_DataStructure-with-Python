# 각 배열 원소의 최댓값을 구해서 출력하기(튜플, 문자열, 문자열 리스트)

from max import max_of

t = (4, 7, 5.6, 2, 3.14, 1)
s = 'string'
a = ['DTS', 'AAC', 'FLAC']

print(f'{t}의 최댓값은 {max_of(t)}입니다.')
print(f'{s}의 최댓값은 {max_of(s)}입니다.')
print(f'{a}의 최댓값은 {max_of(a)}입니다.')

print(max(t))


a = 3
b = a
print(a,b)
a = 4
print(a,b)

list1 = [1,2,3,4,5]
list2 = list1
print(list1 is list2)
list1[2]=9
print(list1)
print(list2)