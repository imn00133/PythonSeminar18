import random

# 랜덤으로 0~9까지의 수를 뽑은다음 [0~9] 리스트에서 아무수를 pop하여 중복을 없애고 random_list에 하나씩 저장한다.


def mk_random_number():
    for i in range(4):
        random_num = random.randrange(0, len(num_list))
        sel_num = num_list.pop(random_num)
        random_list.append(sel_num)
    return random_list


def input_number():
    while True:
        input_num = input("중복되지 않는 4자리 숫자를 입력해주세요 : ")
        if len(input_num) != 4:
            print("4자리 숫자를 입력해 주세요.")
            continue
        # set()은 집합. 집합은 중복값을 허용하지 않아 중복을 삭제 할 수 있다.
        if len(set(input_num)) != len(input_num):
            print("중복되지 않게 입력해 주세요.")
            continue
        input_list = [int(i) for i in input_num]
        return input_list


def check_number(u_list, r_list):
    strike, ball, out = 0, 0, 0
    for i in range(4):
        for j in range(4):
            if u_list[i] == r_list[j] and i == j:
                strike += 1
            elif u_list[i] == r_list[j] and i != j:
                ball += 1
    out = 4 - strike - ball
    if strike == 4:
        return True
    print("[ %d ] strike, [ %d ] ball, [ %d ] out" % (strike, ball, out))


def playing_game():
    rand_list = mk_random_number()
    user_try = 0

    while True:
        user_list = input_number()
        user_try += 1

        if check_number(user_list, rand_list) == 1:
            print("%d번 만에 맞췄습니다!" % user_try)
            break


def restart():
    while True:
        again = input("게임을 다시 하시겠습니까? (yes or no) : ")
        if again == 'yes':
            return True
        elif again == 'no':
            return False
        else:
            continue


while True:
    # 0~9를 가지는 리스트 선언
    num_list = [i for i in range(10)]
    random_list = []
    input_list = []

    playing_game()
    print("끗")
    if restart() == 1:
        print("게임을 다시 시작합니다")
        continue
    else:
        print("~진짜끝~")
        break
