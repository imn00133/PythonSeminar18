height = float(input("본인의 키(m)를 입력하십시오 : "))
if height > 2.5:
    print("\n※ 미터(m)단위로 입력해주십시오. 예시 - 1.75\n")
    height = float(input("본인의 키(m)를 입력하십시오 : "))
weight = float(input("본인의 몸무게(Kg)를 입력하십시오 : "))
bmi = weight/(height*height)

print("\n§ 당신의 신체질량지수(BMI)는 %d입니다." % bmi)
if bmi > 30:
    print("§ 고도비만입니다.....")
elif bmi > 25:
    print("§ 비만입니다... 건강에 유의하세요.")
elif bmi > 23:
    print("§ 과체중입니다. 조심하세요")
elif bmi > 18.5:
    print("§ 정상입니다!!")
else:
    print("§ 저체중입니다.")
print("\n")
