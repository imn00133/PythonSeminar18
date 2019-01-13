drink = {}
drink['ame'] = {'name': "아메리카노", 'price': 3500}
drink['sch'] = {'name': "딸기치즈케익할라치노", 'price': 5500}
drink['gtl'] = {'name': "그린티라떼", 'price': 4500}
drink['cbr'] = {'name': "콜드브루", 'price': 4000}

keys = 'ame', 'sch', 'gtl', 'cbr'
flag = True
input_money = 0
current_money = 0
min_price = min(drink[keys[0]]['price'],
                drink[keys[1]]['price'],
                drink[keys[2]]['price'],
                drink[keys[3]]['price'])

while flag:

    print("\n1. 아메리카노(3500원)")
    print("2. 딸기치즈케익할라치노(5500원)")
    print("3. 그린티라떼(4500원)")
    print("4. 콜드브루(4000원)")
    print("5. 돈 넣기")
    print("6. 거스름돈")
    print("넣은 돈 : %d원" % current_money)

    order = int(input("뽑을 물품을 골라주세요: "))

    if order > 0 and order <= 4:
        if drink[keys[order - 1]]['price'] <= current_money:
            print(drink[keys[order - 1]]['name'], "이/가 나왔습니다.")
            current_money -= drink[keys[order - 1]]['price']
            if current_money < min_price:
                print(current_money, "원을 반환합니다.")
                current_money = 0
        else:
            print("돈이 부족합니다. 돈을 더 넣어주세요.")
    elif order == 5:
        input_money = int(input("돈을 넣으세요: "))
        current_money += input_money
    elif order == 6:
        print(current_money, "원을 반환합니다.")
        current_money = 0
    else:
        flag = False
        print(current_money, "원을 반환합니다.")
        print("프로그램을 종료합니다.")
        current_money = 0
