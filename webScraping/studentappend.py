# добавление студентов в список
#
import xml.etree.ElementTree as et


def append_student(students, st_name, st_city, st_faculty, st_campus='', st_address=''):
    # добавление студента st_name в список

    # создать новый элемент student
    student = et.SubElement(students, 'student')

    # создать все вложенные элементы и внести в них значение

    # номер
    new_num = et.SubElement(student, 'num')
    new_num.text = '0'
    # имя
    new_name = et.SubElement(student, 'name')
    new_name.text = st_name
    # город
    new_city = et.SubElement(student, 'city')
    new_city.text = st_city
    # факультет
    new_faculty = et.SubElement(student, 'faculty')
    new_faculty.text = st_faculty

    if st_campus != '':
        # добавить только если введена информация об общежитии
        new_campus = et.SubElement(student, 'campus')
        new_campus.text = st_campus
        new_address = et.SubElement(student, 'address')
        new_address.text = st_address

xml_students = 'XML/students.xml'
# парсинг файла
dom = et.parse(xml_students)
# получить корневой элемент
root = dom.getroot()
# получить описание списка студентов
students = root.find('students')

# запрашивать в цикле продолжение ввода в список
while (key := input('\nДобавить студента в список? (1 - Да; 0 - Нет): ')) != '0':
    # если выбран режим добавления
    if key == '1':
        # запросить ввести все данные
        if (name := input('Имя: ')) != '':
            # запросить остальные данные, если было введено имя
            city = input('Место рождения: ')
            faculty = input('Факультет: ')
            campus = input('Общежитие: ')
            address = input('Адрес: ')

            # добавить студента в DOM
            append_student(students, name, city, faculty, campus, address)

# перенумеровать и отсортировать список перед сохранением
students[:] = sorted(students, key=lambda st: st.find('name').text)
for index, student in enumerate(students):
    num = student.find('num')
    num.text = str(index + 1)

# сохранить изменения в файл
try:
    dom.write(xml_students, encoding='utf-8')
except:
    print('При сохранении возникла ошибка!')
else:
    print('Данные успешно сохранены')
