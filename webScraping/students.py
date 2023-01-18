# создание списка студентов из XML-файла
#
import xml.etree.ElementTree as et

xml_students = 'XML/students.xml'

# парсинг файла
dom = et.parse(xml_students)
# получить корневой элемент
root = dom.getroot()

# пропуск строки в консоли
print()
# получить название документа
title = root.find('title')
# вывести его на экран
print(title.text.upper())

# разделяющая линия
line = '-'*80
print(line)

# получить описание столбцов таблицы
header = root.find('header')
print(f'{header.find("col1").text:5}{header.find("col2").text:20}{header.find("col3").text:18}' \
      f'{header.find("col4").text:10}{header.find("col5").text:10}{header.find("col6").text}')
print(line)

# получить описание списка студентов
students = root.find('students')
# сформировать таблицу списка студентов
for student in students:
    # получить элемент campus
    campus = student.find('campus')
    # проверить наличие этого элемента
    if campus != None:
        print(f'{student.find("num").text:5}{student.find("name").text:20}{student.find("city").text:18}' \
              f'{student.find("faculty").text:10}{student.find("campus").text:10}{student.find("address").text}')
    else:
        print(f'{student.find("num").text:5}{student.find("name").text:20}{student.find("city").text:18}' \
              f'{student.find("faculty").text:10}')
    print(line)



