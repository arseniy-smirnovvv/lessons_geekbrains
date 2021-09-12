# Честно, я не понял что имелось ввиду под фразой "задокументровать код функции"
import random


def unic_words(word, lst):
    if len(lst) == 0:
        return False
    for _, jokes in enumerate(lst):
        if word in jokes.split(' '):
            return True
    return False


def get_jokes(count_jokes, unic_word=False):
    '''
    Возвращает список шуток со словами, которые находятся в теле функции
    При наличие флага unic_word, что означает уникальное слово, возвращает список шуток, с неповторящимеся словами в шутках
    '''
    nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
    adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
    adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
    words_jokes = [nouns] + [adverbs] + [adjectives]
    max_jokes = len(list(zip(nouns, adverbs, adjectives)))
    result = []
    if (count_jokes > max_jokes):
        return f'Превышенно максимально количество создаваемых анектодов! Макс. {max_jokes}'
    for _ in range(count_jokes):
        jokes = ''
        for word in words_jokes:
            random_word = random.choice(word)
            if unic_word:
                while unic_words(random_word, result):
                    random_word = random.choice(word)
            jokes += f'{random_word} '
        result.append(jokes[:-1])
    return result


print(get_jokes(6, True))
print(get_jokes(5, True))
print(get_jokes(5))
print(get_jokes(4, True))
print(get_jokes(2))
