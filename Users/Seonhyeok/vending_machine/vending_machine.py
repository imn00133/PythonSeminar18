money = 0

while True:
    cnt = 0

    drink = [[100, '블랙커피'], [150, '밀크커피'], [200, '고급커피']]
    admin_list = ['물품출력', '개수추가', '종료']
    drink_num = len(drink)
    min_price = min(drink)[0]
    # admin_siwtch = 0

    # 메뉴판
    while True:
        if cnt == drink_num:
            print("%d. 돈 넣기" % (cnt+1))
            cnt += 1
        elif cnt == drink_num+1:
            print("%d. 거스름돈 반환\n넣은 돈 : %d원" % (cnt+1, money))
            break
        else:
            print("%d. %s(%d원)" % (cnt+1, drink[cnt][1], drink[cnt][0]))
            cnt += 1

    cnt = 0

    sel_num = input("번호를 선택해주세요 : ")

    if sel_num.isnumeric() != 1:
        if str(sel_num) == '종료':
            print("종료됩니다.\n돈을 반환합니다 : %d원\n\n" % money)
            break
        elif str(sel_num) == 'admin':
            print("admin모드를 시작합니다.\n")
            # admin_siwtch = 1
            while True:
                for i in range(len(admin_list)):
                    print("%d. %s" % (cnt+1, admin_list[cnt]))
                    cnt += 1
                admin_num = int(input("번호를 선택해주세요 : "))
                cnt = 0
                if admin_num == 3:
                    print("admin 모드를 종료합니다.\n")
                    break
    else:
        sel_num = int(sel_num)
        if 1 <= sel_num <= drink_num:
            if drink[sel_num-1][0] <= money:
                print("%s가 나왔습니다." % drink[sel_num-1][1])
                money -= drink[sel_num-1][0]
                if money < min_price:
                    print("돈이 부족합니다. 돈을 반환합니다.\n반환된 금액 : %d원" % money)
                    money = 0
                print("\n\n")
            else:
                print("돈이 부족합니다.\n돈을 더 넣어 주세요.\n\n")
        elif sel_num == drink_num + 1:
            money += int(input("돈을 넣습니다.\n투입금액 : "))
            print("현재 투입된 돈은 %d원 입니다.\n\n" % money)
        elif sel_num == drink_num + 2:
            print("거스름돈을 반환합니다 : %d원\n\n" % money)
            money = 0
        elif not 1 <= sel_num <= drink_num + 2:
            print("물품번호를 잘못 입력하셨습니다.\n돈을 반환합니다 : %d원\n\n" % money)
            money = 0

