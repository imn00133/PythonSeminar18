height = float(input("본인의 키를 입력하세요.(m): "))
weight = float(input("본인의 몸무게를 입력하세요.(Kg): "))

BMI_score = weight/(height**2)

if BMI_score < 18.5:
    print("저체중")
elif BMI_score <= 23:
    print("정상")
elif BMI_score <= 25:
    print("과체중")
elif BMI_score <= 30:
    print("경도 비만")
elif BMI_score <= 35:
    print("중증도 비만")
else:
    print("고도 비만")

