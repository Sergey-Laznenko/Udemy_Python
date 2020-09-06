"""
Создание dict
# 1

players = {'Bob': 12, 'Jek': 14, 'Kol': 15, 'Mel': 9}
print(players)

# 2

players = dict(Bob=12, Jek=14, Kol=15, Mel=9)
print(players)
"""

players = dict(Bob=12, Jek=14, Kol=15, Mel=9)

"""
# Присваиваем переменной ключ словаря
top = players['Bob']
print(f"Top players is {top}")

# Доступ к значению по ключу
players.get('Jek')

# Добавить ключ и значение в словарь
players['So'] = 19

# Добавить ключ со значением None в конец словаря
players.setdefault('Ruby')

# Обновить значение по ключу
players['So'] = 21

# Удаление пары из словаря
del players['So']
players.pop('So')

# Просмотр ключей и значений словаря через присвоение переменной
keys = players.keys()
vals = players.values()

# Создание списка ключей или значений
l = list(players.keys())
v = list(players.values())

# Сортировка ключей или значений и вывод отсортированного списка 
sorted(players.keys())
sorted(players.values())

# Создание копии 
players_copy = players.copy()

# Количество пар в словаре
len(players)

# Итерация по словарю и вывод в столбик
for k, v in players.items():
    print(k, v)
"""

