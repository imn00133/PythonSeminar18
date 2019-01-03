#복붙용℃ ℉
"""
    <화씨-섭씨 변환>

1. 화씨 온도 입력
2. 계산
3. 소수점 둘쨰 자리까지 출력
"""

f_temp = 0
c_temp = 0

f_temp = input("화씨 온도 입력 : ")
while f_temp.isnumeric() == False:
    f_temp = input("숫자만 : ")
c_temp = (int(f_temp)-32)*5/9

print("%s℉ >> %0.2f℃" %(f_temp, c_temp))



"""

질문이요

분명 isnumeric은 수만 존재하는지 판단하는데
소수점이 들어가면 수가 아니라고 판단하는 이유와
소수점도 수로 판단하게 하는 방법이 있나요?

"""
