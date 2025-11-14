first = int(input("введите первое число прогресси: "))
znaminatel = int(input("введите знаминатель прогрессии: "))
colichv = int(input("введите количество чисел в прогрессии: "))

for i in range(colichv):
    print(first, end=" ")
    first = first * znaminatel