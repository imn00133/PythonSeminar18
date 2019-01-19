from time import sleep

# 물품 목록, 가격 정의
prod_list = []
prod_list.append(('에스프레소', 4000))
prod_list.append(('카페라뗴', 4500))
prod_list.append(('카페모카', 5000))
prod_list.append(('카라멜 마끼아또', 5500))

# 물품 내 가격 정보 리스트 제작
cnt = 0
prod_price = []
while cnt < len(prod_list):
    prod_price.append(prod_list[cnt][1])
    cnt = cnt + 1

money = 0

# 프로그램 루프 시작
while True:
    # 메뉴판 출력
    cnt = 0
    print('')
    while cnt < len(prod_list):
        print('%d. %-16s %d원' % (cnt+1, prod_list[cnt][0], prod_list[cnt][1]))
        cnt = cnt + 1
    print('%d. %-16s' % (cnt+1, "돈 넣기"))
    print('%d. %-16s' % (cnt+2, "거스름돈 반환"))

    # 현재 금액을 출력하고 행동을 입력받습니다.
    print('\n현재 금액 : %s원' % money)
    select = int(input("물품 또는 행동을 선택해 주세요 : "))-1

    if select == cnt+1:
        # 거스름돈 반환 선택시
        print("반환 : %d원." % money)
        money = 0
        sleep(1)
        continue
    elif select == cnt:
        # 돈 입력 선택시
        input_money = 0

        stat = False
        while stat is False:
            input_money = input("돈을 넣으세요 : ")
            if input_money.isnumeric() is False:
                print("제대로 ", end='')
                continue
            while money + int(input_money) < min(prod_price):
                money = money + int(input_money)
                print("\n현재 금액 : %d원" % money)
                input_money = input("돈이 부족합니다. 더 넣으세요 : ")
            stat = True

        sleep(0.3)
        money = money + int(input_money)
        continue
    elif select < -1:
        # 음수 입력시 프로그램 종료
        print("프로그램을 종료합니다.")
        sleep(1)
        break
    elif (select == -1) or (select >= cnt+2):
        # 범위 밖 잘못된 값 입력시
        print("잘못된 값을 입력하였습니다.")
        sleep(2)
        continue
    elif 0 <= select <= cnt+1:
        # 메뉴 내 제품 입력시
        if money >= prod_price[select]:
            # 구매 가능한 돈이 있는지 확인
            print("%s가 나왔습니다." % prod_list[select][0])
            money = money - prod_price[select]
            sleep(1)
        else:
            print("금액이 부족합니다. 먼저 돈을 입력해 주세요.")
            sleep(2)
            continue
        if money < min(prod_price):
            print("\n금액이 부족하여 잔액이 환불됩니다.")
            print("반환 : %d원." % money)
            money = 0
            sleep(2)
            continue
    else:
        print("알수 없는 오류가 발생하였습니다. 관리자에게 문의하세요")
        sleep(2)

print("반환 : %d원." % money)
money = 0
