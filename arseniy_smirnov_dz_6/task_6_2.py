def parse_log(log):
    log_word = log.split(' ')
    return tuple([log_word[0], log_word[5].replace('"', ''), log_word[6]])


def find_ip_spam(logs):
    dict_ip = {}
    for log in logs:
        ip = log[0]
        if ip in dict_ip:
            dict_ip[ip] += 1
        else:
            dict_ip[ip] = 0
    max_key = max(dict_ip, key=lambda key: dict_ip[key])
    return tuple([max_key, dict_ip[max_key]])


log_lst = []
with open('files/nginx_log.txt', 'r', encoding='utf-8') as f:
    log = f.readline().replace('\n', '')
    while log:
        log_lst.append(parse_log(log))
        log = f.readline().replace('\n', '')

print(find_ip_spam(log_lst))