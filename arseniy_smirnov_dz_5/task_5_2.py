def odd_nums(max):
    return (num for num in range(0, max + 1, 3))


gen_num = odd_nums(10)
print(*gen_num)


# OR

def odd_nums_other(max):
    return (num for num in range(0, max + 1, 3) if num % 3 == 0)


gen_num_other = odd_nums_other(10)
print(*gen_num_other)
