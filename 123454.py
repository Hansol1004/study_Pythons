def to_celsius(temp):
    return (temp - 32) * 5 / 9


temps = 100

if to_celsius(temps) > 20:       # 함수 호출 누락
    print("warm")
else:
    print("cold")
