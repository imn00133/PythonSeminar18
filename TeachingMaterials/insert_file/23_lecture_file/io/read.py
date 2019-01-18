file = open("test.txt", 'r', encoding='utf-8')
read_file = [file.read()]
file.close()
print(read_file)
