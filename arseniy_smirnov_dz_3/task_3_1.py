def num_translate(num_str):
    english_dict = {
        'one': 'один',
        'two': 'два',
        'there': 'три',
        'four': 'четыре',
        'five': 'пять',
        'six': 'шесть',
        'seven': 'семь',
        'eight': 'восемь',
        'nine': 'девять',
        'ten': 'десять'
    }

    return english_dict.get(num_str)


print(num_translate('one'))
print(num_translate('two'))
print(num_translate('there'))
print(num_translate('eight'))
print(num_translate('eleven'))