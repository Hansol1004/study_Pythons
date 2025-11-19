kor = 60
eng = 70
math = 80

# sum = kor + eng

def get_sum(korean, english, mathematics) :
    summation = korean + english + mathematics
    return summation

sum = get_sum(kor, eng, math)
print(f"총점 : {sum}") 

kor_scores = [90, 80, 70, 60, 50]
eng_scores = [85, 75, 65, 55, 45]
math_scores = [88, 78, 68, 58, 48]

range(len(kor_scores))

# for i in range(len(kor_scores)) :
#     kor = kor_scores[i]
#     eng = eng_scores[i]
#     math = math_scores[i]
#     sum = get_sum(kor, eng, math)
#     print(f"{i+1}번 학생 총점 : {sum}")

def get_for_sum(korean_scores, english_scores, mathemathics_scores) :
    for i in range(len(kor_scores)) :
        kor = kor_scores[i]
        eng = eng_scores[i]
        math = math_scores[i]
        sum = get_sum(kor, eng, math)
        print(f"{i+1}번 학생 총점 : {sum}")
    return 0

get_for_sum(kor_scores, eng_scores, math_scores)