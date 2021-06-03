num ="1"

with open("test1.txt","r",encoding="utf-8") as file:
   int_number = file.readlines()
#print(int_number)
# Ищем данные
for i in int_number: # перебор всех элементов
    if num in i: # Проверка на наличие номера
        print(i)