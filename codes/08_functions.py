# temp1 = 77
# celsius1 = (temp1 - 32) * 5 / 9
# print(celsius1)
# temp2 = 95
# celsius2 = (temp2 - 32) * 5 / 9
# print(celsius2)
# temp3 = 50
# celsius3 = (temp3 - 32) * 5 / 9
# print(celsius3)

# 함수 사용

# def function_name(param_first, ...) :
#     execute codes (변수 + 약속어)
#     return result

def to_celsius(temp) :
    celsius = (temp - 3) * 5 / 9
    return celsius

pass

to_celsius(120)
temp1 = to_celsius(77)
print(temp1)

pass

temp2 = 100
result2 = to_celsius(temp2)
print(result2)

pass