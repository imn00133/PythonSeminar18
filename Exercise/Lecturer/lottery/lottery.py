import random

people_list = []
with open('people.txt', 'r', encoding='utf-8') as file:
    people_list = file.readlines()

with open('winner.txt', 'w', encoding='utf-8') as file:
    file.write("당첨\n")
    for i in range(6):
        file.write(people_list.pop(random.randint(0, len(people_list))))
    file.write("낙첨, 다음기회에\n")
    for people in people_list:
        file.write(people)
