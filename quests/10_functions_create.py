# 🔹 문제 1
# 섭씨 온도 3개를 받아 평균을 반환하는 함수 avg_celsius(t1, t2, t3) 를 작성하시오.

temp1 = [50, 60, 70]
temp2 = [30, 40, 50]
temp3 = [10, 20, 30]

def avg_celsius(t1, t2, t3):
    return (t1 + t2 + t3) / 3

print(avg_celsius(temp1[0], temp2[0], temp3[0]))
print(avg_celsius(temp1[1], temp2[1], temp3[1])) 
print(avg_celsius(temp1[2], temp2[2], temp3[2]))

# 🔹 문제 2
# 이름과 좋아하는 언어 2개를 받아 아래 형식으로 출력하는 함수를 작성하시오.
# 홍길동님의 선호 언어는 Python, Java 입니다.

name = ["홍길동", "이순신", "강감찬"]
lang1 = ["Python", "C++", "JavaScript"]
lang2 = ["Java", "Python", "C++"]

def favorite_languages(name, lang1, lang2):
    print(f"{name}님의 선호 언어는 {lang1}, {lang2} 입니다.")

favorite_languages(name[0], lang1[0], lang2[0])
favorite_languages(name[1], lang1[1], lang2[1])
favorite_languages(name[2], lang1[2], lang2[2])

# 🔹 문제 3
# 점수 리스트를 받아 60점 이상 점수만 누적한 합계를 반환하는 함수를 작성하시오.

scores1 = [70, 55, 40, 90, 80, 60, 30, 50]
scores2 = [30, 45, 60, 75, 80, 55, 90, 100]
scores3 = [100, 90, 80, 70, 60, 50, 40, 30]

def sum_above(score_list) :
    total_score = 0
    for score in range(len(score_list)) :
        if score_list[score] >= 60 :
            total_score = total_score + score_list[score]
    return total_score
        
print(sum_above(scores1))
print(sum_above(scores2))
print(sum_above(scores3))

# 🔹 문제 4
# 문자열 두 개를 받아 하나의 문장으로 이어 붙이는 함수 combine(str1, str2) 작성.

string1 = ["Hello", "Good", "Happy"]
string2 = ["World", "Morning", "Day"]

def combine(str1, str2) :
    return str1 + " " + str2

print(combine(string1[0], string2[0]))
print(combine(string1[1], string2[1]))
print(combine(string1[2], string2[2]))

# 🔹 문제 5
# 온도 리스트를 받아 모두 섭씨로 변환해 새로운 리스트로 반환하는 함수 작성.

temp1 = [50, 60, 70]
temp2 = [30, 40, 50]
temp3 = [10, 20, 30]

def change_celsius(temp) :
    changed_temps = [0] * len(temp)
    for i in range(len(temp)) :
        changed_temps[i] = (temp[i] - 32) * 5 / 9
    return changed_temps

print(change_celsius(temp1))
print(change_celsius(temp2))
print(change_celsius(temp3))