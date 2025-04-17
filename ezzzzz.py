

# Разбиваем на числа и операторы
def main():
  primer = input("Введите пример (например, 3 + 4 * 2): ")
  zadacha = []
  number = ''
  for perem in primer:
      if perem in '+-*/':
          if number:
              zadacha.append(int(number))
              number = ''
          zadacha.append(perem)
      elif perem.isdigit():
          number += perem
      elif perem == ' ':
          continue
  if number:
      zadacha.append(int(number))

  # Выполняем вычисление слева направо (без приоритета операций)
  result = zadacha[0]
  i = 1
  while i < len(zadacha):
      op = zadacha[i]
      num = zadacha[i + 1]
      if op == '+':
          result += num
      elif op == '-':
          result -= num
      elif op == '*':
          result *= num
      elif op == '/':
          result /= num
      i += 2
  print("Результат:", result)
  return prodolgenie(result)
#Функция для продолжения вычислений
def prodolgenie(result):
  primer=input("Введите продолжение(Например, *3,+32,-6):")
  chislo = ''
  flag = 0
  for x in primer:
    if flag == 0:
      znak = primer[flag]
    else:
      chislo += x
    flag += 1 
  chislo = int(chislo)
  if znak == '+':
        result += chislo
  elif znak == '-':
        result -= chislo
  elif znak == '*':
        result *= chislo
  elif znak == '/':
        result /= chislo  
  print(result)  
  return prodolgenie(result)
main()
                
                    

  
  