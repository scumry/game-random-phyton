import random 
a = int(input('Угадайте рандомное число: '))
c = random.randint(1, 100)
while a != c:
  if a < c:
    print('Слишком мало, попробуйте еще раз')
  else:
    print('Слишком много, попробуйте еще раз')
  a = int(input('Угадайте рандомное число: '))
  if a == c:
    print('Вы угадали, поздравляем!')
