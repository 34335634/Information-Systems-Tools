#Задание 1
def palindrome_check(s):
    reverse = ''.join(reversed(s))
    if s == reverse:
        return "Да"
    return "Нет"


s = input("Введите строку: ")

print(palindrome_check(s))

#Задание 2
lst = []
b = []
c = []
while True:
    value = input()
    if value == "end":
        break
    row = [int(i) for i in value.split()]
    lst.append(row)
for i in range(len(lst)):
    for j in range(len(lst[i])):
        print(lst[i][j], end = " " , sep = " ")
for m in range(len(lst)):
   for n in range(len(lst[0])):
      print(lst[m][n], end=' ')
   print()
print("Минимальные значения строк:")
for k in lst:
      print(min(k))

#Задание 3
string = input('Введите текст: ').lower().split()
for i, word in enumerate(set(string), 1):
    print(f'{i}. {word} {string.count(word)} раз.')


#Задание 4

import pymysql
try:
    connect = pymysql.connect(
        host='127.0.0.1',
        #port=3306,
        user='root',
        password='ppass',
        database='my_db',
        cursorclass=pymysql.cursors.DictCursor
    )
    print("successfully connected...")
    print("#" * 20)

    try:
        pass

    finally:
        connect.close()

except Exception as ex:
    print("Connection refused...")
    print(ex)
