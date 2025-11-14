numb = int(input('введите натуральное число: '))
fib1 = 1
fib2 = 1

for i in range(numb):
    print(fib1, end = ' ')
    fib1, fib2 = fib2, fib1 + fib2


