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

    if num_str[0].isupper():
        return english_dict.get(num_str.lower()).capitalize()
    else:
        return english_dict.get(num_str.lower())


print(num_translate('One'))
print(num_translate('one'))
print(num_translate('Nine'))
print(num_translate('eleven'))
