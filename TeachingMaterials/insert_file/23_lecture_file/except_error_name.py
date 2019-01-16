number_list = [1, 2, 3]

try:
    while True:
        index = int(input("인덱스를 입력하세요."))
        print(number_list[index])
        print(number_list[index]/index)

except IndexError as e:
    print("인덱스 범위가 아닙니다.")
    print(type(e))

except ZeroDivisionError as e:
    print("0으로 나눌 수 없습니다.")

