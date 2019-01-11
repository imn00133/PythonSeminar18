def Dche(Don, value):
    if Don-value > 0:
        return False
    return True


def JanDon(Don, value):
    print("%d" % int(Don - value))


Don = (int)(input("돈을 넣으세요: "))
print("1. 블랙말랑카우(100원)")
print("2. 밀크커피(150원)")
print("3. 고급시계(39900원)")
print("4. 거스름돈")
print("넣은 돈 : %d원" % Don)
mool = (int)(input("뽑을 물품을 골라주세요: "))
if mool == 1:
    if Dche(Don, 100):
        print("돈이 부족합니다.")
        JanDon(Don, 0)
    else:
        print("블랙말랑카우이/가 나왔습니다.")
        JanDon(Don, 100)
elif mool == 2:
    if Dche(Don, 150):
        print("돈이 부족합니다.")
        JanDon(Don, 0)
    else:
        print("밀크커피이/가 나왔습니다.")
        JanDon(Don, 150)
elif mool == 3:
    if Dche(Don, 39900):
        print("돈이 부족합니다.")
        JanDon(Don, 0)
    else:
        print("고급시계이/가 나왔습니다.")
        JanDon(Don, 39900)
elif mool == 4:
    JanDon(Don, 0)
else:
    print("물품번호를 잘못 입력하셨습니다")
