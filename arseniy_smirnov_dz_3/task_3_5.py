# НЕ ВЫПОЛНЕННО УСЛОВИЕ ДОКУМЕНТАЦИИ ФУНКЦИИ
import random


def unic_words(word, lst):
    if len(lst) == 0:
        return False
    for _, jokes in enumerate(lst):
        if word in jokes.split(' '):
            return True
    return False


def get_jokes(count_jokes, unic_word=False):
    nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
    adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
    adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
    max_jokes = len(list(zip(nouns, adverbs, adjectives)))
    result = []
    # Делаем проверку, что бы не было такого, что шутки будут генерироваться бексконечно,
    # потому все слова уже использовались
    if (count_jokes > max_jokes):
        return f'Превышенно максимально количество создаваемых анектодов! Макс. {max_jokes}'
    for _ in range(count_jokes):
        word_nouns = random.choice(nouns)
        word_adverbs = random.choice(adverbs)
        word_adjectives = random.choice(adjectives)
        if unic_word:
            while unic_words(word_nouns, result):
                word_nouns = random.choice(nouns)
            while unic_words(word_adverbs, result):
                word_adverbs = random.choice(adverbs)
            while unic_words(word_adjectives, result):
                word_adjectives = random.choice(adjectives)
        result.append(f'{word_nouns} {word_adverbs} {word_adjectives}')
    return result


print(get_jokes(6, True))
print(get_jokes(5, True))
print(get_jokes(5))
print(get_jokes(4, True))
print(get_jokes(2))
