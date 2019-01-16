import os
import sys
from time import sleep


def bujok():
    print("저런저런 돈이 부족하다구 친구")


def Dche(Don):
    if Don > 0:
        print("%d원 마이쪙" % Don)
    else:
        print("%d원 반환" % Don)


moolgun = ["블랙말랑카우", "밀크커피", "고급시계"]
ga_guek = [100, 150, 39900]
Don = (int)(input("초기배팅금액 입력:"))
while True:
    print("1. 블랙말랑카우(100원)")
    print("2. 밀크커피(150원)")
    print("3. 고급시계(39900원)")
    print("4. 돈좀 넣으쉴?")
    print("5. 거스름돈")
    sel = (int)(input("선택: "))
    if sel < 0:
        Dche(Don)
        break
    elif sel == 0:
        print("Ang↗?")
    elif sel < 4:
        if Don < ga_guek[sel-1]:
            bujok()
        else:
            Don -= ga_guek[sel-1]
            print("%s가 나왔습니다." % moolgun[sel-1])
    elif sel == 4:
        Don += (int)(input("감사합니다.: "))
    if Don < min(ga_guek) or sel == 5:
        Dche(Don)
        Don = 0
    sleep(1)
    os.system('clear')
