# Все мы умеем так:
a = [1, 2, 3]
for num in a:
    print(num * 2)

# Можно это сделать с list comprehension:
b = [num for num in a] # это означает что я хочу итерировать по листу a, и в самом левом мы пишем то что будиться
# записываться тесть, в нашем случае это копия листа a

# мы могли видеть где-то такое:
test = 1 if len(a) > 0 else "empty list" # Это называется тернарные операции
print(test)

# Тернарные операции так же, мы можем использовать в list comprehension
list_test = [num * 2 if num % 2 else num * 4 for num in a]
print(list_test)

# Правая часть это фильтрация
list_test2 = [num * 2 for num in a if num % 2]
print(list_test2)

b = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
list_test3 = [[str(string) for string in l] for l in b]
print(list_test3)

# DICT Comprehension
a = {"key1": 1, "key2": 2}
b = {f"new{k}": v for k, v in a.items()}
print(b)

# Можно еще итерироваться по листу
list_x = [1, 2, 3]
dict_a = {f"key{i}": i for i in list_x}
print(dict_a)