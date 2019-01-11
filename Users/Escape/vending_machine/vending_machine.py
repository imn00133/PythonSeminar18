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
# cnt = 물품 번호(출력 이후, cnt는 전체 물품 개수가 됩니다.)
# product[0] = 이름, product[1] = 가격
cnt = 0
for product in product_list:
    cnt += 1
    print('%d. %s(%d원)%s' % (cnt, product[0], product[1],
                             ('', ' - 구매 불가')[money < product[1]]))
print('%d. 거스름돈' % (cnt + 1))

# 물품을 선택받습니다.
try:
    product_in = int(input('잔액: %d원\n뽑을 물품을 선택해주세요: ' % money))
except ValueError:
    product_in = cnt + 2

# 잘못 입력한 경우
if product_in > cnt + 1:
    print('물품 번호를 잘못 입력하셨습니다.')
# 거스름돈을 선택한 경우
elif product_in == cnt + 1:
    # 아무 것도 안 넣으면 에러가 나와서 아무 것도 안 출력하는 부분을 넣었습니다.
    print(end='')
# 물품을 선택한 경우
else:
    # 리스트는 0번부터 시작하는데 물품번호는 1번부터 시작이므로 1을 빼줍니다.
    # 돈이 충분하면 물품을 내보냅니다.
    product = product_list[product_in - 1]
    if money >= product[1]:
        money -= product[1]
        print('%s을(를) 구매하셨습니다.' % product[0])
    else:
        print('돈이 부족합니다.')

# 잔액이 0원인 경우 '0원이 반환됩니다.' 뜨는 것 해결하기
if money > 0:
    print('%d원이 반환됩니다.' % money)
else:
    print('잔액이 없어 돈이 반환되지 않습니다.')
