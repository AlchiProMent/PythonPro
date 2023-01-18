# удаление в XML-файле
#
import xml.etree.ElementTree as et

xml_students = 'XML/students.xml'
# парсинг файла
dom = et.parse(xml_students)
# получить корневой элемент
root = dom.getroot()
# получить описание списка студентов
students = root.find('students')

del_key = input('Введите номер удаляемой записи: ')
num_deleted = False
for student in students:
    num = student.find('num')
    if del_key == num.text:
        students.remove(student)
        num_deleted = True
        print('Запись удалена')
        # принудительно выйти из цикла
        break

# если запись была удалена
if num_deleted:

    # перенумеровать
    for index, student in enumerate(students):
        num = student.find('num')
        num.text = str(index + 1)

    # сохранить изменения в файл
    try:
        dom.write(xml_students, encoding='utf-8')
    except:
        print('При сохранении возникла ошибка!')
    else:
        print('Данные успешно сохранены.')
