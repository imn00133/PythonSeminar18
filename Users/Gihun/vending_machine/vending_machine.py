#상품 정의
products = {'말차':500
           '녹차':600
           '라떼':650}
money = input("돈 넣으쇼:")
while not money.isdecimal():
    money = input("다시 넣으쇼:")

print("""1. 카페라떼(100원)
2. 녹차라떼(150원)
3. 오라떼(200원)
4. 거스름돈""")
print("넣은 돈: {money}".format(money=money))

selectnum = input("상품 번호를 입력하시게:")
