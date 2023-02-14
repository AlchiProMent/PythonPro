# горизонтальная столбчатая диаграмма
import matplotlib.pyplot as plt

# взносы
fees = {'США': 678613.82,
        'Китай': 370307.22,
        'Япония': 264165.85,
        'Германия': 187852.64,
        'Великобритания': 140874.06,
        'Франция': 136555.61,
        'Италия': 102007.99}

payments = list(fees.values())
nations = list(fees.keys())

fg, ax = plt.subplots(figsize=(10, 6))
ax.barh(nations, payments)
ax.set(xlim=[-10_000, 700_000], xlabel='Взносы в 2020 году', ylabel='Членские взносы в ООН (тыс долл США)')

# повернуть обозначения на 90 градусов
labels = ax.get_xticklabels()
plt.setp(labels, rotation=90)

# компактное размещение
plt.tight_layout()

plt.show()