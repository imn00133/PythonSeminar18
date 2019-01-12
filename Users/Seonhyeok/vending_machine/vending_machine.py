money = 0
input_money = input("돈을 넣으세요 : ")
money += int(input_money)

drink = [['블랙커피', 100], ['밀크커피', 150], ['고급커피', 200]]
drink_num = int(len(drink))

print("""1. %s(%d원)
2. %s(%d원)
3. %s(%d원)
4. 거스름돈
넣은 돈: %d원""" % (drink[0][0], drink[0][1], drink[1][0],
                drink[1][1], drink[2][0], drink[2][1], money))
menu_num = int(input("뽑을 물품을 골라주세요 : "))

if menu_num == 1:
    if drink[0][1] <= money:
        print("%s가 나왔습니다." % drink[0][0])
        money -= drink[0][1]
        print("돈을 반환합니다 : %d원" % money)
    else:
        print("""돈이 부족합니다.\n돈을 반환합니다 : %d원""" % money)
elif menu_num == 2:
    if drink[1][1] <= money:
        print("%s가 나왔습니다." % drink[1][0])
        money -= drink[1][1]
        print("돈을 반환합니다 : %d원" % money)
    else:
        print("""돈이 부족합니다.\n돈을 반환합니다 : %d원""" % money)
elif menu_num == 3:
    if drink[2][1] <= money:
        print("%s가 나왔습니다." % drink[2][0])
        money -= drink[2][1]
        print("돈을 반환합니다 : %d원" % money)
    else:
        print("""돈이 부족합니다.\n돈을 반환합니다 : %d원""" % money)
elif menu_num == 4:
    print("거스름돈을 반환합니다 : %d원" % money)
elif not 1 <= menu_num <= drink_num+1:
    print("""물품번호를 잘못 입력하셨습니다.
돈을 반환합니다 : %d원""" % money)
