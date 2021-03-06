# 입력받는다. 키는 cm로 입력받은 후 m로 변환하기 위해 0.01을 곱한다.
# 이후 입력받은 값을 토대로 BMI 계산
height = float(input('키를 입력해주세요(cm)\t\t: ')) * 0.01
weight = float(input('몸무게를 입력해주세요(kg)\t: '))
BMI = weight / height ** 2

level_cut = (18.5, 23, 25, 30, 35)
level_name = ('저체중', '정상', '과체중', '경도 비만', '중증도 비만', '고도 비만')

# 저체중, 정상, 과체중, ... 순으로 각각 0, 1, 2, ...의 level을 부여한다.
# 각각의 커트라인을 통과할 때마다 레벨 1이 상승하는 방식이다. 세상에서 가장 기분 나쁜 레벨업
for level, x in enumerate(level_cut):
    if BMI < x:
        break

print('\nBMI는 %0.2f이고, %s에 해당됩니다.' % (BMI, level_name[level]))
