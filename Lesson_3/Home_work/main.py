def idiotic_str(input_str):
    """
    Вернуть полученную строку, сделав каждую вторую букву заглавной:
    Пример: тестовая строка -> тЕсТоВаЯ СтРоКа
    """
    # your code here
    id_str = "".join([l.upper() if i % 2 else l.lower() for i, l in enumerate(input_str)])
    return id_str


print(idiotic_str("тестовая строка"))


def filter_unique_int(input_list):
    """
    Дан массив чисел.
    [10, 11, 2, 3, 5, 8, 23, 11, 2, 5, 76, 43, 2, 32, 76, 3, 10, 0, 1]
    убрать из него повторяющиеся элементы
    """
    # your code here
    return list(set(input_list))


print(filter_unique_int([10, 11, 2, 3, 5, 8, 23, 11, 2, 5, 76, 43, 2, 32, 76, 3, 10, 0, 1]))


def DNA_pair(chain: str):
    """
    Дана одна цепь ДНК. Найти вторую цепь ДНК зная, что связи
    аденин (A) возможны с тимином (T), а гуанина (G) с цитозином (C).

    A <-> T, G <-> C

    # in: "ATTGC" out: "TAACG"
    in: "GTAT" out: "CATA"
    """
    # your code here
    dna_dict = {
        "A": "T",
        "T": "A",
        "G": "C",
        "C": "G"
    }
    return True


def avg_score(score_list: list):
    """
    Дописать функцию, которая принимает список строк с оценками, а возвращает
    список строк со средним баллом
    Пример: ["Mike|83, 90, 34, 54", "Jane|45, 46, 53, 23"] ->
    ["Mike|65", "Jane|42"]
    """
    # your code here
    avg_scores = list()
    for student in score_list:
        name, score_str = student.split("|")
        scores = [int(mark) for mark in score_str.split(", ")]
        avg_mark = int(sum(scores) / len(scores))
        avg_scores.append(f"{name}|{avg_mark}")

    return avg_scores

print(avg_score(["Mike|83, 90, 34, 54", "Jane|45, 46, 53, 23"]))


def three_biggest_int(input_list: list):
    """
    Дан массив чисел.
    [10, 11, 2, 3, 5, 8, 23, 11, 2, 5, 76, 43, 2, 32, 76, 3, 10, 0, 1]
    вывести 3 наибольших числа из исходного массива
    """
    # your code here
    biggest_ints = []
    copy_list = input_list.copy()
    for i in range(3):
        max_val = max(copy_list)
        biggest_ints.append(max_val)
        copy_list.remove(max_val)
    return biggest_ints


print(f"Biggest 3 numbers {three_biggest_int([10, 11, 2, 3, 5, 8, 23, 11, 2, 5, 76, 43, 2, 32, 76, 3, 10, 0, 1])}")


def lowest_int_index(input_list: list):
    """
    Дан массив чисел.
    [10, 11, 2, 3, 5, 8, 23, 11, 2, 5, 76, 43, 2, 32, 76, 3, 10, 0, 1]
    вывести индекс минимального элемента массива
    """
    # your code here
    min_el = min(input_list)
    lowest_int_index_min = input_list.index(min_el)
    return lowest_int_index_min


print(f"index minimum elements is {lowest_int_index([10, 11, 2, 3, 5, 8, 23, 11, 2, 5, 76, 43, 2, 32, 76, 3, 10, 0, 1])}")


def reversed_list(input_list: list):
    """
    Дан массив чисел.
    [10, 11, 2, 3, 5, 8, 23, 11, 2, 5, 76, 43, 2, 32, 76, 3, 10, 0, 1]
    вывести исходный массив в обратном порядке
    """
    # your code here
    input_list.reverse()
    return input_list


print(f"reversed list {reversed_list([10, 11, 2, 3, 5, 8, 23, 11, 2, 5, 76, 43, 2, 32, 76, 3, 10, 0, 1])}")