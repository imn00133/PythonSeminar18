import random
from time import sleep
import os
import sys


def che(l_cho, door_open):
    for i in door_open[0:k]:
        if i == l_cho:
            return True
    return False


m = (int)(input("시뮬레이션 실행횟수 입력: "))
n = (int)(input("문의 갯수 입력: "))
k = (int)(input("사회자가 열 수 있는 문의 갯수 입력: "))
if k > n-2 or k <= 0 or m < 0:
    print("장난치다 손모가지 확 날아간다.")
    exit()
before = -1
chw_cou = 0
w_cou = 0
for i in range(1, m+1):
    door_open = []
    In_Car = random.randrange(0, n)
    choice = random.randrange(0, n)
    cou = 0
    while cou < k:
        temp = random.randrange(0, n)
        if temp != In_Car and temp != choice:
            door_open.append(temp)
            cou += 1
    if choice == In_Car:
        w_cou += 1
    while True:
        l_cho = random.randrange(0, n)
        if l_cho == choice or che(l_cho, door_open):
            continue
        break
    choice = l_cho
    if choice == In_Car:
        chw_cou += 1
    if before != (int)(i/m*100):
        before = (int)(i/m*100)
        os.system("clear")
        print("작업중: %d%%" % before)
print("선택을 바꾼경우")
print("이긴 횟수: %d" % chw_cou)
print("이긴 확률: %f" % (float)(chw_cou/m))
print("이론적 수치: %f" % (float)((n-1)/(n*(n-k-1))))
print("안 바꾼 경우")
print("이긴 횟수: %d" % w_cou)
print("이긴 확률: %f" % (float)(w_cou/m))
print("이론적 수치: %f" % (float)(1/n))
