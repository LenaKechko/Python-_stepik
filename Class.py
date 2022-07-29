class Buffer:
    def __init__(self):
        self.buffer = []

    def add(self, *a):
        tmp = list(a)
        while len(tmp) != 0:
            self.buffer.append(tmp.pop(0))
            if len(self.buffer) >= 5:
                sum = 0
                while len(self.buffer) != 0:
                    sum += self.buffer.pop(0)
                print(sum)

    def get_current_part(self):
        return self.buffer

buf = Buffer()
buf.add(1, 2, 3)
print(buf.get_current_part()) # вернуть [1, 2, 3]
buf.add(4, 5, 6) # print(15) – вывод суммы первой пятерки элементов
print(buf.get_current_part()) # вернуть [6]
buf.add(7, 8, 9, 10) # print(40) – вывод суммы второй пятерки элементов
print(buf.get_current_part()) # вернуть []
buf.add(1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1) # print(5), print(5) – вывод сумм третьей и четвертой пятерки
print(buf.get_current_part()) # вернуть [1]