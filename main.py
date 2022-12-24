import datetime as dt


class Revenue:
    PULL = dict(Наличные_на_утро=0, Наличные_на_вечер=0, Безналичный_рассчет=0, Расход=0, Инкасация=0)

    # startapp
    def __init__(self):
        self.file = 'data.txt'
        self.rev = 'rev.txt'
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
            count = len(f.readlines())
            if count < 2:
                self.fix_line(f)
            data = self.take_data()

            data.insert(0, str(count))
            print("  ".join(data), file=f)

        return data, count

    def get_revenue(self):
        box, id_line = self.set_data()
        evening_cash = self.get_morning_cash(self.file)
        sum_r = 0
        for i in box[3:]:
            sum_r += int(i)

        revenue = sum_r - evening_cash

        with open(self.rev, 'a+', encoding='utf-8') as f:
            if id_line < 2:
                self.fix_line(f)
            print('  '.join([str(id_line), self.date, str(revenue)]), file=f)

        return revenue

    # get data
    def get_data(self):
        pass

    @classmethod
    def fix_line(cls, file):

        return print('', file=file)

    @classmethod
    def get_morning_cash(cls, file):
        with open(file) as f:
            get_ec = f.readlines()
            get_ec = get_ec[-1].strip().split()


        return int(get_ec[-5])

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
# print(pt.set_data())
print(pt.get_revenue())
