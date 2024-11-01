import argparse


class StringSortingTool:
    def __init__(self, sort_type="natural"):
        self.sort_type = sort_type
        self.data = []
        self.max_item = ""
        self.counter = 0
        self.percentage = 0
        self.count_dict = dict()

    def add_data(self):
        while True:
            try:
                str_data = input()
                self.data.append(str_data)
            except EOFError:
                break

    def find_max_item(self):
        for item in self.data:
            if len(item) > len(self.max_item):
                self.max_item = item

    def count_max_occurrences(self):
        for item in self.data:
            if len(item) == len(self.max_item):
                self.counter += 1

    def calculate_percentage(self, counter):
        percentage = int(counter / len(self.data) * 100)
        return percentage

    def __str__(self):
        return (f"Total lines: {len(self.data)}.\n"
                f"The longest line:\n"
                f"{self.max_item}\n"
                f"({self.counter} time(s), {self.calculate_percentage(self.counter)}%).")

    def fill_count_dict(self):
        for item in self.data:
            if item in self.count_dict.keys():
                self.count_dict[item] += 1
            else:
                self.count_dict[item] = 1

    def sorting_result(self):
        self.sort_data()
        self.fill_count_dict()
        self.count_dict = dict(sorted(self.count_dict.items(), key=lambda x: x[1]))
        print(f"Total lines: {len(self.data)}.")
        match self.sort_type:
            case "natural":
                print(f"Sorted data:")
                for line in self.data:
                    print(line)
            case "byCount":
                for k in self.count_dict.keys():
                    v = self.count_dict[k]
                    print(f"{k}: {v} time(s), {self.calculate_percentage(v)}%")

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

    def fill_count_dict(self):
        for item in self.data:
            if item in self.count_dict.keys():
                self.count_dict[item] += 1
            else:
                self.count_dict[item] = 1

    def __str__(self):
        return (f"Total words: {len(self.data)}.\n"
                f"The longest word: {self.max_item} ({self.counter} time(s), "
                f"{self.calculate_percentage(self.counter)}%).")

    def sorting_result(self):
        self.sort_data()
        self.fill_count_dict()
        self.count_dict = dict(sorted(self.count_dict.items(), key=lambda x: x[1]))
        print(f"Total words: {len(self.data)}.")
        match self.sort_type:
            case "natural":
                print(f"Sorted data: {' '.join(self.data)}")
            case "byCount":
                for k in self.count_dict.keys():
                    v = self.count_dict[k]
                    print(f"{k}: {v} time(s), {self.calculate_percentage(v)}%")


class NumberSortingTool(WordSortingTool):
    def add_data(self):
        while True:
            try:
                str_data = input()
                self.data += [int(i) for i in str_data.split()]
            except EOFError:
                break

    def find_max_item(self):
        for item in self.data:
            if item > self.max_item:
                self.max_item = item

    def count_max_occurrences(self):
        for item in self.data:
            if item == self.max_item:
                self.counter += 1

    def __str__(self):
        return (f"Total numbers: {len(self.data)}.\n"
                f"The greatest number: {self.max_item} ({self.counter} time(s), "
                f"{self.calculate_percentage(self.counter)}%).")

    def sorting_result(self):
        self.sort_data()
        self.fill_count_dict()
        self.count_dict = dict(sorted(self.count_dict.items(), key=lambda x: x[1]))
        print(f"Total numbers: {len(self.data)}.")
        match self.sort_type:
            case "natural":
                print(f"Sorted data: {' '.join(map(str, self.data))}")
            case "byCount":
                for k in self.count_dict.keys():
                    v = self.count_dict[k]
                    print(f"{k}: {v} time(s), {self.calculate_percentage(v)}%")



if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="This program sorts input strings.")

    parser.add_argument("-dataType", default="word", choices=["word", "line", "long"])
    parser.add_argument("-sortingType", default="natural", choices=["natural", "byCount"])
    args = parser.parse_args()
    mark = args.dataType
    sorting_type = args.sortingType


    match mark:
        case "line":
            tool = StringSortingTool(sort_type=sorting_type)
        case "word":
            tool = WordSortingTool(sort_type=sorting_type)
        case "long":
            tool = NumberSortingTool(sort_type=sorting_type)

    tool.add_data()
    tool.sorting_result()






