
def isMultiple3(num): # num을 int로 받기! , 3의 배수인지 확인해 출력하기 return 안한다 뛰어쓰기는 나중에 하자
    i = 1
    while i <= num:
        if i % 3 != 0:
            print(i)
        else:
            print("짝")

def position(num):
    i = 0
    while num / 10 != 0:
        i += 1
    arr = []
	j = 0
	while j <= i:
        arr.insert(0,num % 10)
        num /= 10
	return arr

def s6g(num):
    arr = position(num)
    

num = int(input("마지막 number를 입력하숑 : "))
s6g(num)