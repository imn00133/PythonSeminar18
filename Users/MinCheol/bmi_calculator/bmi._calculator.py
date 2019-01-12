# 저체중 18.5 정상 23 과체중 25 경도비만 30 중등비만 35 고도비만

height = float(input("키 입력(cm) : ")) * 0.01
weight = float(input("몸무게 입력(kg) : "))

bmi = weight / height ** 2
level = ["저체중", "정상", "과체중", "경도비만", "중등비만", "고도비만"]

if bmi >= 18.5:
    del(level[0])
    if bmi >= 23:
        del(level[0])
        if bmi >= 25:
            del(level[0])
            if bmi >= 30:
                del(level[0])
                if bmi >= 35:
                    del(level[0])
# bmi 기준치를 넘을 때마다 level리스트의 1번쨰 항목를 지운다.
                                        
print("BMI = %0.2f" % bmi)
print(level[0])
