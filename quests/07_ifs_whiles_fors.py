# 문제1

# second = “Python is fun", second 문자열에 "Python"이 포함되어 있는지 확인하고,
#  "Welcome!"과 합쳐서 출력하는 코드를 작성하시오.
# 조건: f-string 사용


# 출력 예시: "Welcome! Python is fun"


# 여기에 코드 작성

second = "Python is fun"
if "Python" in second :
    print(f"Welcome! {second}")


# 문제2

# first 변수가 5부터 1까지 감소하도록 while문을 작성하고,
# first == 2일 때만 "special"을 출력하도록 코드를 작성하시오.
# first = 5
# 여기에 코드 작성

first = 5
while first >= 1 :
    print(first)
    if first == 2 :
        print("special")
        break
    first = first - 1

# 문제3

# kor와 eng 리스트가 주어졌을 때,
# 각 학생 점수의 총합을 total_scores 리스트로 저장


# 각 학생 점수 평균을 avg_scores 리스트로 저장


# kor = [70, 80, 90, 40, 50]
# eng = [90, 80, 70, 70, 60]

# # 여기에 코드 작성
# # 출력 예시:
# # total_scores = [160, 160, 160, 110, 110]
# # avg_scores = [80.0, 80.0, 80.0, 55.0, 55.0]

kor = [70, 80, 90, 40, 50]
eng = [90, 80, 70, 70, 60]

total_scores = []
avg_scores = []

for i in range(len(kor)):
    current_total = kor[i] + eng[i]
    total_scores.append(current_total)
    avg_scores.append(current_total / 2)

print(f'total_scores = {total_scores}')
print(f'avg_scores = {avg_scores}')

# 문제4

# kor 리스트에서 60점 이상인 점수만 누적 합계를 계산하고 출력하시오.
# 조건: for문 사용, 60점 미만은 제외


# kor = [70, 80, 90, 40, 50]

# 여기에 코드 작성
# 출력 예시: 누적합 = 240

kor = [70, 80, 90, 40, 50]
sum_kor = 0
for scores in kor :
    if scores >= 60 :
        sum_kor = scores + sum_kor

print(f"합계 : {sum_kor}")

