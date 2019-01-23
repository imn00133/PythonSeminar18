def init(drinks_dic, c_money, mflag):
    print_menu(drinks_dic)
    if c_money != 0:
        print("현재까지 넣은 돈은 %d원입니다.")
    order_init = input("뽑을 물품을 골라주세요 : ")
    order(order_init, drinks_dic, c_money, mflag)


def print_menu(drinks_dic):
    for i, name in enumerate(drinks_dic['name']+["돈 입력", "거스름돈", "종료"], 1):
        if i <= len(drinks_dic['name']):
            print("%s. %s %d원" % (i, name, drinks_dic['price'][i-1]))
        else:
            print("%s. %s" % (i, name))


def input_money(c_money):
    inputmoney = int(input("돈을 넣어주십시오 : "))
    return c_money + inputmoney


def order(order_byuser, drinks_dic, c_money, mflag):
    if '0' < order_byuser and order_byuser < '9':
        print("인티저개꿀 %s" % order_byuser)
        if 1 < order_byuser < 5:
            pass
        elif order_byuser == 5:
            c_money = input_money(c_money)
        elif order_byuser == 6:
            mflag = False
    elif order_byuser == "kingsan":
            access_admin(drinks_dic)


def access_admin(drinks_dic):
    pass


drinks = {}
drinks['name'] = ["아메리카노", "야메리카노", "어메리카노", "여메리카노"]
drinks['price'] = [3500, 4000, 4500, 5000]
drinks['stock'] = [1, 2, 3, 4]

current_money = 0
flag = True
while flag:
    init(drinks, current_money, flag)

    break
