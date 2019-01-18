file = open('test.txt', 'w', encoding='utf-8')
for index in range(1, 6):
    write_line = "%d줄\n" % index
    file.write(write_line)
file.close()
