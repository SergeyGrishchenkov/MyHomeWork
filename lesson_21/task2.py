# Take your implementation of the context manager class from Task 1
# and write tests for it. Try to cover as many use cases as you can,
# positive ones when a file exists and everything works as designed.
# And also, write tests when your class raises errors or you have errors in the runtime context suite.
import _io
import unittest
import task1 as t
import random

# test case
file_name = "test1.txt"
file_name_sample = "test2.txt"
type_act = ['r', 'w', 'a']
with open('test2.txt', 'w') as f:
    for i in range(3):
        f.write("hello world\n")


# делаем следующие тест кейсы на ощибки
# 1. Ошибка при открытии файла на чтение FileNotFoundError
# -----------------
# делаем следующие тест кейсы на проверку функционала
# 1. корретность закрытия файла
# 2. Файл открыт на чтение
# 3. Чтение строки файла
# 4. корректность записи файла
# 5. корректность добавления записи в файл


class TestTask1Err(unittest.TestCase):

    def test_open_r(self):
        with t.ContextTextFile('filetest' + str(random.randint(1, 199)) + '.txt', type_act[0]) as f:
            with self.assertRaises(FileNotFoundError):
                self.my_test.readable()


class TestTask1Actions(unittest.TestCase):

    def test_close(self):
        with t.ContextTextFile(file_name, type_act[0]) as f:
            print('Opened')
        self.assertTrue(f.closed)

    def test_open_r(self):
        with t.ContextTextFile(file_name, type_act[0]) as f:
            self.assertTrue(f.readable())

    def test_read_line(self):
        with t.ContextTextFile(file_name, type_act[0]) as f:
            test_str = f.readline()
        self.assertEqual('hello world\n', test_str)

    def test_write(self):
        with t.ContextTextFile(file_name, type_act[1]) as f:
            test_str = "hello world\n"
            f.writelines(test_str)
            f.writelines(test_str)
            f.writelines(test_str)
        with open(file_name) as f1:
            f1_read = f1.readlines()
        with open(file_name_sample) as f2:
            f2_read = f2.readlines()
        self.assertEqual(f1_read, f2_read)

class TestTask1Add(unittest.TestCase):
    def test_add(self):
        with t.ContextTextFile(file_name, 'a') as f_add:
            test_str = "hello world\n"
            f_add.write(test_str)
        with open(file_name) as f1:
            f1_read = f1.readlines()
        with open(file_name_sample, 'a') as f2:
            f2.write(test_str)
        with open(file_name_sample) as f2:
            f2_read = f2.readlines()
        self.assertEqual(f1_read, f2_read)


if __name__ == "__main__":
    unittest.main()
