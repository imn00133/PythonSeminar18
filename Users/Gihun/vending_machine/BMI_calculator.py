inheigh = float(input("키(m) : "))
inweigh = float(input("몸무게(kg) : "))
bmi = inweigh / (inheigh ** 2)
print("BMI: {bmi}".format(bmi=bmi))
if bmi < 18.5:
    print("저체중")
elif bmi < 23:
    print("표준")
elif bmi < 25:
    print("과체중")
elif bmi < 30:
    print("경도비만")
elif bmi < 35:
    print("중증도비만")
else:
    print("고도비만 aka 돼지")
