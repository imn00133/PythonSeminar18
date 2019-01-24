# 상품 정의
products = list()
products.append(['감자', 300])
products.append(['고구마', 450])
products.append(['건포도', 500])
products.append(['히오스', 550])


money = input("돈 넣으쇼:")
while not money.isdecimal():
    money = input("다시 넣으쇼:")


pro_cnt = len(products)
# 상품 개수

menu = 0
while pro_cnt > menu:
    print('%d. %s: %d원' % (menu, products[menu][0], products[menu][1]))
    menu = menu + 1
print('%d. 거스름돈' % menu)

select = input("상품 번호를 쓰시게")
while not select.isnumeric():
    select = input("다시 쓰쇼:")

