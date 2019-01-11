def admin_mode():
    pass


item_price = {
    '블랙커피': dict('가격': 100, '개수': 3),
    '밀크커피': dict('가격': 150, '개수': 3),
    '고급커피': dict('가격': 200, '개수': 3),
    }

# list와 price를 각각 사용하면 사용자의 실수가 있을 수 있다.
item_list = list(item_price.keys())
item_list.extend(['돈 입력', '거스름돈'])

total_money = 0
while True:
    # 목록의 리스트를 출력한다.
    for index, item_name in enumerate(item_list, 1):
        print("")
        if item_price.get(item_list[index]) is not None:
            print("{0}. {1}({2}원)".format(
                index, item_name, item_price[item_list]['가격']))
        else:
            print("{0}. {1}".format(index, item_name))

        print("현재까지 넣은 돈은 %d원입니다." % total_money)
    select_value = int(input("뽑을 물품을 골라주세요: "))

    # 돈 입력 및 거스름돈을 선택했을 때
    if select_value == len(item_list):
        print("돈을 반환합니다: %d원" % total_money)
        total_money = 0

    elif select_value == (len(item_list) - 1):
        input_money = int(input("돈을 넣으세요: "))
        if input_money < 0:
            break
        else:
            total_money += input_money

    elif 0 < select_value <= len(item_price.keys()):
        # list는 0부터 시작하기 때문에 계산의 편의를 위해 -1을 한다.
        select_value -= 1
        if total_money >= item_price[item_list[select_value]]:
            total_money -= item_price[item_list[select_value]]
            print("%s이/가 나왔습니다." % item_list[select_value])
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
