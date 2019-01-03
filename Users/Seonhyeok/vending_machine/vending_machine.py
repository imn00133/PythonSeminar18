money = 0
input_money = input("돈을 넣으세요 : ")
money += int(input_money)

print("""1. 블랙커피(100원)
2. 밀크커피(150원)
3. 고급커피(200원)
4. 거스름돈
넣은 돈: %d원""" % money)
