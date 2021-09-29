from re import findall
# Можно было сделать компиляцию  регулярных выражений для усорения, но это я делать не стал.


def email_parse(email):
    template = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*$'
    if not findall(template, email):
        raise ValueError(f'Неправильный формат: {email}')

    template = r'(^[a-zA-Z0-9_.+-]+)@([a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*$)'
    result = findall(template, email)
    return {'username': result[0][0], 'domain': result[0][1]}


email = 'arseniy.smirnovvv@gmail.com'
try:
    print(email_parse(email))
except ValueError as e:
    print(e)

email = 'test'
try:
    print(email_parse(email))
except ValueError as e:
    print(e)