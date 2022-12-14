import unittest
import lesson_16.task_2 as t


class MathTestCase(unittest.TestCase):

    def setUp(self):
        self.my_class = t.Mathematician()

    def test_square_nums(self):
        l1 = [7, 11, 5, 4]
        l2 = [49, 121, 25, 16]
        self.assertEqual(self.my_class.square_nums(l1), l2)

    def test_remove_positives(self):
        l1 = [26, -11, -8, 13, -90]
        l2 = [-11, -8, -90]
        self.assertEqual(self.my_class.remove_positives(l1), l2)

    def test_filter_leaps(self):
        l1 = [2001, 1884, 1995, 2003, 2020]
        l2 = [1884, 2020]
        self.assertEqual(self.my_class.filter_leaps(l1), l2)

if __name__ == "__main__":
    unittest.main()
