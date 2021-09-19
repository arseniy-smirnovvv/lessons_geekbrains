def odd_nums(max):
    for num in range(0, max + 1, 3):
        yield num


gen_num = odd_nums(15)
print(*gen_num)
