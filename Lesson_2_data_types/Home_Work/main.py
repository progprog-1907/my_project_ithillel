def catalog_finder(url_list: list):
    """
    Дописать функцию, которая принимает список URL, а возвращает
    список только тех URL, в которых есть /catalog/
    """
    # your code here
    result_list = []
    for url in url_list:
        if url.find("/catalog/") != -1:
            result_list.append(url)

    return result_list


def get_str_center(input_str):
    """
    Дописать функцию, которая вернет Х символов из середины строки
    (2 для четного кол-ва символов, 3 - для нечетного).
    """
    # your code here
    output_str = ""
    len_str = int(len(input_str) / 2)
    output_str = input_str[len_str - 1:len_str + 2:] if len(input_str) % 2 else input_str[len_str - 1:len_str + 1:]
    return output_str


def count_symbols(input_str: str):
    """
    Дописать функцию, которая считает сколько раз каждая из букв
    встречается в строке, разложить буквы в словарь парами
    {буква:количество упоминаний в строке}
    """
    # your code here
    output_dict = dict()
    for sym in set(input_str):
        output_dict[sym] = input_str.count(sym)

    return output_dict

def mix_strings(str1, str2):
    """
    Дописать функцию, которая будет принимать 2 строки и вставлять вторую
    в середину первой
    """
    # your code here
    result_str = str1[:int(len(str1) / 2):] + str2 + str1[int(len(str1) / 2)::]
    return result_str

def even_int_generator():
    """
    Сгенерировать список из диапазона чисел от 0 до 100 и записать
    в результирующий список только четные числа.
    """
    # your code here
    even_int_list = list()
    for num in range(101):
        if num % 2 == 0:
            even_int_list.append(num)

    return even_int_list


catalog_urls = ["turbo.az/catalog/enter", "turbo.az/catalogs/enters", "turbo.az/catalogs/enter",
                "binance.com/catalog/enter", "turbos.az/catalog/enter"]
catalog = catalog_finder(catalog_urls)
print(catalog)
center_str = get_str_center("Salam")
print(center_str)
count_symbols_dict = count_symbols("Salam")
print(count_symbols_dict)
print(mix_strings("salam", "salam"))
print(even_int_generator())