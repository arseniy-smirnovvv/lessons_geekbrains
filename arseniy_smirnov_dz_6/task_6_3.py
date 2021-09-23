import sys
import json

with open('files/users.csv', 'r', encoding='utf-8') as f:
    names = [name for name in f.read().split('\n')]

with open('files/hobby.csv', 'r', encoding='utf-8') as f:
    hobbie = [hobbie for hobbie in f.read().split('\n')]

if len(names) < len(hobbie):
    sys.exit('1')

result_dict = {name: hobbie[i] if len(hobbie) > i else None for i, name in enumerate(names)}
with open('files/date_task_1.json', 'w', encoding='utf-8') as f:
    json.dump(result_dict, f)

with open('files/date_task_1.json', 'r', encoding='utf-8') as f:
    print(json.load(f))
