def parse_log(log):
    log_word = log.split(' ')
    return tuple([log_word[0], log_word[5].replace('"', ''), log_word[6]])



log_lst = []
with open('files/nginx_log.txt', 'r', encoding='utf-8') as f:
    log = f.readline().replace('\n', '')
    while log:
        log_lst.append(parse_log(log))
        log = f.readline().replace('\n', '')

for i in range(10):
    print(log_lst[i])