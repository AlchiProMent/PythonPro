# проверка спама методом наивного байесовского классификатора
from pandas import DataFrame

TITLE = 'title'
MARK_1 = 'mark1'
MARK_2 = 'mark2'
SPAM = 'spam'
TOTAL = 'total'
COUNT_IND = 'count'
IS_SPAM = 'спам'
NOT_SPAM = 'нет'

# исходная таблица данных
spam_table = DataFrame({TITLE: ['предложение',
                                'предложение',
                                'привет',
                                'совещание',
                                'совещание',
                                'совещание',
                                'привет',
                                'предложение',
                                'предложение',
                                'совещание',
                                'предложение',
                                'привет',
                                'привет',
                                'совещание'],
                        MARK_1: ['рост',
                                 'рост',
                                 'рост',
                                 'рост',
                                 'переговоры',
                                 'переговоры',
                                 'переговоры',
                                 'рост',
                                 'переговоры',
                                 'переговоры',
                                 'переговоры',
                                 'рост',
                                 'переговоры',
                                 'рост'],
                        MARK_2: ['доходы',
                                 'продажи',
                                 'доходы',
                                 'доходы',
                                 'доходы',
                                 'продажи',
                                 'продажи',
                                 'доходы',
                                 'доходы',
                                 'доходы',
                                 'продажи',
                                 'продажи',
                                 'доходы',
                                 'продажи'],
                        SPAM: [True,
                               True,
                               False,
                               False,
                               False,
                               True,
                               False,
                               True,
                               False,
                               False,
                               False,
                               False,
                               False,
                               True]})


def k_bayes_calc(p_b_a, p_a, p_b):
    # расчитать вероятность по формуле Байеса
    return p_b_a * p_a / p_b


def create_freq_tab(df, col_name, total_spam, total_no_spam, calc_div=False):
    # полная сумма всех событий таблицы
    total_answers = total_spam + total_no_spam
    # сформироват таблицу частоты значений для столбца col_name
    new_df = DataFrame(df[col_name].value_counts())
    # переименовать столбец (для удобства дальнейшей работы, чтобы не путать со столбцом основной таблицы)
    new_df.rename(columns={col_name: TOTAL}, inplace=True)
    # добавить столбцы с нулевыми значениями
    new_df[IS_SPAM] = 0
    new_df[NOT_SPAM] = 0

    total_rows = 0
    # рассчитать количество появлений сообщений СПАМ и НЕ СПАМ для атрибутов каждого наблюдения
    for ind in new_df.index:
        new_df.loc[ind][IS_SPAM] = df[(df[SPAM] == True) & (df[col_name] == ind)][col_name].count()
        new_df.loc[ind][NOT_SPAM] = df[(df[SPAM] == False) & (df[col_name] == ind)][col_name].count()
        # увеличить счётчик добавленных строк
        total_rows += 1

    # добавить итоговый столбец
    new_df.loc[COUNT_IND] = [0, total_spam/total_answers, total_no_spam/total_answers]

    # если указан параметр, количество появлений перевести в частоты
    if calc_div:
        for ind in range(total_rows):
            new_df.iloc[ind][TOTAL] /= total_answers
            new_df.iloc[ind][IS_SPAM] /= total_spam
            new_df.iloc[ind][NOT_SPAM] /= total_no_spam
    # вернуть полученную таблицу
    return new_df

def get_prob(df, mark_txt, spam_or_no):
    # получить вероятность для указанного элемента
    if (mark_txt in df.index) and (spam_or_no in df.columns):
        # получить частоту по запросу
        p_b_a = df.loc[mark_txt][spam_or_no]
        p_a = df.loc[COUNT_IND][spam_or_no]
        p_b = df.loc[mark_txt][TOTAL]
        return p_b_a * p_a / p_b
    else:
        print('Ошибка индексов')
        return -10000000

def start_bayes():
    # стартовая функция

    # получить количество ответов ДА и НЕТ в графе СПАМ
    spam_no, spam_yes = spam_table[SPAM].value_counts()

    freq_tabs = {}
    # пройтись по всем столбцам таблицы
    for col in spam_table.columns:
        # добавить очередную таблицу частот в виде спавочника
        freq_tabs[col] = create_freq_tab(spam_table, col, spam_yes, spam_no, calc_div=True)

    test_count = 0
    total_spams = 0
    unident_count = 0
    # ввод заголовка письма в цикле
    while ( title_txt := input('Заголовок письма: ')) != '':
        if title_txt != '':
            # ввод дополнительных маркеров
            mark1_txt = input('Маркер 1: ')
            mark2_txt = input('Маркер 2: ')

            # увеличить счетчик проведенных тестов
            test_count +=1

            # вероятности для спама по каждой позиции
            p11 = get_prob(freq_tabs[TITLE], title_txt, 'спам')
            p12 = get_prob(freq_tabs[MARK_1], mark1_txt, 'спам')
            p13 = get_prob(freq_tabs[MARK_2], mark2_txt, 'спам')

            # вероятности для не спама по каждой позиции
            p21 = get_prob(freq_tabs[TITLE], title_txt, 'нет')
            p22 = get_prob(freq_tabs[MARK_1], mark1_txt, 'нет')
            p23 = get_prob(freq_tabs[MARK_2], mark2_txt, 'нет')

            # расчёт полной вероятности для спама (сумма произведений частот на вероятность)
            p1 = freq_tabs[TITLE].loc[title_txt, 'спам']*p11 + \
                 freq_tabs[MARK_1].loc[mark1_txt, 'спам']*p12 + \
                 freq_tabs[MARK_2].loc[mark2_txt, 'спам']*p13
            # расчёт полной вероятности для не-спама
            p2 = freq_tabs[TITLE].loc[title_txt, 'нет']*p21 + \
                 freq_tabs[MARK_1].loc[mark1_txt, 'нет']*p22 + \
                 freq_tabs[MARK_2].loc[mark2_txt, 'нет']*p23

            # окончательный вывод о том, спам это или нет
            if p2 > p1:
                print('Это не спам')
            else:
                if round(p2,1) == round(p1,1):
                    print('Сложный вопрос. Может спам, а может нет. Надо ещё подумать...')
                    unident_count += 1
                else:
                    print(f'Это скорее всего спам')
                    # увеличть счетчик спама
                    total_spams += 1

            print()

    print()
    print(f'Проведено опытов всего: {test_count}')
    print(f'Найдено спама всего: {total_spams}')
    if (unident_count > 0):
        print(f'Неопознанных: {unident_count}')


if __name__ == '__main__':
    start_bayes()
    print('Программа закончила работу.')
