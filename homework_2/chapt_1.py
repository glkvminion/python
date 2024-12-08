def read_and_validate_file(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as data_file:
            for content in data_file:
                content = content.strip()
                try:
                    elements = content.split()
                    if all(element.replace('.', '', 1).isdigit() for element in elements):
                        print(content)
                    else:
                        raise TypeError("Найдена строка с нечисловым значением")
                except TypeError as error:
                    print(error)
    except FileNotFoundError:
        print("Ошибка: указанный файл отсутствует")

read_and_validate_file('info.txt')
