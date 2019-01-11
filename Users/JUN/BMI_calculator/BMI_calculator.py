weight = (float)(input("몸무게를 입력해주십시오.: "))
height = (float)(input("키를 입력해주십시오.: "))
BMI = abs(weight/(height*height))
if BMI<18.5:
    print("저체중")
elif BMI<23:
    print("정상")
elif BMI<25:
    print("과체중")
elif BMI<30:
    print("경도비만")
elif BMI<35:
    print("중증도비만")
else:
    print("고도비만")