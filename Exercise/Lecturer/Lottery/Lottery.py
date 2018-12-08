import random

people_list = []
with open('People.txt', 'r', encoding='utf-8') as file:
    people_list = file.readlines()

lottery_num = int(input("추첨할 인원을 적어주세요: "))
with open('Winner.txt', 'w', encoding='utf-8') as file:
    file.write("당첨\n")
    for i in range(lottery_num):
        file.write(people_list.pop(random.randint(0, len(people_list)-1)))
    file.write("낙첨, 다음기회에\n")
    for people in people_list:
        file.write(people)
