vegetables = input("enter your vegetables: \n")
listVegetables = vegetables.split(', ')
listVegetables = [item.lower() for item in listVegetables]
print(f'2 задание (Привести все овощи к нижнему регистру) {listVegetables}')
listVegetables = (','.join(listVegetables))
listVegetablesNotSpace = listVegetables.replace(' ','')
listVegetablesNotComa = listVegetables.replace(',', '')
# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------
uniqueLetters = set()
for vegetable in listVegetablesNotComa:
    uniqueLetters.update(set(vegetable))
uniqueLettersLen = len(uniqueLetters)
print(f"3 задание (Посчитать сколько всего уникальных букв\n встречается во всех названиях овощей) {uniqueLettersLen}")
# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------
maxCountO = 0
wordMaxO = ''
for i in listVegetables.split(','):
    if i.count('o') > maxCountO:
        maxCountO = i.count('o')
        wordMaxO = i
print(f"4 задание (Найти овощ с самым большим количеством букв О) {wordMaxO}")
# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------
vegetablesDict = {}
for i in listVegetables.split(','):
    vegetablesDict.update({ i: i.count('a') + i.count('e')+ i.count('i')+ i.count('o')+ i.count('u')+ i.count('y') })
print(f"5 задание (Название овоща и количество гласных в нем) {vegetablesDict}")
# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------
print("6 задание (Найти овощ в котором гласных больше всего)" ,max(vegetablesDict, key = vegetablesDict.get))
# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------
averageLength = len(listVegetablesNotComa)/len(listVegetables.split(','))
averageLengthDictionary = []
for i in listVegetables.split(','):
    if len(i) > averageLength:
        averageLengthDictionary.append(i)
print(f"7 задание (Сформировать список овощей длина которых больше среденей длины) {averageLengthDictionary}")
# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------
print("8 задание (Создать кортеж, в котором будут овощи в обратном порядке ввода)",listVegetables.split(',')[::-1])
# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------
vegetablesWithC = []
for i in listVegetables.split(','):
    if (i[0])[0] == 'c':
        vegetablesWithC.append(i)
if vegetablesWithC:
    print(f"9 задание (проверить, встречаются ли овощи начинающиеся на букву с или к) {vegetablesWithC}")
else:
    print('НЕТ ТАКИХ ОВОЩЕЙ')
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------

count = int(input('введите число \n'))
countDict = []
list = listVegetables.split(',')
for i in list:
    if len(i) > count:
        countDict.append(i)
print(f"10 задание (Вывести овощи у которых количество букв больше N) {countDict}")











