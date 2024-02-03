from random import randint

random = randint(1, 100)

while True:
    guess = int(input('Введите число: '))
    if guess == random:
        break

print('Угадал!')