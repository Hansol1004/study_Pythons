kor = [70, 80 ,90, 40, 50]							# 리스트 선언
eng = [90, 80 ,70, 70, 60]
sum1, sum2, sum3, sum4 = 0, 0, 0, 0				    # 누적 변수 초기화

# for 단일변수 in 리스트 :
# 실행문

for score in kor:
    print(score, end='')
    sum1 += score
print(f"\n국어 총점 : {sum1}")

for score in eng:
    print(score, end='')
    sum2 += score
print(f"\n영어 총점 : {sum2}")

for index in range(5):								# 0~4
    kor[index] + eng[index]
    sum3 = kor[index] + eng[index] + sum3
    print(f'국어와 영어 누적값 : {sum3}')
