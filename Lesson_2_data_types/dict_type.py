# DICT - словари. Это множество пар. Он изменяемый тип данных. Пары ключ и значение.
# Конструктор {}, dict(one=2), {"one": 1}
# Индексация по ключам

a = {}
print(f"type a is {type(a)}")
# почему не сет?

b = {1, 2, 3, 4}
print(f"type b is {type(b)}")

c = {"1": 1, "2": 2, "3": 3}
print(f"type c is {type(c)}")

a = {'1': 1, '2': 2, 3: 3}

# Dict, как и set не хранят порядок хранение, не когда не нужно расщипывать на циклы for по dict-ом потому что не
# всегда вы получите порядок элементов. На маленьких dict-ов ок! Но всегда нужно знать что это не так работает.

# Добавление пар элементов в словарь:
a.update({'x': 'y'}) # этот вариант хорош для сведения двух dict-ов в один или, вы фактически хотите добавить
# не сколько ключей
print(f"a = {a}")
# Можно и так
a["One"] = 1
print(f'a = {a}')
# То есть если нет ключа то создаст новый ключ а, если есть то тогда изменит содержимый
a["One"] = 2 # Этот вариант хорош для добавления одного ключа
print(f"a = {a}")
# Ключи бывают уникальными!


# Method keys() - возвращает список всех ключей
x = a.keys()
print(x)
print(type(x))

# Method values() - возвращает список всех значений
y = a.values()
print(y)
print(type(y))

# Method items() - возвращает list в котором у нас tuple, где каждый tuple это ключ и значение
a_items = a.items()
print(a_items)
print(type(a_items))




data = {"response": 200, "data": {"user": "Yehor", "id": 1, "orders": {"discount": 1}}}

if data.get("response"):
    print(data.get("response"))

if data.get("respons"):
    print(data.get("respons"))
else:
    print("404")

# в место этого можем сделать так:
print(data.get("respons", "404"))
print(data.get("response", "404"))

# мы можем вот так проверить вложенные dict-ы
print(data.get("data").get("orders").get("discount")) # как мы видим нашли значение
# А что если нет?
# print(data.get("data").get("order").get("discount")) # ошибка AttributeError
# У AttributeError нет говорит метод get(). Можно обойти это следующим образом, страхуя себя
print(data.get("data", {}).get("order", {}).get("discount", {}))