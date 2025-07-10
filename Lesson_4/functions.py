# Filter
# Создает список элементов, в отношении которых используемая функция возвращает True. Например:
from functools import reduce

data = [1, 2, 3, 4,5]
def filter_data(value):
    return True if value % 2 else False


result = filter(filter_data, data)
print(type(result))

for i in result:
    print(i)


# многие сразу пишут так
result2 = list(filter(filter_data, data))
print(result2)

# Еще пример:
def non_zero(num: int):
    return True if num > 0 else False


input_func = [-5, -1, 0, 1, 5]
filtered = filter(non_zero, input_func)
print(filtered)
result_filtered = list(filtered)
print(result_filtered)


# MAap - применяет функцию ко всем элементам множества
def sqrt(val):
    return val**2


input_map = [1, 2, 3]
mapped = map(sqrt, input_map)
print(mapped)
result_mapped = list(mapped)
print(result_mapped)


# Reduce кумулятивно применяет функцию ко всем элементом множества слева на право, приводя их к единому значению.
def sum_int(int1, int2):
    return int1 + int2

input_sum_int = [1, 1, 2, 3, 5, 8]
reduced = reduce(sum_int, input_sum_int)
print(reduced)


# Lambda - короткая in-line анонимная функция с единственным выражением, результат
# которого и возвращается “наружу”. Не поддерживает никаких фич языка.
def sum1(x, y):
    return x + y

input1 = [1, 1, 2, 3, 5, 8]
reduced1 = reduce(sum1, input1)
reduced2 = reduce(lambda x, y: x + y, input1)
print(reduced2)

add = 10
lam = lambda v: v + add
print(lam(15))

funcs = [lambda x, n=n: x+n for n in range(5)]
results = list()
for i in funcs:
    results.append(i(0))

print(results)