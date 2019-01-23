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


def admin_list(moolgun, moolgun_cou):
    i = 1
    for mo in moolgun:
        print("%d. %s: %d" % (i, mo, moolgun_cou[mo]))
        i += 1


def admin_mode(moolgun, moolgun_cou):
    while True:
        print("1. 물품 목록과 ㄱㅐ수 출력")
        print("2. 물품ㄱㅐ수 변경")
        print("3. admin_mode 종료")
        select = (int)(input("입력하시게: "))
        if select == 1:
            admin_list(moolgun, moolgun_cou)
        elif select == 2:
            admin_list(moolgun, moolgun_cou)
            sel_num = (int)(input("뭘 바꾸실텐가?: "))
            cou = (int)(input("몇개?: "))
            moolgun_cou[moolgun[sel_num-1]] = cou
        elif select == 3:
            break
        else:
            print("Ang~?")
        sleep(1)
        os.system('clear')


moolgun_cou = {'블랙말랑카우': 5, '밀크커피': 5, '고급시계': 5}
moolgun = ["블랙말랑카우", "밀크커피", "고급시계"]
ga_guek = [100, 150, 39900]
Don = (int)(input("초기배팅금액 입력:"))
while True:
    print("1. 블랙말랑카우(100원)")
    print("2. 밀크커피(150원)")
    print("3. 고급시계(39900원)")
    print("4. 돈좀 넣으쉴?")
    print("5. 거스름돈")
    print("6. 종료")
    sel = input("선택: ")
    if sel == "admin":
        os.system('clear')
        admin_mode(moolgun, moolgun_cou)
    if sel > '0' and sel <= '9':
        sel = (int)(sel)
        if sel == 6:
            Dche(Don)
            break
        elif sel < 4:
            if Don < ga_guek[sel-1]:
                bujok()
            elif moolgun_cou.get(moolgun[sel-1]) > 0:
                Don -= ga_guek[sel-1]
                moolgun_cou[moolgun[sel-1]] -= 1
                print("%s가 나왔습니다." % moolgun[sel-1])
            else:
                print("물건이 부족합니다.")
        elif sel == 4:
            Don += (int)(input("감사합니다.: "))
        if Don < min(ga_guek) or sel == 5:
            Dche(Don)
            Don = 0
    sleep(1)
    os.system('clear')
