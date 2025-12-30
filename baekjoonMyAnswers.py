# 백준 Python3 단계별 학습 노트


# 1단계 입출력과 사칙연산 (시작 날 25. 12. 30)

# 문제 번호 2557
# Hello World!를 화면에 출력하는 문제 (예제 출력과 똑같이 출력해야 합니다.)
print('Hello World!')

# 문제 번호 1000
# 두 수를 입력받고 합을 출력하는 문제
a, b = map(int, input().split())
# map()로 input 한 번에 두 수 입력 "1 2" 후 문자열을 정수로 바꿔줌
# 혹시 입력때 '01 2' 이런식으로 입력될 경우 01을 정수로 바꾸는 과정에서오류가 생기기 때문에 split() 사용
print(a+b)

# 문제 번호 1001
# 두 수를 입력받고 뺄셈을 한 결과를 출력하는 문제
a, b = map(int, input().split())
print(a-b)

# 문제 번호 10998
# 곱셈 문제
a, b = map(int, input().split())
print(a-b)

# 문제 번호 1008
# 나눗셈 문제. 이 문제에는 "스페셜 저지" 표시가 붙어 있는데, 이것은 예제 출력과 꼭 똑같이 출력할 필요는 없고 조건에 맞는 답을 출력하면 된다는 뜻입니다.
a, b = map(int, input().split())
print(a/b)

# 문제 번호 10869
# 모든 사칙연산 문제
a, b = map(int, input().split())
print(a+b)
print(a-b)
print(a*b)
print(a//b) # 요구조건 몫
print(a%b) # 요구조건 나머지

# 문제 번호 10926
# 입출력을 응용하는 문제
