import unittest
import random
from insert_sort import insertion_sort


class InsertionSortTest(unittest.TestCase):
    def test_full_range(self):
        data = [1000, 999, 1001, 995, 990]
        insertion_sort(data)
        message = "True"
        for i in data:
            self.assertLess(i, i + 1, message)

    def test_lowest_range(self):
        data = [-1000, -999, -1002, -993, -997]
        insertion_sort(data)
        message = "True"
        for i in data:
            self.assertLess(i, i + 1, message)

    def test_middle_range(self):
        data = [-3, 0, 5, -15, 105]
        insertion_sort(data)
        message = "True"
        for i in data:
            self.assertLess(i, i + 1, message)

    def test_random_value(self):
        data = [random.randint(-1000, 1000) for i in range(5)]
        tmp = insertion_sort(data)
        message = "True"
        for i in tmp:
            print(i)
            self.assertLess(i, i + 1, message)



