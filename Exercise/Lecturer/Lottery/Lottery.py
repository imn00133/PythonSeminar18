import random

people_list = []
with open('People.txt', 'r', encoding='utf-8') as file:
    people_list = file.readlines()

<<<<<<< HEAD:Exercise/Lecturer/lottery/lottery.py
lottery_num = int(input("추첨할 인원을 적어주세요: "))
with open('winner.txt', 'w', encoding='utf-8') as file:
=======
with open('Winner.txt', 'w', encoding='utf-8') as file:
>>>>>>> 2d08e3165fdb9c07c0aaa650e8c7304daa46b6d8:Exercise/Lecturer/Lottery/Lottery.py
    file.write("당첨\n")
    for i in range(lottery_num):
        file.write(people_list.pop(random.randint(0, len(people_list)-1)))
    file.write("낙첨, 다음기회에\n")
    for people in people_list:
        file.write(people)
