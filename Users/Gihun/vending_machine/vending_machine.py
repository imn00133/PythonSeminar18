# 상품 정의
products = list()
products.append(['감자', 300])
products.append(['고구마', 450])
products.append(['건포도', 500])
products.append(['히오스', 550])


money = int(input("돈 넣으쇼:"))

pro_cnt = len(products)
# 상품 개수

# 메뉴판 출력
while True:
    menu = 0
    while pro_cnt > menu:
        print('%d. %s: %d원' % (menu+1, products[menu][0], products[menu][1]))
        menu = menu + 1

    menu = menu + 1
    print('%d. 거스름돈' % menu)
    print('넣은 돈 : %d 원 ' % money)

    # 상품 번호 확인
    select = int(input("상품 번호를 쓰시게 "))-1

    if 0 <= select < len(products):
        if money > int(products[select][1]):
            money = money - products[select][1]
            print('%s 구매 완료' % (products[select][0]))
            print('%d 원 반환' % (money))
            break
        else:
            print("돈 부족")
    elif select == menu-1:
            print('%d 원 반환' % (money))
            break
    else:
        print("잘못된 상품 번호다")
