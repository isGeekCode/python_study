# 키의 단위 cm를 m로 환산
a = float(input("키를 입력하세요. : "))*0.01
b = float(input("몸무게를 입력하세요. : "))
bmi = b/(a**2)

# print(bmi)
print("BMI수치는 ", bmi, "입니다")

if bmi > 25:
    print("비만입니다.")

elif 23 <= bmi <= 25:
    print("과체중입니다.")

elif 18.5 <= bmi <= 23:
    print("정상체중입니다.")

elif bmi < 18.5:
    print("저체중입니다.")
