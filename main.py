a = str(input("Введите строку: "))
sogl = "йфцчвскмптрнглбшдщзжх"
glas = "яыуаиеоюё"
count1 = 0
count2 = 0
for i in a.lower():
    if i in sogl:
        count1 += 1
    if i in glas:
        count2 += 1
print("Количество гласных " + str(count2) + " , количество согласных " + str(count1))
print("Длина строки " + str(len(a)))
