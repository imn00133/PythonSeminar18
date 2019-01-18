file = open('test.txt', 'r', encoding='utf-8')
lines = file.readlines()
file.close()

print(lines)
for line in lines:
    print(line, end='')

