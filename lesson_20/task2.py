# Write tests for the Phonebook application, which you have implemented in module 1.
# Design tests for this solution and write tests using unittest library

#ATTENTION!!!
# Тест кейс далеко не полняй
# Предусмотрел только :
# - добавление
# - обновление
# - удаление
# Если полноценно тестить, на все возможные кейсы, очень долго


import unittest
import lesson_11.task_2 as t

# test case list
p_dict = dict(first_name='', last_name='', full_name='', phone_numbers='', state='', city='')
my_phonebook_empty = {'persons': [p_dict]}
add_case = dict(first_name='Sam', last_name='Johns', full_name='Sam Johns', phone_numbers='+38151515'
                , state='City', city='City')
update_case = dict(first_name='Sam2', last_name='Johns2', full_name='Sam2 Johns2', phone_numbers='+38151515'
                , state='City', city='City')
test_values = [['Sam','Johns','+38151515','City','City'], ['Sam2','Johns2','+38151515','City','City']]



class TestPhoneBookAdding(unittest.TestCase):

    def test_add_record(self):
        """testing adding records"""
        print("-----test to add record-----")
        print(f"Test waiting to type:\n{test_values[0][0]}\n"
              f"{test_values[0][1]}\n{test_values[0][2]}\n{test_values[0][3]}\n{test_values[0][4]}\n")
        my_phonebook = my_phonebook_empty.copy()
        t.add_new(my_phonebook)
        copy_my_phonebook = my_phonebook_empty.copy()
        copy_my_phonebook['persons'].append(add_case)
        self.assertEqual(my_phonebook, copy_my_phonebook)
        del copy_my_phonebook
        del my_phonebook

class TestPhoneBookUpdating(unittest.TestCase):

    def test_update_record(self):
        """testing updating records"""
        print("-----test to update record-----")
        print(f"Test waiting to type {test_values[1][2]} at start.\nThen you have to type:\n{test_values[1][0]}\n"
              f"{test_values[1][1]}\n{test_values[1][2]}\n{test_values[1][3]}\n{test_values[1][4]}\n")
        my_phonebook = my_phonebook_empty.copy()
        my_phonebook['persons'].append(add_case)
        t.update_by(my_phonebook, 'phone_numbers')
        copy_my_phonebook = my_phonebook_empty.copy()
        copy_my_phonebook['persons'].append(update_case)
        self.assertEqual(my_phonebook, copy_my_phonebook)


class TestPhoneBookDeliting(unittest.TestCase):

    def test_del_record(self):
        """testing deliting records"""
        print("-----test to delete record-----")
        print("test waiting to type 'Sam2'")
        my_phonebook = my_phonebook_empty.copy()
        my_phonebook['persons'].append(add_case)
        t.delete_by(my_phonebook, 'first_name')
        copy_my_phonebook = my_phonebook_empty.copy()
        self.assertEqual(my_phonebook, copy_my_phonebook)

if __name__ == "__main__":
    unittest.main()