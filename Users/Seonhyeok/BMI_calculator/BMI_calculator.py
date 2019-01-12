bmi_num = (18.5, 25, 30, 35)
height = float(input("키를 입력하세요(m) : "))
weight = float(input("몸무게를 입력하세요(kg) : "))

bmi = weight / (height ** 2)

if bmi < bmi_num[0]:
    print("저체중 입니다.")
elif bmi_num[0] <= bmi < bmi_num[1]:
    print("정상체중 입니다.")
elif bmi_num[1] <= bmi < bmi_num[2]:
    print("과체중 입니다.")
elif bmi_num[2] <= bmi < bmi_num[3]:
    print("경도비만 입니다.")
elif bmi_num[3] <= bmi:
    print("고도비만 입니다.")
