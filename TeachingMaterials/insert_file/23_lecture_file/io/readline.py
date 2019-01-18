wfile = open('test.txt', 'r', encoding='utf-8')
while True:
    line = file.readline()
    if not line:
        break
    print(line, end='')
file.close()

