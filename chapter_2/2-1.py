# 학생 5명의 시험 점수를 입력받아 합계와 평균을 출력하기

print('학생 그룹 점수의 합계와 평균을 구합니다.')

score1 = int(input('1번 학생의 점수를 입력하세요.: '))
score2 = int(input('1번 학생의 점수를 입력하세요.: '))
score3 = int(input('1번 학생의 점수를 입력하세요.: '))
score4 = int(input('1번 학생의 점수를 입력하세요.: '))
score5 = int(input('1번 학생의 점수를 입력하세요.: '))

total = 0
total += score1
total += score2
total += score3
total += score4
total += score5

print(f'합계는 {total}점입니다.')
print(f'평균은 {total / 5}점 입니다.')

"""
리스트 내포
내포 표기 생성 : 리스트 안에서 for, if 문을 사용하여 새로운 리스트를 생성하는 기법
"""
numbers = [1, 2, 3, 4, 5]
twise = [num * 2 for num in numbers if num % 2 == 1]
print(twise)