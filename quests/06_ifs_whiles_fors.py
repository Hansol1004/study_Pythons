# 문제1

second = "Programming"
first = "Welcome to Python Strings" + {second}   # 오류 발생

print(first)

# 오류 사항
# Exception has occurred: TypeError
# can only concatenate str (not "set") to str
#   File "/apps/study_Pythons/quests/123.py", line 2, in <module>
#     first = "Welcome to Python Strings" + {second}   # 오류 발생
#             ~~~~~~~~~~~~~~~~~~~~~~~~~~~~^~~~~~~~~~
# TypeError: can only concatenate str (not "set") to str

# 수정한 코드
second = "Programming"
first = "Welcome to Python Strings" + " " + second

print(first)

# 문제2
first = "Hello Python"

while first > 0:
    print(first)
    first = first - 1
# 오류 사항
# Exception has occurred: TypeError
# '>' not supported between instances of 'str' and 'int'
#   File "/apps/study_Pythons/quests/123.py", line 3, in <module>
#     while first > 0:
#           ^^^^^^^^^
# TypeError: '>' not supported between instances of 'str' and 'int'

# 수정한 코드
first = "Hello Python"

count = len(first)
while count > 0:
    print(first)
    count = count - 1

# 문제3
kor = [70, 80, 90, 40, 50]
eng = [90, 80, 70, 70, 60]
sum_all = 0

for k in kor:
    sum_all = sum_all + kor + eng     # 오류 위치

# 오류 사항
# Exception has occurred: TypeError
# unsupported operand type(s) for +: 'int' and 'list'
#   File "/apps/study_Pythons/quests/123.py", line 6, in <module>
#     sum_all = sum_all + kor + eng     # 오류 위치
#               ~~~~~~~~^~~~~
# TypeError: unsupported operand type(s) for +: 'int' and 'list'

# 수정한 코드
kor = [70, 80, 90, 40, 50]
eng = [90, 80, 70, 70, 60]
sum_all = 0

for k in kor:
    sum_all = sum_all + k

for e in eng:
    sum_all = sum_all + e

print(sum_all)

# 문제4
kor = [70, 80, 90, 40, 50]
eng = [90, 80, 70, 70, 60]

sum_total = 0

for i in range(0, 10):    # 오류 발생
    sum_total = sum_total + kor[i] + eng[i]

# 오류 사항
# Exception has occurred: IndexError
# list index out of range
#   File "/apps/study_Pythons/quests/123.py", line 7, in <module>
#     sum_total = sum_total + kor[i] + eng[i]
#                             ~~~^^^
# IndexError: list index out of range

kor = [70, 80, 90, 40, 50]
eng = [90, 80, 70, 70, 60]

sum_total = 0

for i in range(len(kor)):
    sum_total = sum_total + kor[i] + eng[i]

print(sum_total)