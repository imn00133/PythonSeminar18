while True:
    answer = input("계속 반복합니까?(yes/no): ")
    if answer == "no":
        print("종료!")
        break
    elif answer == "yes":
        print("계속 반복!")
    else:
        print("yes/no를 입력하세요.")
