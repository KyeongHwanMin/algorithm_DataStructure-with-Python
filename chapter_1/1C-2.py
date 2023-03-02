# 세 정수를 입력받아 중앙값 구하기 1
def med3(a,b,c):
    """a,b,c의 중앙값을 구하여 반환"""
    if a >= b:
        if b >= c:
            return b
        elif a <= c:
            return a
        else:
            return c
    elif a > c :
        return a
    elif b > c :
        return c
    else:
        return b
    
def med3_1(a,b,c):
    # 비효율적
    if (b >= a and c <= a) or (b <= a and c>=a):
        return a
    elif (a > b and c < b) or ( a < b and c > b):
        return b
    return c
    
print('세 정수의 중앙 값을 구합니다.')
a = int(input('정수 a의 값을 입력하세요.:'))
b = int(input('정수 b의 값을 입력하세요.:'))
c = int(input('정수 c의 값을 입력하세요.:'))

print(f'중앙값은 {med3(a,b,c)}입니다.')
print(f'중앙값은 {med3_1(a,b,c)}입니다.')