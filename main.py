pull = dict(Наличные_на_утро=0, Наличные_на_вечер=0, Безналичный_рассчет=0, Расход=0, Инкасация=0)


def revenue(pull):
    for key, value in pull.items():
        print(key.replace("_", " ") + ":", end=" ")
        pull[key] += int(input())

    rev_total = pull["Наличные_на_вечер"] + pull["Безналичный_рассчет"] + pull["Расход"] + pull["Инкасация"] - pull["Наличные_на_утро"]

    return print("Выручка: " + str(rev_total))


revenue(pull)

