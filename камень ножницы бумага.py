import random
def game():
 library=['Камень','Ножницы','Бумага']
 
 vibor1 = input('Камень, Ножницы, Бумага\n')
 vibor = vibor1.lower()
 
 random2 = random.choice(library)
 random1 = random2.lower()
 
 if random1 == vibor:
  print(random2, "— Ничья")
 elif random1 == 'камень' and vibor == 'бумага':
  print(random2, '— Вы выиграли')
 elif random1 == 'бумага' and vibor =='ножницы':
  print(random2, '— Вы выиграли')
 elif random1 == 'ножницы' and vibor == 'камень':
  print(random2, '— Вы выиграли')
 else:
  print(random2, '— Вы проиграли')
game()
#расширить список ввода