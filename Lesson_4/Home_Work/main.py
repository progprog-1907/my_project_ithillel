def validate_password(password: str) -> bool:
    """
    Функция принимает пароль строкой и выполняет валидацию с помощью трёх
    вспомогательных функций:
    1. Содержит только a−z, A−Z, 0−9
    2. Содержит четное количество букв
    3. Содержит нечетное количество цифр
    Основная функция возвращает True, если пароль валидный.
    Если пароль не валидный, возвращает лист стрингов, в которых перечислены
    причины неуспешной проверки. Например: ["содержит запрещенные символы"]
    """
    if not _validate_symbols(password):
        return False
    if not _validate_numbers_odd(password):
        return False
    if not _validate_letters_even(password):
        return False

    return True


def _validate_symbols(input_str: str) -> bool:
    """
    Проверяет строку на наличие запрещенных символов
    Подсказка: у строк есть метод, проверяющий наличие только був и цифр
    Возвращает True/False
    """
    if not input_str.isalnum():
        return False

    return True


def _validate_letters_even(input_str: str) -> bool:
    """
    Проверяет строку на четное количество букв.
    Возвращает True/False
    """
    output = "".join([i for i in input_str if i.isalpha()])
    if len(output) % 2:
        return False
    return True


def _validate_numbers_odd(input_str: str) -> bool:
    """
    Проверяет строку на нечетное количество цифр
    Возвращает True/False
    """
    output = "".join([i for i in input_str if i.isdigit()])
    if not len(output) % 2:
        return False
    return True


print(validate_password("Salman1123"))
