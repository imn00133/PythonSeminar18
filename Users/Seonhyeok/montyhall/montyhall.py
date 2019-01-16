from random import randint

total_door = int(input("총 문의 개수를 입력하세요 : "))
open_door = int(input("사회자가 여는 문의 개수를 입력하세요 : "))
repeat = int(int("반복 횟수를 입력하세요 : "))

win = (total_door - 1) / total_door(total_door - open_door - 1)
lose = 1 - win

