# 문제 1

frist = 5   # 오타

while first > 0:
    print(f"while 값 : {first}")
    first = first - 1

# 문제 발생 원인 
# Exception has occurred: NameError
# name 'first' is not defined
#   File "/apps/study_Pythons/quests/05_ifs_whiles.py", line 5, in <module>
#     while first > 0:
#           ^^^^^
# NameError: name 'first' is not defined

# 수정된 사항
first = 5 

while first > 0:
    print(f"while 값 : {first}")
    first = first - 1


# 문제2 
first = 5

while first > 0:
print(f"while 값 : {first}")  # 들여쓰기 문제
    first = first - 1

# 문제 발생 원인
# Exception has occurred: IndentationError

# 수정된 사항
first = 5

while first > 0:
    print(f"while 값 : {first}")
    first = first - 1

# 문제3
first = 5

while first > 0:
    print(f"while 값 : {first}")
    if first < 3:
        print("break 실행")
        break
    first = first - 1

# 문제 발생 원인
# 문제점은 if first < 3: 조건문입니다.                                                                                                                                                                   █                                                                                                                                                                                                       █
#이 조건은 first가 3보다 작을 때 참이 됩니다. 따라서 first가 3일 때는 3 < 3이 거짓이므로 break가 실행되지 않고, first가 2가 되었을 때 2 < 3이 참이 되어 break가 실행됩니다.                             █                                                                                                                                                                                                         █
#first가 3일 때 break를 실행하려면 조건문을 if first == 3:으로 변경해야 합니다.

# 수정된 사항

first = 5

while first > 0:
    print(f"while 값 : {first}")
    if first == 3:  # first가 3일 때 break하도록 수정
        print("break 실행")
        break
    first = first - 1