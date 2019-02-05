# Author: KimJaeheong
# email: imn00133@gmail.com
# date: 19.01.21

import random
USING_NUMBER_IN_GAME = 4


def main():
    # game loop
    while True:
        computer_num = gernerate_num()
        exec_game(computer_num)
        if game_rerun():
            break
        print("다시 시작합니다.")


def gernerate_num():
    """
    컴퓨터의 숫자를 생성하여 반환한다.
    0-9까지의 숫자를 가진 list를 만들고 pop을 통해 중복을 생성하지 않는다.

    return: (list)computer_num
    """
    number_list = list(range(10))
    computer_num = []
    for index in range(USING_NUMBER_IN_GAME):
        choice_num = number_list.pop(random.randrange(0, len(number_list)))
        computer_num.append(choice_num)
    return computer_num


def exec_game(computer_num):
    """
    사용자가 맞출 때까지 반복하는 함수이다.
    """
    number_question = 0
    while True:
        user_num = input_user_num()
        if compare_num(computer_num, user_num):
            print("축하합니다. %d번만큼 질문하여 맞추셨습니다." % number_question)
            break
        number_question += 1


def input_user_num():
    """
    사용자의 입력을 받아 조건에 맞는지 확인하는 함수이다.
    """
    while True:
        user_text = input("중복되지 않은 %d자리수를 입력해주세요(0000-9999): "
                          % USING_NUMBER_IN_GAME)
        if not user_text.isnumeric():
            print("숫자만 입력해주세요.")
            continue
        if len(user_text) != USING_NUMBER_IN_GAME:
            print("%d자리 숫자를 입력해주세요." % USING_NUMBER_IN_GAME)
            continue
        if verify_overlap(user_text):
            print("각 자리 숫자가 중복되지 않게 입력해주세요.")
            continue
        # 리스트 내의 각 문자를 숫자로 변환하기 위해서는 컴프리헨션을 사용하는 것이 좋다.
        # list_value = [int(i) for i in list_value]
        # 또는 map함수를 이용한다.
        # list_value = list(map(int, list_value))
        user_value = []
        for value in user_text:
            user_value.append(int(value))
        return user_value


def verify_overlap(test_list):
    """
    리스트를 받아와 내부에 중복이 있는지 확인한다.
    중복이 있으면 True, 없으면 False를 반환한다.

    return: bool
    """
    set_test_list = set(test_list)
    if len(set_test_list) == len(test_list):
        return False
    return True


def compare_num(computer_num, user_num):
    """
    사용자와 컴퓨터 숫자를 비교해 strike, ball, out을 확인한다.
    return: bool(strike==4, True)
    """
    strike, ball, out = 0, 0, 0
    for index in range(USING_NUMBER_IN_GAME):
        if computer_num[index] == user_num[index]:
            strike += 1
        elif user_num[index] in computer_num:
            ball += 1
        else:
            out += 1
    print("strike: {0}, ball: {1}, out: {2}".format(strike, ball, out))
    if strike == 4:
        return True
    return False


def game_rerun():
    """
    게임 종료를 확인한다. 다시 할지 물어본다.
    return: bool(yes==False)
    """
    while True:
        user_choice = input("다시 하시겠습니까?(yes/no) ")
        if "yes" == user_choice.lower() or "y" == user_choice.lower():
            return False
        elif "no" == user_choice.lower() or "n" == user_choice.lower():
            return True


if __name__ == "__main__":
    main()
