# 문제1

# 아래 함수는 섭씨 변환 후 값을 반환해야 한다.
# 현재 코드에서 발생하는 오류를 찾고 수정하시오.

# def to_celsius(temp):
#     celsius = (temp - 32) * 5 / 9
#     # return 문이 없음

# result = to_celsius(77)
# print(result)

# 해결 방안

def to_celsius(temp):
    celsius = (temp - 32) * 5 / 9
    return celsius

result = to_celsius(77)
print(result)

# 문제2

# 아래 프로그램은 실행 시 오류가 발생한다.
#  오류 위치를 찾고 올바르게 수정하시오.
# def convert(temp):
#     return (temps - 3) * 5 / 9   # 오타: temps

# print(convert(95))

# 해결 방안

def convert(temp):
    return (temp - 3) * 5 / 9   # 오타: temps

print(convert(95))

# 문제3

# 아래 코드는 함수 호출이 잘못되어 있다.
#  오류를 설명하고 고치시오.
# def to_celsius(temp):
#     return (temp - 32) * 5 / 9

# value = to_celsius()
# print(value)

# 해결 방안

def to_celsius(temp):
    return (temp - 32) * 5 / 9

value = to_celsius(55)
print(value)

# 문제4

# 아래 코드는 문자열을 함수에 전달하여 오류가 발생한다.
#  이 오류가 왜 발생하는지 설명하고 해결하시오.
# def to_celsius(temp):
#     return (temp - 3) * 5 / 9

# print(to_celsius("77"))

# 해결 방안

def to_celsius(temp):
    return (temp - 3) * 5 / 9

print(to_celsius(77))

# 문제5

# 아래 코드는 여러 값을 함수로 변환하려 하지만 오류가 발생한다.
#  오류 원인을 찾고 고치시오.(Option : for 문을 함수화)

# def to_celsius(temp):
#     return (temp - 3) * 5 / 9

# temps = [77, 95, 50]
# results = []

# for t in temps:
#     result = to_celsius(temp)   # 변수명 오류
#     print(results)

# 해결 방안

def to_celsius(temp):
    return (temp - 32) * 5 / 9

temps = [77, 95, 50]
results = [0] * len(temps)

for i in range(len(temps)):
    results[i] = to_celsius(temps[i])

print(results)

