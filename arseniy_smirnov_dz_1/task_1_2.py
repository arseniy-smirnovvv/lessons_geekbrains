# создаём список состоящий из кубов нечётных чисел от 1 до 1000
gen_num = []
# можно было использовать генераторы, но мы до них ещё не дошли
for num in range(1, 1001):
    if num % 2 != 0:
        gen_num.append(num ** 3)

resut_num = []
for date in gen_num:
    total = 0
    num = date
    while num > 0:
        dig_num = num % 10
        total += dig_num
        num = num // 10
    if total % 7 == 0:
        resut_num.append(date)
print(sum(resut_num))

# задача b, к каждому элементу добавляем 17
# обнуляем старый список
resut_num = []
for date in gen_num:
    total = 0
    num = date
    while num > 0:
        dig_num = num % 10
        total += dig_num
        num = num // 10
    if total % 7 == 0:
        resut_num.append(date)
print(sum(resut_num))