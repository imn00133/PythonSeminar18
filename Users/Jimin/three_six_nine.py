
def isMultiple3(num):
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
        arr.insert(0, num % 10)
        num /= 10
    return arr

def s6g(num):
    arr = position(num)
    for num2 in arr:
        isMultiple3(num2) 

num = int(input("마지막 number를 입력하숑 : "))
s6g(num)
