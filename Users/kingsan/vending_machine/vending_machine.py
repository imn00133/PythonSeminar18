def init(drinks_dic, c_money):
    print_menu(drinks_dic)
    if c_money > 0:
        print("현재까지 넣은 돈은 %d원입니다." % c_money)


def print_menu(drinks_dic):
    print("")
    for i, name in enumerate(drinks_dic['name']+["돈 넣기", "거스름돈", "종료"], 1):
        if i <= len(drinks_dic['name']):
            print("%s. %s %d원" % (i, name, drinks_dic['price'][i-1]))
        else:
            print("%s. %s" % (i, name))


def input_money():
    inputmoney = int(input("돈을 넣어주십시오 : "))
    return inputmoney


def order_byuser():
    order = input("뽑을 물품을 골라주세요 : ")
    if '0' < order and order < '9':
        order = int(order)
        return order
    elif order == "kingsan":
        return 0


def money_out(c_money):
    if c_money > 0:
        print("거스름돈을 반환합니다.")
    return 0


def print_menu_admin(drinks_dic):
    for i in range(4):
                print("%d. %s 개수: %d"
                      % (i + 1, drinks_dic['name'][i], drinks_dic['stock'][i]))


def access_admin(drinks_dic):
    while True:
        print("\n1. 물품출력\n2. 개수추가\n3. 종료")
        order_toadmin = int(input("원하는 작업을 선택해 주세요 : "))
        if order_toadmin == 1:
            print_menu_admin(drinks_dic)
        elif order_toadmin == 2:
            print_menu_admin(drinks_dic)
            select_toadd = int(input("개수를 추가할 물품을 선택해주세요: "))
            order_toadd = int(input("추가할 개수를 입력해주세요: "))
            drinks_dic['stock'][select_toadd-1] += order_toadd
            print("%s, %d개 추가하였습니다." %
                  (drinks_dic['name'][select_toadd-1], order_toadd))
        else:
            return drinks_dic


def drink_out(index, drinks_dic, c_money):
    if c_money >= drinks_dic['price'][index-1]:
        if drinks_dic['stock'][index-1] > 0:
            drinks_dic['stock'][index-1] -= 1
            c_money -= drinks_dic['price'][index-1]
            print("주문하신 %s 나왔습니다.남은돈 %d" % (drinks['name'][index-1], c_money))
        else:
            print("재고가 부족합니다.")
    else:
        print("돈이 부족합니다.")
    return drinks_dic, c_money


def proc(drinks_dic, c_money):
    order = order_byuser()
    cont = True
    if order == 0:
        drinks_dic = access_admin(drinks_dic)
    elif order < 5:
        drinks_dic, c_money = drink_out(order, drinks_dic, c_money)
    elif order == 5:
        c_money += input_money()
    elif order == 6:
        c_money = money_out(c_money)
    else:
        print("종료를 선택하셨습니다.")
        c_money = money_out(c_money)
        cont = False
    return drinks_dic, c_money, cont


drinks = {}
drinks['name'] = ["아메리카노", "야메리카노", "어메리카노", "여메리카노"]
drinks['price'] = [3500, 4000, 4500, 5000]
drinks['stock'] = [1, 2, 3, 4]

current_money = 0
flag = True
while flag:
    init(drinks, current_money)
    drinks, current_money, flag = proc(drinks, current_money)
