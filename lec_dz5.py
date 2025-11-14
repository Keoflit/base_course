numb1 = int(input('введите первое число: '))
numb2 = int(input('введите второе число: '))

if numb2 == 0:
    print('на 0 делить нельзя')
else:
    if numb1 % numb2 == 0:
        print(f'{numb1} делится на {numb2}')
    else:
        print(f'{numb1} не делится на {numb2}')
print(f'{numb1} / {numb2} = {numb1 / numb2}')
print(f'{numb1} % {numb2} = {numb1 % numb2}')