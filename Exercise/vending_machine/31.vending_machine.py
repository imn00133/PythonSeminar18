"""
자판기 과제 파일
물품의 이름, 가격, 개수를 저장하고 돈을 입력받아 물품을 출력해준다.
저장되는 파일의 이름은 item_list.txt이다.
저장되는 파일내의 column명은 metadata_item()에 있다.
"""
# Author: Kim Jaehyeong
# email: imn00133@gmail.com
# date: 19.02.06


def main():
    """
    프로그램의 시작
    """
    try:
        item_list = read_item_file()
    except Exception:
        exit()
    total_money = 0
    while True:
        print_item(item_list)
        print("현재까지 넣은 돈은 %d원입니다.\n" % total_money)
        select_value = input_user_value(item_list)

        # 물품을 선택할 때
        if 0 < select_value <= len(item_list):
            total_money = select_item(item_list, select_value, total_money)

        # 돈 입력 선택했을 때
        elif select_value == ctrl_str_index(item_list, '돈 입력'):
            input_money = distinguish_positive_num("돈을 넣으세요: ")
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


def distinguish_positive_num(print_value):
    input_value = input(print_value)
    while not input_value.isnumeric():
        input_value = input(print_value)
    return int(input_value)


def input_user_value(item_list):
    """
    사용자의 입력값을 받는다.
    :param item_list
    :return select_value
    """
    select_value = ""
    # isinstance(object, type) object에 입력된 type이 type과 같은지 확인한다.
    while not isinstance(select_value, int):
        # 목록의 리스트를 출력한다.
        select_value = input("뽑을 물품을 골라주세요: ")

        # admin모드 진입
        if select_value == 'admin':
            item_list = admin_mode(item_list)
        elif select_value.isnumeric():
            select_value = int(select_value)
            return select_value


def print_item(item_list, permission='normal'):
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
        princ_ctrl(item_list)


def princ_ctrl(item_list, permission='normal'):
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
        'admin': ('물품추가', '물품변경', '물품삭제', '물품출력', '개수추가', '종료'),
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
        print("%s이/가 나왔습니다." % item_list[select_value]['물품'])
        if total_money < min_item_price(item_list):
            total_money = return_charge(item_list, total_money)
    return total_money


def min_item_price(item_list):
    """
    item dict에서 가격이 가장 작은 값을 반환한다.
    :param item_list
    :return price_min
    """
    price_min = item_list[0]['가격']
    for item in item_list:
        if price_min > item['가격']:
            price_min = item['가격']
    return price_min


def return_charge(item_list, total_money):
    """
    돈을 반환해주는 함수로 본 함수가 실행되면 파일을 저장한다.
    :params item_list, total_money
    :return total_money = 0
    """
    write_item_file(item_list)
    print("돈을 반환합니다: %d원" % total_money)
    total_money = 0
    return total_money


def metadata_item():
    """
    물품에 대한 metadata를 저장한다.
    이중 tuple로 column의 이름과 형식이 저장된다.
    """
    return (('물품', 'str'), ('가격', 'int'), ('개수', 'int'))


def add_item(item_list):
    """
    물품을 리스트 마지막에 추가한다.
    :param item_list
    :return item_list
    """
    question = "추가할 {}을/를 입력하세요: "
    add_item_info = {}
    for metadata_name, metadata_type in metadata_item():
        if metadata_type == 'int':
            metadata_value \
                = distinguish_positive_num(question.format(metadata_name))
            metadata_value = int(metadata_value)
        else:
            metadata_value = input(question.format(metadata_name))
        add_item_info[metadata_name] = metadata_value
    item_list.append(add_item_info)
    return item_list


def change_item(item_list):
    """
    list의 물품명이나 가격을 한다.
    :param item_list
    :return item_list
    """
    print_item(item_list, permission="admin")
    select_value = distinguish_positive_num("변경할 물품을 선택해주세요: ")
    select_value -= 1
    print("%s을/를 선택하셨습니다." % item_list[select_value]['물품'])
    name_temp = input("물품 이름 변경(값 미입력시, 변경하지 않음): ")
    if name_temp != "":
        print("물품 변경")
        item_list[select_value]['물품'] = name_temp
    value_temp = input("물품 가격 변경(값 미입력시, 변경하지 않음): ")
    while value_temp != "" and (not value_temp.isnumeric()):
        value_temp = input("물품 가격 변경(값 미입력시, 변경하지 않음): ")
    if value_temp.isnumeric():
        item_list[select_value]['가격'] = int(value_temp)
    return item_list


def remove_item(item_list):
    """
    list에서 물품을 삭제한다.
    :param item_list
    :return item_list
    """
    print_item(item_list, permission='admin')
    select_value = distinguish_positive_num(
        "삭제할 물품을 선택해주세요(목록에서 벗어난 수를 입력시 처음으로 돌아갑니다.): ")
    if select_value <= len(item_list):
        del_item = item_list.pop(select_value-1)
        print("{}이/가 삭제되었습니다.".format(del_item['물품']))
    return item_list


def change_item_num(item_list):
    print_item(item_list, permission='admin')
    item_select = distinguish_positive_num("개수를 추가할 물품을 선택하세요: ")
    if 0 < item_select <= len(item_list):
        item_list[item_select - 1]['개수'] += \
            distinguish_positive_num("추가할 개수를 입력해주세요: ")
        return item_list
    else:
        print("물품을 잘못 선택하셨습니다.")


def admin_mode(item_list):
    """
    admin모드로 접근한다. permission은 admin으로 되어있다.
    :param item_list
    :return item_list
    """
    print("")
    print("관리자모드")
    while True:
        princ_ctrl(item_list, permission='admin')
        select_value = distinguish_positive_num("원하는 작업을 선택해주세요: ")
        print("")
        if select_value == ctrl_str_index([], '물품추가', 'admin'):
            item_list = add_item(item_list)
        elif select_value == ctrl_str_index([], '물품변경', 'admin'):
            item_list = change_item(item_list)
        elif select_value == ctrl_str_index([], '물품삭제', 'admin'):
            item_list = remove_item(item_list)
        elif select_value == ctrl_str_index([], '물품출력', 'admin'):
            print_item(item_list, permission='admin')
        elif select_value == ctrl_str_index([], '개수추가', 'admin'):
            change_item_num(item_list)
        elif select_value == ctrl_str_index([], '종료', 'admin'):
            write_item_file(item_list)
            print("자판기 모드로 돌아갑니다.")
            print_item(item_list)
            return item_list
        else:
            print("잘못 입력하셨습니다.")
        print("")


def read_item_file():
    """
    item_list.txt를 읽어 각 물품의 dictionary를 담은 리스트를 되돌려준다.
    파일이 잘못되었을 경우, 관리자에게 연락하라는 말을 출력하고 종료한다.
    return: item_list
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
    except FileNotFoundError:
        open("item_list.txt", mode='w', encoding='utf-8').close()
        print("관리자에게 연락하십시오.")
    except Exception:
        error_msg = "초기화할 때 오류가 있습니다.\n관리자에게 연락하십시오."
        print(error_msg)
        raise
    return item_list


def converse_data_to_int(item_temp_dict):
    """
    metadata_item을 통해 int로 변경할 값을 찾아 변경한다.
    파일을 읽을 때 dictionary로 저장된 값 중 int가 될 값을 int로 저장한다.
    :param item_temp_dict
    :return item_temp_dict
    """
    for metadata_name, metadata_type in metadata_item():
        if metadata_type == 'int':
            item_temp_dict[metadata_name] \
                = int(item_temp_dict[metadata_name])
    return item_temp_dict


def write_item_file(item_list):
    """
    item_list.txt에 현재 상태를 저장한다.
    """
    str_temp_list = []
    str_temp = ""
    for metadata_name, _ in metadata_item():
        str_temp += metadata_name
        str_temp += " "
    str_temp_list.append(str_temp)
    for item_dict in item_list:
        str_temp = ""
        for metadata_name, _ in metadata_item():
            str_temp += str(item_dict[metadata_name])
            str_temp += " "
        str_temp_list.append(str_temp)
    with open("item_list.txt", mode='w', encoding='utf-8') as file:
        for str_temp in str_temp_list:
            file.write("%s\n" % str_temp)


if __name__ == "__main__":
    main()
