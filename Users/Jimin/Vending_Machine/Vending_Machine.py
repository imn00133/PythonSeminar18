
money = int(input("돈을 넣으세요: "))

print("1. 오라떼 사과(550원)")
print("2. 갈아만든 배(800원)")
print("3. 박카스F(1000원)")
print("4. 거스름돈")
print("넣은 돈:%d원" % money)
# print("넣은 돈:",money,"원")

num = int(input("뽑으실 물품을 골라주십시오 : "))
if num < 1 or num > 4:
    print("물품 번호를 잘못 입력하셨습니다.")
    print("돈을 반환합니다.  [%d원] 짤랑 " % money)
elif num == 4:
    print("돈을 반환합니다.  [%d원] 짤랑 " % money)

elif num == 1:
    if money < 550:
        print("금액이 부족합니다.")
        print("돈을 반환합니다.  [%d원] 짤랑 " % money)
    else:
        print("(오라떼 사과)이/가 나왔습니다.")
        print("거스름돈 %d원" % (money - 550))

elif num == 2:
    if money < 800:
        print("금액이 부족합니다.")
        print("돈을 반환합니다.  [%d원] 짤랑 " % money)
    else:
        print("(갈아만든 배)이/가 나왔습니다.")
        print("거스름돈 %d원" % (money - 800))

elif num == 3:
    if money < 1000:
        print("금액이 부족합니다.")
        print("돈을 반환합니다.  [%d원] 짤랑 " % money)
    else:
        print("(박카스F)이/가 나왔습니다.")
        print("거스름돈 %d원" % (money - 1000))
