print(5)
print(type(5)) # int - !! integer(целые числа)
print(5 / 5) # // - целочисленное деление, / - деление
print(5 % 5) # остаток от деления
print(5 ** 5) # возведение в степень

print(type(2.0)) # !! float - числа с плавающей точкой/запятой(плавающие/дробные числа). float+int=float. Числа - неизменяемые типы

print(type('Hello, world1')) # !! string - строка(тип данных - текст). Отличие " от ' - необходимость отобразить кавычки
print('Hello, ' + 'world!')# строки поддерживают операцию сложение concatenate. Вычитать строки нельзя!
# '1' + 1) # '1' является текстом а не числом. Операции можно проводить только с одним типом данных
print(type(True), type(False)) # !! boolean - логический тип данных. Важно писать с большой буквы иначе не распознаются
print(5 < 234, 32 > 233, 5, 'hello world', True) # "print" поддерживает ввод разных типов данных через разделители. Это не выполнение функций, а перечисление по сути
print(5 != 5) # "<=" - меньше или равно, ">=" - больше или равно, "==" - равно, "!=" - не равно
print(5 != 5 or 5 > 10) # "and" - и (строгий оператор) "or" - или (нестрогий оператор)

print(type(bool('5'))) # команды "int" - целые числа, "bool" - логические выражения, "str" - текст, "float" - дробные; переводят один тип в другой
#23891471923807487.142352314353455
#23891471923807487.142352314356734
#23891471923843245.142352314334563
#23891471923843245.142352314334553

print(23891471923807487.142352314353455 + 23891471923843245.142352314334563 < 23891471923807487.142352314356734 + 23891471923843245.142352314334553)