'''
На ферме есть куры, коровы и свиньи. Запросить кол-во животных
Просуммировать и вывести результат на консоль
'''


chiken = int(input('Введите кол-во кур: '))
cow = int(input('Введите кол-во коров: '))
pig = int(input('Введите кол-во свиней: '))

total = (chiken * 2) + (cow * 4) + (pig * 4)

print(f'Общее кол-во ног животных на ферме, равняется - {total}')