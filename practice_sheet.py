# ✅ **문제:
# 두 개의 숫자 리스트를 이용해 사칙연산(+, -, , /)을 수행하는 함수를 구현하시오.*
# 조건
# 테스트 데이터는 리스트(list) 로만 제공


# 테스트 데이터 개수는 10개


# 변수명은 소문자 + _ 조합


# 함수는 두 숫자를 입력받아 덧셈, 뺄셈, 곱셈, 나눗셈 결과를 모두 반환


# 0으로 나누는 경우는 "division_error" 반환

test_data1 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
test_data2 = [2, 4, 0, 8, 10, 12, 14, 16, 18, 20]

add = [0] * 10
sub = [0] * 10
mul = [0] * 10
div = [0] * 10
result = [0] * 10

def calcualter(number1, number2) :
    for i in range(len(test_data1)) :
        add[i] = number1[i] + number2[i]
        sub[i] = number1[i] - number2[i]
        mul[i] = number1[i] * number2[i]
        div[i] = number1[i] / number2[i]
        if number2 == 0 :
            div = "division_error"
    return add, sub, mul, div
result = calcualter(test_data1, test_data2)    