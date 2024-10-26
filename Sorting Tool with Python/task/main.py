import argparse


class StringSortingTool:
    def __init__(self):
        self.data = []
        self.max_item = ""
        self.counter = 0
        self.percentage = 0

    def add_data(self):
        while True:
            try:
                str_data = input()
                self.data.append(str_data)
            except EOFError:
                break

    def max(self):
        for item in self.data:
            if len(item) > len(self.max_item):
                self.max_item = item

    def counting_max(self):
        for item in self.data:
            if len(item) == len(self.max_item):
                self.counter += 1

    def percentage_counter(self):
        self.percentage = int(self.counter / len(self.data) * 100)

    def __str__(self):
        return (f"Total lines: {len(self.data)}.\n"
                f"The longest line:\n"
                f"{self.max_item}\n"
                f"({self.counter} time(s), {self.percentage}%).")


class WordSortingTool(StringSortingTool):
    def add_data(self):
        while True:
            try:
                str_data = input()
                self.data += str_data.split()
            except EOFError:
                break

    def __str__(self):
        return (f"Total words: {len(self.data)}.\n"
                f"The longest word: {self.max_item} ({self.counter} time(s), {self.percentage}%).")


class NumberSortingTool(StringSortingTool):
    def __init__(self):
        super().__init__()
        self.data = []
        self.max_item = 0
        self.counter = 0
        self.percentage = 0

    def add_data(self):
        while True:
            try:
                str_data = input()
                self.data += [int(i) for i in str_data.split()]
            except EOFError:
                break

    def max(self):
        for item in self.data:
            if item > self.max_item:
                self.max_item = item

    def counting_max(self):
        for item in self.data:
            if item == self.max_item:
                self.counter += 1

    def __str__(self):
        return (f"Total numbers: {len(self.data)}.\n"
                f"The greatest number: {self.max_item} ({self.counter} time(s), {self.percentage}%).")


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="This program sorts input strings.")

    parser.add_argument("-dataType", default="word", choices=["word", "line", "long"])
    args = parser.parse_args()
    mark = args.dataType
    
    match mark:
        case "line":
            a = StringSortingTool()
            a.add_data()
            a.max()
            a.counting_max()
            a.percentage_counter()
            print(str(a))
        case "word":
            b = WordSortingTool()
            b.add_data()
            b.max()
            b.counting_max()
            b.percentage_counter()
            print(str(b))
        case "long":
            c = NumberSortingTool()
            c.add_data()
            c.max()
            c.counting_max()
            c.percentage_counter()
            print(str(c))







