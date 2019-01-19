from random import randint

Doors = int(input("문은 몇개일까용?"))
Doors_toopen = int(input("몇개 열까용?"))
Try = int(input("몇번 할까용?ㅎ"))
count = Try
reselect_count = Try
result_reselect = 0
result = 0
reselct = False

while count > 0:
    answer = randint(1, Doors)
    user_choice = randint(1, Doors)

    if answer == user_choice:
        result += 1

    count -= 1

reselct = True

while reselect_count > 0:
    answer = randint(1, Doors)
    user_choice = randint(1, Doors)

    if answer != user_choice:
        set_monty = set()
        set_count = Doors

        while set_count > 0:
            set_monty.add(set_count)
            set_count -= 1

        set_removed = set()

        if user_choice in set_monty:
            set_monty.remove(user_choice)

        set_count = Doors_toopen

        while set_count > 0:
            temp = randint(1, Doors)
            if temp != answer:
                if temp in set_monty:
                    set_monty.remove(temp)
                    set_removed.add(temp)
                    set_count -= 1

        select = 0
        flag = True

        while flag:
            select = randint(1, Doors)
            if select != user_choice:
                if select not in set_removed:
                    flag = False

        if select == answer:
            result_reselect += 1
    if reselect_count % 10000 == 0:
        print("만번 해써염")
    reselect_count -= 1

result = (result/Try)
result_reselect = (result_reselect/Try)

print("안 바꿨을때 이길 확률 %f" % result)
print("바꿨을때 이길 확률 %f" % result_reselect)

"""
while count > 0:
    answer = randint(1, 3)
    user_choice = randint(1, 3)

    if answer == user_choice:
        result += 1
    count -= 1

reselct = True

while reselect_count > 0:
    answer = randint(1, 3)
    user_choice = randint(1, 3)

    if answer != user_choice:
        result_reselect += 1
    reselect_count -= 1

result = int(result/Try*100)
result_reselect = int(result_reselect/Try*100)

print("안 바꿨을때 이길 확률 %d%%" % result)
print("바꿨을때 이길 확률 %d%%" % result_reselect)
"""
