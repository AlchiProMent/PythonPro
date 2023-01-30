# чтение Excel файла и его последующий парсинг
#
import pandas as pnd

NAME_FILE_EXCEL = 'C:\Code\PythonPro\Excel\список.xlsx'

def get_seets(excel_name):
    # список для листов документа
    sheets_lst = []
    try:
        # загрузить файл
        sheets = pnd.ExcelFile(excel_name)
    except:
        print(f'Ошибка при открытии файла {excel_name}')
    else:
        for sheet_name in sheets.sheet_names:
            # Добавить в список очередной лист
            sheets_lst.append({sheet_name: sheets.parse(sheet_name)})
    # вернуть справочник
    return sheets_lst


def print_sheet(sheet_dict):
    # вывести на консоль содержимое листа

    # название листа
    sheet_name = list(sheet_dict.keys())
    page_name = sheet_name [0]
    # получить сам лист
    page = sheet_dict[page_name]

    # получить размерность таблицы
    size2d = page.shape
    # количество строк
    total_rows = size2d[0]
    # количество столбцов
    total_cols = size2d[1]

    # вывести название листа (и размерность)
    print(f'[ {page_name.upper()}: размер:{total_rows}x{total_cols} ]')

    # вывести все ячейки листа

    # получить первую строку в виде массива ячеек
    all_cols = page.columns
    # вывести в строку
    for col in all_cols:
        print(f'{col:<22}', end=' | ')

    # получить содержимое в виде таблицы
    table = page.values
    # вывести все строки
    for row in table:
        # вывести все ячейки строки
        for cell in row:
            print(f'{cell:<22}', end=' | ')
        # переход на новую строку
        print()

    # прогон пустой строки в конце таблицы
    print()


def go_parsing(file_name):
    # парсинг Excel-файла

    # получить все листы документа
    all_sheets = get_seets(file_name)

    # вывети на экран содержимое все листов
    for sheet in all_sheets:
        # вывести на экран текущий лист
        print_sheet(sheet)

    # вывод ячейки по индексу
    # print(page.iat[row_index, col_index])

if __name__ == '__main__':
    go_parsing(NAME_FILE_EXCEL)