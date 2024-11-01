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

    def sorting_result(self):
        self.sort_data()
        print(f"Total lines: {len(self.data)}.\n"
              f"Sorted data: {' '.join(self.data)}")

    def sort_data(self):
        self.data = self._merge_sort(self.data)

    def _merge_sort(self, arr):
        if len(arr) <= 1:
            return arr

        # Split the array into two halves
        middle = len(arr) // 2
        left_half = self._merge_sort(arr[:middle])
        right_half = self._merge_sort(arr[middle:])

        # Merge the two halves
        return self._merge_arr(left_half, right_half)

    @staticmethod
    def _merge_arr(left, right):
        result = []
        i = j = 0

        # Merge two sorted lists
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1

        # Add any remaining elements
        result.extend(left[i:])
        result.extend(right[j:])
        return result


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

    def sorting_result(self):
        self.sort_data()
        print(f"Total numbers: {len(self.data)}.\n"
              f"Sorted data: {' '.join(map(str, self.data))}")



if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="This program sorts input strings.")

    parser.add_argument("-dataType", default="word", choices=["word", "line", "long"])
    parser.add_argument("-sortIntegers", action="store_true")
    args = parser.parse_args()
    mark = args.dataType
    sort_int = args.sortIntegers

    if sort_int:
        d = NumberSortingTool()
        d.add_data()
        d.sorting_result()
    else:
        match mark:
            case "line":
                tool = StringSortingTool()
            case "word":
                tool = WordSortingTool()
            case "long":
                tool = NumberSortingTool()

        tool.add_data()
        tool.max()
        tool.counting_max()
        tool.percentage_counter()
        print(str(tool))






