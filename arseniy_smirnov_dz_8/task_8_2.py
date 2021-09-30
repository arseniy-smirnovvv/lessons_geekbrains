import re
import requests


def get_nginx_logs(uri):
    response = requests.get(uri)
    return [logs for logs in response.text.split('\n')]


def re_match_log(lst, count=None):
    if count == None:
        count = len(lst)

    # Регулярные выражения
    re_addr = r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'
    re_datetime = r'\[([^\]]+)\]'
    re_type = '(POST|GET|PUT|OPTION|HEAD)'
    re_resourses = r' /([a-zA-Z0-9_.+-/]+)'
    re_code = r'\d{3}\s+'
    re_size = r'\d{3}\s+(\d+\s+)'
    parsed_raw = []

    for i in range(count):
        if i > len(lst): break
        log = lst[i]
        tmp_lst = []
        # Я обернул её в исключения, что бы если передавалось что-то другое или в что-нибудь что не логи,
        # то оно бы просто пропускалось и не обрбатывалось
        try:
            # Тут выбиваем ошибку, если это ivp6, я не смог написать для её поиска регулярку, поэтому сделал так
            try:
                tmp_lst.append(re.findall(re_addr, log)[0])
            except IndexError as e:
                # Один хрен мы знаем, что ip всегда первым идет
                tmp_lst.append(log.split(' ')[0])

            tmp_lst.extend([
                re.findall(re_datetime, log)[0],
                re.findall(re_type, log)[0],
                re.findall(re_resourses, log)[0],
                re.findall(re_code, log)[0].replace(' ', ''),
                re.findall(re_size, log)[0].replace(' ', '')
            ])
            parsed_raw.append(tuple(tmp_lst))
        except Exception as e:
            continue
    return parsed_raw


uri = 'https://raw.githubusercontent.com/elastic/examples/master/Common%20Data%20Formats/nginx_logs/nginx_logs'

template = r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'
for log_tuple in re_match_log(get_nginx_logs(uri), 100):
    print(log_tuple)
