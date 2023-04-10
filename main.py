n = int(input("Введите трехзначное число: "))
sum = int(n/100) + int(n%100/10)  + int(n%10)
print(sum)

crane = int(input("Введите количество журавликов "))
temp = crane % 6
n = int(crane / 6)
if (temp == 0) :
    print(f"Катя сделала {n*4} журавликов, а Петя и Сережа по {n}" )
else:
    print("Нельзя определить")

tiket = input("Введите номер билета: ")
temp1 = int(tiket[0])+int(tiket[1])+int(tiket[2])
temp2 = int(tiket[3])+int(tiket[4])+int(tiket[5])
if temp1 == temp2: print("Вам достался счастливый билет")
else: print("Прокатитесь еще")

n = int(input("Введите значение n"))
m = int(input("Введите значение m"))
k = int(input("Введите значение k"))
if k%n == 0 or k%m == 0:
    print("yes")
else:
    print("no")