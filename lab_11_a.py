# 5.
# а) Дан текстовий файл f. Отримати в файлі g кількість букв, що знаходяться в файлі
# f.

# Грінченко Маргарита 1 курс група 122Б

with open('f.txt', 'r') as f:
    f_s = f.read()
    # print(f_s)
    c = 0
    for i in f_s:
        if i.isalpha():
            c += 1
# print(c)
with open('g.txt', 'w') as g:
    g.write(f"{c}")
