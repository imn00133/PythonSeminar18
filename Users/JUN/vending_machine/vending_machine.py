import os
import sys
from time import sleep


def save(moolgun_dic, moolgun_list, moolgun_value):
    db = open("moolgundb.txt", 'w')
    for i in range(0, len(moolgun_list)):
        arr = moolgun_list[i] + " "
        arr += (str)(moolgun_value[i]) + " "
        arr += (str)(moolgun_dic.get(moolgun_list[i])[1]) + "\n"
        db.write(arr)
    db.close()


def bujok():
    print("저런저런 돈이 부족하다구 친구")


def Dche(Don):
    if Don > 0:
        print("%d원 마이쪙" % Don)
    else:
        print("%d원 반환" % Don)


def admin_list(moolgun_dic):
    i = 1
    for mo in moolgun_dic.keys():
        print("%d. %s: %d" % (i, mo, moolgun_dic[mo][1]))
        i += 1


def admin_mode(moolgun_dic, moolgun_list, moolgun_value):
    while True:
        print("1. 물품 목록과 ㄱㅐ수 출력")
        print("2. 물품ㄱㅐ수 변경")
        print("3. admin_mode 종료")
        select = (int)(input("입력하시게: "))
        if select == 1:
            admin_list(moolgun_dic)
        elif select == 2:
            admin_list(moolgun_dic)
            sel_num = (int)(input("뭘 바꾸실텐가?: "))
            cou = (int)(input("몇개?: "))
            moolgun_dic[moolgun_list[sel_num-1]][1] = cou
        elif select == 3:
            break
        else:
            print("Ang~?")
        sleep(1)
        os.system('clear')
    save(moolgun_dic, moolgun_list, moolgun_value)


try:
    db = open("moolgundb.txt", 'r')
except No_DB:
    print("관리자를 호출해주세요")
moolgun_dic = dict()
moolgun_value = list()
moolgun_list = list()
while True:
    i = (str)(db.readline())
    i = i.split()
    if i == []:
        break
    moolgun_dic.setdefault(i[0], [(int)(i[1]), (int)(i[2])])
db.close()
for i in moolgun_dic.keys():
    moolgun_list.append(i)
for i in moolgun_list:
    moolgun_value.append(moolgun_dic.get(i)[0])
Don = (int)(input("초기배팅금액 입력:"))
while True:
    coui = 1
    for i in moolgun_dic.keys():
        print("%d. %s(%s)" % (coui, i, moolgun_dic.get(i)[0]))
        coui = coui+1
    print("4. 돈좀 넣으쉴?")
    print("5. 거스름돈")
    print("6. 종료")
    sel = input("선택: ")
    if sel == "admin":
        os.system('clear')
        admin_mode(moolgun_dic, moolgun_list, moolgun_value)
    if sel > '0' and sel <= '9':
        sel = (int)(sel)
        if sel == 6:
            Dche(Don)
            save(moolgun_dic, moolgun_list, moolgun_value)
            break
        elif sel < 4:
            if Don < moolgun_value[sel-1]:
                bujok()
            elif moolgun_dic.get(moolgun_list[sel-1])[0] > 0:
                Don -= moolgun_value[sel-1]
                moolgun_dic[moolgun_list[sel-1]][1] -= 1
                print("%s가 나왔습니다." % moolgun_list[sel-1])
            else:
                print("물건이 부족합니다.")
        elif sel == 4:
            Don += (int)(input("감사합니다.: "))
        if Don < min(moolgun_value) or sel == 5:
            Dche(Don)
            save(moolgun_dic, moolgun_list, moolgun_value)
            Don = 0
    sleep(1)
    os.system('clear')
