price = 3500, 5500, 4500, 4000
drink = "아메리카노", "딸기치즈케익할라치노", "그린티라떼", "콜드브루"

input_money = int(input("돈을 넣으세요: "))
return_money = input_money

print("1. 아메리카노(3500원)")
print("2. 딸기치즈케익할라치노(5500원)")
print("3. 그린티라떼(4500원)")
print("4. 콜드브루(4000원)")
print("5. 거스름돈")
print("넣은 돈 :", input_money, "원")

order = int(input("뽑을 물품을 골라주세요: "))

if order > 0 and order <= 4:
    if price[order-1] <= input_money:
        print(drink[order-1], "이/가 나왔습니다.")
        return_money = return_money - price[order - 1]
        print(return_money, "원을 반환합니다.")
    else:
        print("돈이 부족합니다.")
        print(return_money, "원을 반환합니다.")
elif order <= 5:
    return_money = input_money
    input_money = 0
    print(return_money, "원을 반환합니다.")

else:
    print("물품번호를 잘못 입력하셨습니다.")
    return_money = input_money
    input_money = 0
    print(return_money, "원을 반환합니다.")
