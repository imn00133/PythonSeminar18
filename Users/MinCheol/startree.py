print("*************별 트리 만들기*************\n\n")

condition = True
while condition:
    line_num = 0
    while not 0 < line_num < 80:
        line_num = int(input("그리고 싶은 별 트리의 줄 수를 입력하세요 (1~79) : "))
        if line_num < 0:
            print("종료합니다.")
            condition = False
            break
        if not 0 < line_num < 80:
            print("1에서 79까지만 입력할 수 있습니다.")

    count = 1
    while line_num > 0:
        print(" " * (line_num-1) + "*" * (count*2-1))
        line_num = line_num - 1
        count = count + 1

"""
질문이요

별 트리 줄 수 입력할 때 숫자 입력을 하지 않고 그냥 엔터를 치면
에러가 뜨는데 cmd에서처럼 값을 입력할 떄까지 다시 입력창이 뜨게
하는 방법이 있나요?
"""
