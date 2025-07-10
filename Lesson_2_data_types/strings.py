# String types
text = 'test'
a = 5
result = f'{text} {a}'
print(result)

data = 'value'

# method format()
result = "{} test {}".format(1, 2)
print(result)

result = "{one} test {two}".format(one='one', two='two')
print(result)

a = "{one} test {two}"
print(a)
result = a.format(one='one', two='two')
print(result)


x = list(a[::])
print(f"x = {x}")

# method split() - расколоть, разделить. Возвращает список(list)
print(a.split())
url = "etc/var/lib/myfile.txt"
result_url = url.split("/")
print(result_url)

# мы так же можем получить только последний элемент
result_url = url.split("/")[-1]
print(result_url)

# Method strip() убирает пробелы в начале и в конце
data_1 = " my username    "
print(data_1.strip())

# method lstrip() убирает пробелы только с лева
data_2 = "   my username    "
print(data_2.lstrip() + "1")

# method rstrip убирает пробелы только с права
data_3 = data_2.rstrip()
print(data_3)

# method startswith() проверяет с чем начинается строка и возвращает bool значение
url1 = "www.turbo.az"
url2 = 'http://turbo.az'
url3 = "https://turbo.az"

if url1.startswith("https"):
    print("url 1 start with https")
elif url2.startswith("https"):
    print("url 2 start with https")
elif url3.startswith("https"):
    print("url 3 start with https")
else:
    print("Nothing starts with https.")


# method endswith() проверяет с чем заканчивается строка и возвращает bool значение
url1 = "www.turbo.az"
url2 = 'http://turbo.com'
url3 = "https://turbo.net"

if url1.endswith(".com"):
    print("url 1 ends with .com")
elif url2.endswith(".com"):
    print("url 2 ends with .com")
elif url3.endswith(".com"):
    print("url 3 ends with .com")
else:
    print("Nothing ends with .com.")


# method replace(first_symbol, second_symbol) заменяет один символ на другой
sport_name = "Feeball"
replace_sport_name = sport_name.replace("ee", "oo")
print(replace_sport_name)
