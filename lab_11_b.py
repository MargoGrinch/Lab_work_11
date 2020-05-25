# 5.
# б) Дано текстові файли f1 і f2. Переписати зі збереженням порядку проходження
# кожен другий компонент файлу f1 в f2, а кожен другий компонент файлу f2 - в файл f1.
# Використовувати допоміжний файл h.


# Грінченко Маргарита 1 курс група 122Б

with open('f1.txt', 'r') as f1:
    f1_s = f1.read()
    with open('h.txt', 'w') as h:
        for i in range(0, len(f1_s) - 1, 2):
            h.write(f1_s[i])
with open('f2.txt', 'r') as f2:
    f2_s = f2.read()
    with open('f1.txt', 'w') as f1:
        for i in range(0, len(f2_s) - 1, 2):
            f1.write(f2_s[i])
with open('h.txt', 'r') as h:
    h_s = h.read()
with open('f2.txt', 'w') as f2:
    f2.write(h_s)