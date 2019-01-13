money = 0
money_in = input('돈을 넣으세요: ')

# 돈 대신 이상한 거 넣으면 걸러내는 부분
while not money_in.isnumeric():
    money_in = input('돈을 제대로 넣으세요: ')

# 제대로 넣었으면 넣은 돈을 money에 추가합니다.
money += int(money_in)

# 초기 물품 구성
product_list = list()
product_list.append(('멧뚜기', 100))
product_list.append(('보라메', 500))
product_list.append(('비둘기', 800))
product_list.append(('멧돼지', 1200))
product_list.append(('늑대와흑우컴퓨터', 3000))

# 물품을 불러와서 출력합니다.
# cnt = 물품의 index(출력 이후, cnt는 전체 물품 개수가 됩니다.)
# product_list[cnt][0] = 이름, product_list[cnt][1] = 가격
while True:
    cnt = 0
    while cnt < len(product_list):
        print(
            '%d. %s(%d원)' %
            (cnt + 1, product_list[cnt][0], product_list[cnt][1])
        )
        cnt += 1
    print('%d. 돈 넣기' % (cnt + 1))
    print('%d. 거스름돈' % (cnt + 2))

    # 물품을 선택받습니다.
    product_in = int(input('잔액: %d원\n뽑을 물품을 선택해주세요: ' % money))

    # 잘못 입력한 경우
    if product_in > cnt + 2:
        print('물품 번호를 잘못 입력하셨습니다.')
    # 거스름돈을 선택한 경우
    elif product_in == cnt + 1:
        money_in = input('돈을 넣으세요: ')
        while not money_in.isnumeric():
            money_in = input('돈을 제대로 넣으세요: ')
        money += int(money_in)
    elif product_in == cnt + 2:
        if money > 0:
            print('%d원이 반환됩니다.' % money)
            money = 0
        else:
            print('잔액이 없어 돈이 반환되지 않습니다.')
    # 음수를 입력하여 종료를 시도한 경우
    elif product_in < 0:
        # 꼭 그렇게 똑같은 부분을 반복해서 입력해야만 속이 후련했녛어엏ㄱ
        if money > 0:
            print('%d원이 반환됩니다.' % money)
            money = 0
        else:
            print('잔액이 없어 돈이 반환되지 않습니다.')
        break
    # 물품을 선택한 경우
    else:
        # 리스트는 0번부터 시작하는데 물품번호는 1번부터 시작이므로 1을 빼줍니다.
        # 돈이 충분하면 물품을 내보냅니다.
        product = product_list[product_in - 1]
        if money >= product[1]:
            money -= product[1]
            print('%s을(를) 구매하셨습니다.' % product[0])
            # 가장 싼 물품 가격 구하기(물품 정보를 튜플로 저장해서 min을 못 씀)
            cnt = 0
            price_min = product_list[0][1]
            while cnt < len(product_list):
                price_min = min(price_min, product_list[cnt][1])
                cnt += 1
            if 0 < money < price_min:
                print('%d원이 반환됩니다.' % money)
                money = 0
            elif money == 0:
                print('잔액이 없어 돈이 반환되지 않습니다.')
        else:
            print('돈이 부족합니다. 돈을 더 넣어주세요.')
