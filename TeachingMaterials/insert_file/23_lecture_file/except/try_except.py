number_list = [1, 2, 3]

try:
    while True:
        index = int(input("인덱스를 입력하세요."))
        print(number_list[index])

except:
    print("오류 발생")

