def item_price_min(item_dict):
    """
    item dict에서 가격이 가장 작은 값을 반환한다.
    """
    price_min = item_dict[1]['가격']
    for item in item_dict.values():
        if price_min > item['가격']:
            price_min = item['가격']
    return price_min


def return_charge(total_money):
    """
    돈을 반환해주는 함수. total_money를 0으로 만들기 위해 0을 반환
    """
    print("돈을 반환합니다: %d원" % total_money)
    return 0


def cont_str():
    """
    자판기의 종료, 돈 입력 같은 제어명령를 저장한 딕셔너리를 반환해 준다.
    'admin': 개수변경, 종료
    'normal': 돈 입력, 거스름돈, 종료
    :return CONTROL_STR, 딕셔너리이고 값은 튜플
    """
    CONTROL_STR = {
        'admin': ('물품출력', '개수추가', '종료'),
        'normal': ('돈 입력', '거스름돈', '종료')
        }
    return CONTROL_STR


def cont_str_index(item_dict, searching_value, permission='normal'):
    """
    item_dict와 seacrching_value를 받아 제어명령 딕셔너리에서 위치를 반환한다.
    index를 통해 searching_value를 찾는다.
    :params item_dict, searching_value, permission='normal'
    :return 제어 명령의 위치
    """
    return len(item_dict) + cont_str()[permission].index(searching_value) + 1


def cont_print(permission='normal'):
    """
    control string을 출력한다.
    퍼미션이 admin이면, item_dict을 포함하지 않고 index를 출력하고
    퍼미션이 normal이면 item_dict을 포함하여 index를 출력한다.
    :param permission='normal'
    """
    if permission == 'admin':
        for index, control_content in enumerate(cont_str()[permission], 1):
            print("{0}. {1}".format(index, control_content))
    else:
        for index, control_content in enumerate(cont_str()[permission],
                                                len(item_dict) + 1):
            print("{0}. {1}".format(index, control_content))


def item_print(item_dict, permission='normal'):
    """
    아이템 목록을 출력한다.
    permission이 admin이면 개수를 보여준다.
    permission이 normal이면 제어 명령도 출력한다.
    :params item_dict, permission='normal'
    """
    for index in item_dict.keys():
        print("{0}. {1}({2}원)".format(index, item_dict[index].get('물품'),
                                      item_dict[index]['가격']), end='')
        if permission == 'admin':
            print(" 개수: {0}".format(item_dict[index]['개수']))
        else:
            print("")
    if permission != 'admin':
        cont_print()


def admin_mode(item_dict):
    """
    admin모드로 접근한다. permission은 admin으로 되어있다.
    :param item_dict
    :return item_dict
    """
    while True:
        print("")
        cont_print(permission='admin')
        select_value = int(input("원하는 작업을 선택해주세요: "))
        print("")
        if select_value == cont_str_index({}, '물품출력', 'admin'):
            item_print(item_dict, permission='admin')
        elif select_value == cont_str_index({}, '개수추가', 'admin'):
            item_print(item_dict, permission='admin')
            item_select = int(input("개수를 추가할 물품을 선택하세요: "))
            if 0 < item_select <= len(item_dict):
                item_dict[item_select]['개수'] += \
                    int(input("추가할 개수를 입력해주세요: "))
            else:
                print("물품을 잘못 선택하셨습니다.")
        elif select_value == cont_str_index({}, '종료', 'admin'):
            print("자판기 모드로 돌아갑니다.")
            return item_dict
        else:
            print("잘못 입력하셨습니다.")


item_dict = {
    1: {'물품': '블랙커피', '가격': 100, '개수': 1},
    2: {'물품': '밀크커피', '가격': 150, '개수': 1},
    3: {'물품': '고급커피', '가격': 200, '개수': 1},
    }
total_money = 0

while True:
    print("")
    select_value = ''
    price_min = item_price_min(item_dict)

    # 목록의 리스트를 출력한다.
    # isinstance(object, type) object에 입력된 type이 type과 같은지 확인한다.
    while not isinstance(select_value, int):
        item_print(item_dict)
        print("현재까지 넣은 돈은 %d원입니다." % total_money)
        select_value = input("뽑을 물품을 골라주세요: ")

        # admin모드 진입
        if select_value == 'admin':
            item_dict = admin_mode(item_dict)
        elif select_value.isnumeric():
            select_value = int(select_value)

    # 돈 입력 및 거스름돈을 선택했을 때
    if select_value == cont_str_index(item_dict, '거스름돈'):
        total_money = return_charge(total_money)

    elif select_value == cont_str_index(item_dict, '돈 입력'):
        input_money = int(input("돈을 넣으세요: "))
        if input_money < 0:
            print("잘못 입력하셨습니다.")
        else:
            total_money += input_money

    # 물품을 선택할 때
    elif 0 < select_value <= len(item_dict):
        item_value = item_dict[select_value]['가격']
        if total_money < item_value:
            print("돈이 부족합니다. 돈을 더 넣어주세요.")
        elif item_dict[select_value]['개수'] <= 0:
            print("물품 개수가 부족합니다. 관리자를 불러주세요.")
        else:
            total_money -= item_value
            item_dict[select_value]['개수'] -= 1
            print("%s이/가 나왔습니다." % item_dict[select_value]['물품'])
            if total_money < price_min:
                total_money = return_charge(total_money)

    # 종료를 누르면 종료
    elif select_value == cont_str_index(item_dict, '종료'):
        break

    # 그 외 물품번호를 잘못 입력
    else:
        print("물품번호를 잘못 입력하셨습니다.")

return_charge(total_money)
print("자판기 프로그램을 종료합니다.")
