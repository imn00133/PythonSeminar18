number_list = [1, 2, 3]

try:
    index = int(input("인덱스를 입력하세요."))
    print(number_list[index])

except IndexError as e:
    print("인덱스 범위가 아닙니다.", e)

else:
    print("인덱스가 내부에 있습니다.")
