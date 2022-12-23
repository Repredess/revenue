import datetime as dt


class Revenue:
    PULL = dict(Наличные_на_утро=0, Наличные_на_вечер=0, Безналичный_рассчет=0, Расход=0, Инкасация=0)

    # startapp
    def __init__(self):
        self.file = 'data.txt'
        self.head = self.read_head(self.file)
        self.date = str(dt.date.today())
        # self.line = ''

    # take data
    def take_data(self):
        data = [self.date]

        for key, value in self.PULL.items():
            print(key.replace("_", " ") + ":", end=" ")
            self.PULL[key] = input()
            data.append(self.PULL[key])

        return data

    # set data
    def set_data(self):

        with open(self.file, 'r+', encoding='utf-8') as f:
            count = 0
            data = self.take_data()

            for line in f.readlines():
                count += 1

            data.insert(0, str(count))
            print("  ".join(data), file=f)

        return data

    # get data
    def get_data(self):
        pass

    @classmethod
    def read_head(cls, file):
        with open(file, encoding='utf-8') as f:
            return f.readline().strip().split()

    @classmethod
    def __check_value(cls, x):
        return type(x) in (int, float)

    def get_head(self):
        return self.head


pt = Revenue()
print(pt.set_data())
