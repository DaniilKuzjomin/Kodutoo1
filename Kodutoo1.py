from random import *
spisok=[]
numbers=[1,2,3,4,5]
abc=["Abc","B","C"]
slovo="Программирование"
slovo_list=list(slovo)

while True:
  print("1-добавить букву в список\n2-склеить списки\n3-добавить букву на i-позицию\n4-развернуть список\n5-отсортировать буквы от А до Я\n6-удалить элемент из списка\n7-написать текст вертикально\n8-найти длину слова\n9-выберает рандомный транспорт из списка\n10-Делает все буквы заглавными ")
  print()

  valik=int(input())
  if valik==1:
    a=input("Введи букву ")
    slovo_list.append(a)
    print(f"Добавили {a} новый список",slovo_list)
  elif valik==2:
    slovo_list.extend(abc)
    print(slovo_list)
  elif valik==3:
    a=input("Введи букву, которую хочешь добавить")
    i=int(input("Введи номер позиции, куда хочешь добавить"))
    slovo_list.insert(i-1,a)
    print(slovo_list)
  elif valik==4:
    slovo_list.reverse() #Разворачиваем список
    print(slovo_list) #Выводим список на экран
  elif valik==5:
    slovo_list.sort() # Сортируем в алфавитном порядке
    print(slovo_list) # Выводим список на экран
  elif valik==6:
    a=int(input("Введи цифру(от 1-16), и оно удалить букву под этим номером ")) #Просим пользователя ввести номер  буквы
    print(slovo_list.pop(a)) # Выводим на экран букву под этим номером
    print(slovo_list) # Выводим список на экран
  elif valik==7:
    print(slovo_list[0]) #Выводим на экран 1ую букву и т.д  |
    print(slovo_list[1])
    print(slovo_list[2])
    print(slovo_list[3])
    print(slovo_list[4])
    print(slovo_list[5])
    print(slovo_list[6])
    print(slovo_list[7])
    print(slovo_list[8])
    print(slovo_list[9])
    print(slovo_list[10])
    print(slovo_list[11])
    print(slovo_list[12])
    print(slovo_list[13])
    print(slovo_list[14])
    print(slovo_list[15])
  elif valik==8:
    a=[] # Создаём список
    a=input("Введи слово, что бы посчитать сколько в нём букв ") # Просим пользователя ввести слово для подсчёта символов
    print(len(a)) # Выводим сколько в этом слове букв
  elif valik==9:
    spisok1=["Автомобиль","Автобус","Троллейбус","Такси","Трамвай"] # Задаем список
    a=randint(1,4) # Генерируем рандомное число
    print(spisok1) # Выводим список
    print(spisok1[a]) # Выводим слово из списка
  elif valik==10:
    a=input("Введите слово ") # Просим написать слово
    a_upper = [ i.capitalize() for i in a] # Делаем все буквы заглавными
    print(a_upper) # Выводим на экран слово заглавными буквами
  else: # В другом случае, если человек вводит другие цифры 
      print("Error") # Выводим на экран ошибку
