# The “sys.path” list is initialized
# from the PYTHONPATH environment variable.Is it possible to change it from within Python?
# If so, does it affect where Python looks for module files?
# Run some interactive tests to find it out.

import collections
import sys
print('Cписок строк, которые указывают путь поиска для модулей')
sys_path_test = sys.path.copy()
for item in sys_path_test:
    print(item)
#Теперь начинаем эксперименты
# 1. удаляем путь
sys.path.remove('C:\Program Files\JetBrains\PyCharm 2022.2.3\plugins\python\helpers\pycharm_matplotlib_backend')
#Проверяем
if collections.Counter(sys_path_test) == collections.Counter(sys.path):
    print('Списки одинаковы')
else:
    print('Списки разные')
    for item in sys.path:
        print(item)

# 2. Добавляем путь. Добавляем путь к левой папке на диске D, где хранится модкль с тестовой функцией.
# Этот модуль в папке урока 5, test_import.py . для моделирования
sys.path.append('D:\TestPython')
for item in sys.path:
    print(item)
# 3. Пытаемся подключить модуль из добавленного пути
import test_import as ti
ti.my_test_import()
#Everithing is working!!!