def admin_mode(item_price):
    item_print(item_price, permission='admin')


def item_print(item_price, permission='normal'):
    for index in item_price.keys():
        print("{0}. {1}({2}원)".format(index, item_price[index].get('물품'),
                                      item_price[index]['가격']), end='')
        if permission == 'admin':
            print(" 개수: {0}".format(item_price[index]['개수']))
        else:
            print("")


item_price = {
    1: {'물품': '블랙커피', '가격': 100, '개수': 3},
    2: {'물품': '밀크커피', '가격': 150, '개수': 3},
    3: {'물품': '고급커피', '가격': 200, '개수': 3},
    }
control_string ={
    'admin': ['개수변경', '나가기']
    'normal': ['돈 입력', '거스름돈', '종료']
    }
SELECT_INSERT = 1
SELECT_RETURN = 2


total_money = 0
while True:
    # 목록의 리스트를 출력한다.
    item_print(item_price)

    print("현재까지 넣은 돈은 %d원입니다." % total_money)
    select_value = int(input("뽑을 물품을 골라주세요: "))

    # 돈 입력 및 거스름돈을 선택했을 때
    if select_value == len(item_price) + SELECT_RETURN:
        print("돈을 반환합니다: %d원" % total_money)
        total_money = 0

    elif select_value == len(item_price) + SELECT_INSERT:
        input_money = int(input("돈을 넣으세요: "))
        if input_money < 0:
            break
        else:
            total_money += input_money

    elif 0 < select_value <= len(item_price):
        # list는 0부터 시작하기 때문에 계산의 편의를 위해 -1을 한다.
        select_value -= 1
        item_value = item_price[select_value]['가격']
        if total_money >= item_value:
            total_money -= item_value
            print("%s이/가 나왔습니다." % item_price[select_value]['물품'])
            if total_money < min(item_price.values()):
                print("돈을 반환합니다: %d원" % total_money)
                total_money = 0
        else:
            print("돈이 부족합니다. 돈을 더 넣어주세요.")
    else:
        print("물품번호를 잘못 입력하셨습니다.")

# 프로그램을 종료하기 전에 항상 돈을 반환하도록 작성한다.
print("돈을 반환합니다: %d원" % total_money)
print("프로그램을 종료합니다.")
