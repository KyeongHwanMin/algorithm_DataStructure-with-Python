# 함수 내부'외부에서 정의한 변수와 객체의 식별 번호를 출력하기

n = 1
y = n
def put_id():
    x = n
    z = 1
    print(f'id(x) = {id(x)}')
    print(f'id(z) = {id(z)}')
    
print(f'id(1) = {id(1)}')
print(f'id(n) = {id(n)}')
print(f'id(y) = {id(y)}')
put_id()