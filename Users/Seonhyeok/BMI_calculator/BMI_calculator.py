height = float(input("키를 입력하세요(m) : "))
weight = float(input("몸무게를 입력하세요(kg) : "))

bmi = weight / (height ** 2)

if bmi < 18.5:
    print("저체중 입니다.")
elif 18.5 <= bmi < 25:
    print("정상체중 입니다.")
elif 25 <= bmi < 30:
    print("과체중 입니다.")
elif 30 <= bmi < 35:
    print("경도비만 입니다.")
elif 35 <= bmi:
    print("고도비만 입니다.")
