import argparse
import sys


class StringSortingTool:
    def __init__(self, sort_type="natural"):
        self.sort_type = sort_type
        self.data = []
        self.max_item = ""
        self.counter = 0
        self.percentage = 0
        self.count_dict = dict()
        self.result_string = ""

    def read_file(self, file_name):
        with open(file_name, "r") as file:
            self.data = file.readlines()

    def write_to_file(self, file_name):
        with open(file_name, "w") as file:
            file.write(self.result_string)

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

    def make_result(self):
        self.sort_data()
        self.fill_count_dict()
        self.count_dict = dict(sorted(self.count_dict.items(), key=lambda x: x[1]))
        self.result_string += f"Total lines: {len(self.data)}.\n"
        match self.sort_type:
            case "natural":
                self.result_string += f"Sorted data:\n"
                for line in self.data:
                    self.result_string += (line + "\n")
            case "byCount":
                for k in self.count_dict.keys():
                    v = self.count_dict[k]
                    self.result_string += f"{k}: {v} time(s), {self.calculate_percentage(v)}%\n"

    def printing_result(self):
        print(self.result_string)

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
    def from_string_to_word(self):
        word_list = []
        for line in self.data:
            word_list += line.split()
        self.data = word_list

    def fill_count_dict(self):
        for item in self.data:
            if item in self.count_dict.keys():
                self.count_dict[item] += 1
            else:
                self.count_dict[item] = 1

    def __str__(self):
        self.from_string_to_word()
        self.find_max_item()
        self.count_max_occurrences()
        return (f"Total words: {len(self.data)}.\n"
                f"The longest word: {self.max_item} ({self.counter} time(s), "
                f"{self.calculate_percentage(self.counter)}%).")

    def make_result(self):
        self.from_string_to_word()
        self.sort_data()
        self.fill_count_dict()
        self.count_dict = dict(sorted(self.count_dict.items(), key=lambda x: x[1]))
        self.result_string += f"Total words: {len(self.data)}.\n"
        match self.sort_type:
            case "natural":
                self.result_string += f"Sorted data: {' '.join(self.data)}\n"
            case "byCount":
                for k in self.count_dict.keys():
                    v = self.count_dict[k]
                    self.result_string += f"{k}: {v} time(s), {self.calculate_percentage(v)}%\n"


class NumberSortingTool(WordSortingTool):
    def from_str_to_int(self):
        int_list = []
        for char in self.data:
            try:
                num = int(char)
                int_list.append(num)
            except ValueError:
                print(f"{char} is not a long. It will be skipped.")
                continue
        self.data = int_list

    def find_max_item(self):
        for item in self.data:
            if item > self.max_item:
                self.max_item = item

    def count_max_occurrences(self):
        for item in self.data:
            if item == self.max_item:
                self.counter += 1

    def __str__(self):
        self.from_str_to_int()
        self.find_max_item()
        self.count_max_occurrences()
        return (f"Total numbers: {len(self.data)}.\n"
                f"The greatest number: {self.max_item} ({self.counter} time(s), "
                f"{self.calculate_percentage(self.counter)}%).")

    def make_result(self):
        self.from_string_to_word()
        self.from_str_to_int()
        self.sort_data()
        self.fill_count_dict()
        self.count_dict = dict(sorted(self.count_dict.items(), key=lambda x: x[1]))
        self.result_string += f"Total numbers: {len(self.data)}.\n"
        match self.sort_type:
            case "natural":
                self.result_string += f"Sorted data: {' '.join(map(str, self.data))}\n"
            case "byCount":
                for k in self.count_dict.keys():
                    v = self.count_dict[k]
                    self.result_string += f"{k}: {v} time(s), {self.calculate_percentage(v)}%\n"



if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="This program sorts input strings.")

    parser.add_argument("-dataType", nargs="?", default="word", choices=["word", "line", "long"])
    parser.add_argument("-sortingType", nargs="?", default="natural", choices=["natural", "byCount"])
    parser.add_argument("-inputFile", nargs="?")
    parser.add_argument("-outputFile", nargs="?")
    args, unknown = parser.parse_known_args()
    data_type = args.dataType
    sorting_type = args.sortingType
    input_file = args.inputFile
    output_file = args.outputFile

    if len(unknown) > 0:
        for arg in unknown:
            print(f'"{arg}" is not a valid parameter. It will be skipped.')

    if sorting_type is None:
        print('No sorting type defined!')
        sys.exit()
    if data_type is None:
        print('No data type defined!')
        sys.exit()


    match data_type:
        case "line":
            tool = StringSortingTool(sort_type=sorting_type)
        case "word":
            tool = WordSortingTool(sort_type=sorting_type)
        case "long":
            tool = NumberSortingTool(sort_type=sorting_type)

    if (input_file is not None) and (output_file is None):
        tool.read_file(input_file)
        tool.make_result()
        tool.printing_result()
    elif (input_file is not None) and (output_file is not None):
        tool.read_file(input_file)
        tool.make_result()
        tool.write_to_file(output_file)
    else:
        tool.add_data()
        tool.make_result()
        tool.printing_result()






