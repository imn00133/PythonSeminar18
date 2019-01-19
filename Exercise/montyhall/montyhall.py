import random

while True:
    door_num = int(input("총 문의 개수를 입력하세요: "))
    compere_door = int(input("사회자가 여는 문의 개수를 입력하세요: "))
    if door_num - compere_door >= 2:
        break
    print("사회자가 여는 문의 개수가 너무 많습니다.")

rotation_num = int(input("반복횟수를 입력하세요: "))

win = 0
change_win = 0
current_rotation_num = 0
while current_rotation_num < rotation_num:
    # 사건이 독립적임으로, 맨 첫번째를 당첨으로 고정한다.
    door = [0] * door_num
    door[0] = 1

    # 랜덤하게 선택해서 당첨이 나오면, 바꿀때는 무조건 실패한다.
    participant_select = random.randrange(0, len(door))
    if door[participant_select] == 1:
        win += 1
        current_rotation_num += 1
        continue
    door.pop(participant_select)

    # 맨 뒤쪽 값을 사회자가 선택하는 개수만큼 제거한다.
    compere_open_num = 0
    while compere_open_num < compere_door:
        door.pop()
        compere_open_num += 1

    # 남은 문을 랜덤하게 선택해서 이기는지 확인한다.
    participant_select = random.randrange(0, len(door))
    if door[participant_select] == 1:
        change_win += 1
    current_rotation_num += 1

    if current_rotation_num % 10000 == 0:
        print("%d번째 입니다." % current_rotation_num)

print("총 횟수: %d" % rotation_num)
print("바꾸지 않았을 때 이긴 횟수: %d" % win)
print("바꿨을 때 이긴 횟수: %d" % change_win)
print("바꾸지 않았을 때 이길 이론적 확률: %0.4f" % (1/door_num))
print("바꾸지 않았을 때 이긴 시뮬레이션 확률: %0.4f" % (win/rotation_num))
print("바꿨을 때 이길 이론적 확률: %0.4f" % ((door_num - 1)
      / (door_num * (door_num - compere_door - 1))))
print("바꿨을 때 이긴 시뮬레이션 확률: %0.4f" % (change_win/rotation_num))
