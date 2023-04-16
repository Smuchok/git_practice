print('Hello world!')

number = 0
with open('data.txt', 'r') as f:
  number = int(f.read())

while True:
  inp = input("МЕНЮ:\n1 - Задати число\n2 - Змінити\n3 - Занулити\n0 - Вийти")
  if inp == '1':
    number = int(input('Задайте число: '))
  elif inp == '2':
    number = int(input('Змінити число: '))
  elif inp == '3':
    number = 0
  elif inp == '0':
    break
