item_list = [
    ['블랙커피', 100],
    ['밀크커피', 150],
    ['고급커피', 200],
    ['거스름돈', None]
    ]

input_money = int(input("돈을 넣으세요: "))

print("1. 블랙커피(100원)")
print("2. 밀크커피(150원)")
print("3. 고급커피(200원)")
print("4. 거스름돈")

print("넣은 돈: %d원" % input_money)

# list는 0부터 시작하기 때문에 계산의 편의를 위해 -1을 한다.
select_value = int(input("뽑을 물품을 골라주세요: "))-1
if 0 <= select_value < len(item_list):
    # 거스름돈을 선택하면 빠져나가도록 만든다.
    if select_value != len(item_list)-1:
        if input_money >= item_list[select_value][1]:
            input_money -= item_list[select_value][1]
            print("%s이/가 나왔습니다." % item_list[select_value][0])
        else:
            print("돈이 부족합니다.")

else:
    print("물품번호를 잘못 입력하셨습니다.")

# 프로그램을 종료하기 전에 항상 돈을 반환하도록 작성한다.
print("돈을 반환합니다.: %d원" % input_money)
