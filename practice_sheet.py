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
