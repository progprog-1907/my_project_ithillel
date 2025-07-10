# LIST изменяемый тип данных, конструкция [], индексация от 0 до n-1
# method append() добавляет в list элемент
list_1 = [1, 2, 3]
list_2 = [3, 4, 5]
list_1.append(0)
print(list_1)
list_1.append(list_2)
print(list_1) # как мы видим добавил вложенный лист

# что бы добавить несколько элементов тогда используем extend()
list_3 = [0, 1, 2]
list_3.extend(list_2)
print(list_3)

# method pop(index) удаляет элемент принимает номер индекса элемента
# method remove(element) удаляет элемент принимает элемент
# method sort(reverse=True/False) отсортирует лист, если не чего не примет то по умолчанию принимает False
# method sorted() он возвращает отсортированный лист но не меняет положение листа
a = [5, 1, 3, 0, 8, 6, 4]
sorted(a)
print(f"a = {a}")
c = sorted(a)
print(f"c = {c}")

# min(list) возвращает минимальный элемент листа
# max(list) возвращает максимальный элемент листа
min_el = min(a)
max_el= max(a)
print(f"minimum element in list = {min_el}")
print(f"maximum element in list = {max_el}")