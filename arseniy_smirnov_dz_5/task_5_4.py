import sys

# Список
src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
result = [src[idx] for idx, num in enumerate(src, 1) if len(src) > idx and src[idx] > src[idx - 1]]
print(result)
print(sys.getsizeof(result))

# Генератор
result = (src[idx] for idx, num in enumerate(src, 1) if len(src) > idx and src[idx] > src[idx - 1])
print(list(result))
print(sys.getsizeof(result))