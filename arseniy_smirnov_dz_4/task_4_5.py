# Я точно не знаю, подключать ли модули и пакеты после проверки name, но я думаю что после проверки все-таки лучше)


if __name__ == '__main__':
    import sys
    import utils

    if len(sys.argv) < 2:
        print('Вы не передали буквенный код валюты!')
        exit()
    char_code = sys.argv[1]
    print(utils.currency_rates(char_code))
