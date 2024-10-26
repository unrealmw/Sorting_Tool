class SortingTool:
    def __init__(self):
        self.nums = []
        self.max_num = 0
        self.counter = 0

    def add_to_nums(self):
        while True:
            try:
                data = input()
                self.nums += [int(i) for i in data.split()]
            except EOFError:
                break

    def max_num_search(self):
        for i in self.nums:
            if i > self.max_num:
                self.max_num = i

    def counting_max_num(self):
        for i in self.nums:
            if i == self.max_num:
                self.counter += 1

    def __str__(self):
        return (f"Total numbers: {len(self.nums)}.\n"
                f"The greatest number: {self.max_num} ({self.counter} time(s)).")


if __name__ == '__main__':
    s = SortingTool()
    s.add_to_nums()
    s.max_num_search()
    s.counting_max_num()
    print(str(s))



