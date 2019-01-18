write_lines = (
    "Hello World!\n",
    "Python is Easy\n",
    "write text"
)
file = open('multiline.txt', 'w', encoding='utf-8')
file.writelines(write_lines)
file.close()
