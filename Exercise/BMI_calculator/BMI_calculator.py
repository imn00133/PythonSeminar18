height = float(input("본인의 키를 입력하세요.(m): "))
weight = float(input("본인의 몸무게를 입력하세요.(kg): "))

# BMI에 대한 각 경계값을 가지는 상수 튜플이다.
BMI_BOUNDARY = (18.5, 23, 25, 30, 35)

BMI_index = weight / (height ** 2)

# 부동소수점으로 ==, 즉 같음을 비교할 경우
# https://winterj.me/Floating-Point/를 참고할 것
if BMI_index < BMI_BOUNDARY[0]:
    print('저체중')
elif BMI_index < BMI_BOUNDARY[1]:
    print('정상')
elif BMI_index < BMI_BOUNDARY[2]:
    print('과체중')
elif BMI_index < BMI_BOUNDARY[3]:
    print('경도비만')
elif BMI_index < BMI_BOUNDARY[4]:
    print('중증도 비만')
else:
    print('고도 비만')
