"""
기본과제-자판기1

돈을 입력받고 메뉴를 출력 후 현재 넣은 금액도 출력.
입력받는값은 정수.
"""
from time import sleep

cur_money = int(input("금액 입력하세요 : "))
# while not cur_money.isnumeric():
#     cur_money = input("숫자만 : ")
print('''1. 에스프레소(4000원)
2. 카페라떼(4500원)
3. 카라멜 마끼아또(5500원)
4. 카페모카(5500원)
5. 거스름돈
넣은 돈 : %s''' % cur_money)

product = [4000, 4500, 5000, 5500]
select = int(input("물품을 선택하세요(번호) : "))-1

if select == 4:
    print("잔액이 환불됩니다.")
elif not 0 <= select < len(product):
    print("잘못 입력했습니다.")
elif cur_money < product[select]:
    print("금액이 부족합니다.")
else:
    for i in range(100):
        msg = '\r%d%%' % (i+1)
        print(''*len(msg), end='')
        print(msg, end='')
        sleep(0.1)
    sleep(0.3)
    print("\n제품이 나왔습니다")
    cur_money = cur_money - product[select]
if cur_money == 0:
    print("잔액이 0원입니다.")
else:
    print("환불 : %d원" % cur_money)
