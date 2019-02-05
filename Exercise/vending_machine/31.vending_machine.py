def main():
    """
    프로그램의 시작
    """
    item_list = read_item_file()
    total_money = 0
    while True:
        select_value = input_user_value(item_list)
        print("")

        # 물품을 선택할 때
        if 0 < select_value <= len(item_list):
            total_money = select_item(item_list, select_value, total_money)

        # 돈 입력 선택했을 때
        elif select_value == ctrl_str_index(item_list, '돈 입력'):
            input_money = int(input("돈을 넣으세요: "))
            if input_money < 0:
                print("잘못 입력하셨습니다.")
            else:
                total_money += input_money

        # 거스름돈 선택
        elif select_value == ctrl_str_index(item_list, '거스름돈'):
            total_money = return_charge(item_list, total_money)

        # 종료 선택
        elif select_value == ctrl_str_index(item_list, '종료'):
            return_charge(item_list, total_money)
            print("자판기 프로그램을 종료합니다.")
            break

        # 그 외 물품번호를 잘못 입력
        else:
            print("물품번호를 잘못 입력하셨습니다.")


def input_user_value(item_list):
    """
    사용자의 입력값을 받는다.
    :param item_list
    :return select_value
    """
    # isinstance(object, type) object에 입력된 type이 type과 같은지 확인한다.
    while not isinstance(select_value, int):
        # 목록의 리스트를 출력한다.
        item_print(item_list)
        print("현재까지 넣은 돈은 %d원입니다.\n" % total_money)
        select_value = input("뽑을 물품을 골라주세요: ")

        # admin모드 진입
        if select_value == 'admin':
            item_list = admin_mode(item_list)
        elif select_value.isnumeric():
            select_value = int(select_value)
        return select_value


def item_print(item_list, permission='normal'):
    """
    아이템 목록을 출력한다.
    permission이 admin이면 개수를 보여준다.
    permission이 normal이면 제어 명령도 출력한다.
    :params item_list, permission='normal'
    """
    for index in range(len(item_list)):
        print("{0}. {1}({2}원)".format(index + 1, item_list[index].get('물품'),
                                      item_list[index]['가격']), end='')
        if permission == 'admin':
            print(" 개수: {0}".format(item_list[index]['개수']))
        else:
            print("")
    if permission != 'admin':
        ctrl_print()


def ctrl_print(permission='normal'):
    """
    control string을 출력한다.
    퍼미션이 admin이면, item_list을 포함하지 않고 index를 출력하고
    퍼미션이 normal이면 item_list을 포함하여 index를 출력한다.
    :param permission='normal'
    """
    if permission == 'admin':
        for index, control_content in enumerate(ctrl_str(permission), 1):
            print("{0}. {1}".format(index, control_content))
    else:
        for index, control_content in enumerate(ctrl_str(permission),
                                                len(item_list) + 1):
            print("{0}. {1}".format(index, control_content))


def ctrl_str(permission):
    """
    자판기의 종료, 돈 입력 같은 제어명령를 저장한 튜플을 반환해 준다.
    퍼미션에 따라 다른 값이 출력된다.
    'admin': 개수변경, 종료
    'normal': 돈 입력, 거스름돈, 종료
    :return CONTROL_STR, 딕셔너리이고 값은 튜플
    """
    CONTROL_STR = {
        'admin': ('물품출력', '개수추가', '종료'),
        'normal': ('돈 입력', '거스름돈', '종료'),
        'error': ('종료')
        }
    return CONTROL_STR[permission]


def ctrl_str_index(item_list, searching_value, permission='normal'):
    """
    item_list와 seacrching_value를 받아 제어명령 딕셔너리의 위치를 반환한다.
    index를 통해 searching_value를 찾는다.
    :params item_list, searching_value, permission='normal'
    :return 제어 명령의 위치
    """
    return len(item_list) + ctrl_str(permission).index(searching_value) + 1


def select_item(item_list, select_value, total_money):
    """
    물품 번호를 선택했을 때, 물품을 처리한다.
    :params item_list, select_value, total_money
    :return total_money
    """
    # list는 0부터 시작하기 때문에 뺀다.
    select_value -= 1
    item_value = item_list[select_value]['가격']
    if total_money < item_value:
        print("돈이 부족합니다. 돈을 더 넣어주세요.")
    elif item_list[select_value]['개수'] <= 0:
        print("물품 개수가 부족합니다. 관리자를 불러주세요.")
    else:
        total_money -= item_value
        item_list[select_value]['개수'] -= 1
        print(item_list[select_value]['개수'])
        print("%s이/가 나왔습니다." % item_list[select_value]['물품'])
        if total_money < item_price_min(item_list):
            total_money = return_charge(item_list, total_money)
    return total_money


def item_price_min(item_list):
    """
    item dict에서 가격이 가장 작은 값을 반환한다.
    """
    price_min = item_list[0]['가격']
    for item in item_list:
        if price_min > item['가격']:
            price_min = item['가격']
    return price_min


def return_charge(item_list, total_money):
    """
    돈을 반환해주는 함수로 본 함수가 실행되면 파일을 저장한다.
    :return total_money = 0
    """
    write_item_file(item_list)
    print("돈을 반환합니다: %d원" % total_money)
    total_money = 0
    return total_money


def admin_mode(item_list):
    """
    admin모드로 접근한다. permission은 admin으로 되어있다.
    :param item_list
    :return item_list
    """
    while True:
        print("")
        ctrl_print(permission='admin')
        select_value = int(input("원하는 작업을 선택해주세요: "))
        print("")
        if select_value == ctrl_str_index([], '물품출력', 'admin'):
            item_print(item_list, permission='admin')
        elif select_value == ctrl_str_index([], '개수추가', 'admin'):
            item_print(item_list, permission='admin')
            item_select = int(input("개수를 추가할 물품을 선택하세요: "))
            if 0 < item_select <= len(item_list):
                item_list[item_select - 1]['개수'] += \
                    int(input("추가할 개수를 입력해주세요: "))
            else:
                print("물품을 잘못 선택하셨습니다.")
        elif select_value == ctrl_str_index([], '종료', 'admin'):
            write_item_file(item_list)
            print("자판기 모드로 돌아갑니다.")
            return item_list
        else:
            print("잘못 입력하셨습니다.")


def read_item_file():
    """
    item_list.txt를 읽어 각 물품의 dictionary를 담은 리스트를 되돌려준다.
    파일이 잘못되었을 경우, 관리자에게 연락을 출력하고 종료한다.
    return: itme_list
    """
    item_list = []
    try:
        with open("item_list.txt", mode='r', encoding='utf-8') as file:
            title = file.readline().split()
            while True:
                item_temp_dict = {}
                item = file.readline().split()
                if not item:
                    break
                for index in range(len(title)):
                    item_temp_dict[title[index]] = item[index]
                converse_data_to_int(item_temp_dict)
                item_list.append(item_temp_dict)
    except Exception:
        print("관리자에게 연락하십시오.")
    return item_list


def converse_data_to_int(conversion_dict):
    """
    item dictionary를 받아 key에서 int로 변경할 값을 변경한다.
    """
    conversion_key = ("가격", "개수")
    for key in conversion_key:
        conversion_dict[key] = int(conversion_dict[key])
    return conversion_dict


def write_item_file(item_list):
    """
    item_list.txt에 지금 상태를 저장한다.
    """
    title = item_list[0].keys()
    with open("item_list.txt", mode='w', encoding='utf-8') as file:
        title_temp = ""
        for str_temp in title:
            title_temp += str(str_temp)
            title_temp += " "
        file.write("%s\n" % title_temp)
        for item_dict in item_list:
            str_temp = ""
            for key in title:
                str_temp += str(item_dict[key])
                str_temp += " "
            file.write("%s\n" % str_temp)
        return None


if __name__ == __main__:
    main()
