# Implement 2 classes, the first one is the Boss and the second one is the Worker.
# Worker has a property 'boss', and its value must be an instance of Boss.
# You can reassign this value, but you should check whether the new value is Boss.
#--------------------------------------------
# Each Boss has a list of his own workers. You should implement a method that allows you to add workers to a Boss.
# You're not allowed to add instances of Boss class to workers list directly via access to attribute,
# use getters and setters instead!

class Boss:

    def __init__(self, id_: int, name: str, company: str):
        self.id = id_

        self.name = name

        self.company = company

        self.workers = []

    @property
    def boss_info(self):
        return {self.name: [self.id, self.company]}

    @property
    def my_workers(self):

        return self.workers

    @my_workers.setter
    def my_workers(self, new_worker):
        if isinstance(new_worker, Worker):
            self.workers.append(new_worker)
        else:
            raise TypeError

    @my_workers.deleter
    def my_workers(self, old_worker):
        if isinstance(old_worker, Worker):
            pass
            #Здесь ничего не пишем, поскольку нет такой задачи
            #Если бы надо было, алгоритм:
            # 1. в классе Worker переопределяем метод __eq__(self, other)
            # 2. В списке объекта класса Boss ищем такой isinstance
            # 3. Удаляем
        else:
            raise TypeError


class Worker:

    def __init__(self, id_: int, name: str, company: str, boss: Boss):
        self.id = id_

        self.name = name

        self.company = company

        self.boss = boss

    @property
    def my_boss(self):
        return self.boss

    @my_boss.setter
    def my_boss(self, new_boss):
        if isinstance(new_boss, Boss):
            self.boss = new_boss
        else:
            raise TypeError

    @my_boss.deleter
    def my_boss(self):
        del self.boss


def main():
    boss_1 = Boss(1, 'John Gudman', 'Intel')
    boss_2 = Boss(1, 'Vika Dvornik', 'Beetroot')

    w1 = Worker(31, 'Roman', 'Beetroot', boss_2)
    #adding worker to a Boss
    boss_2.my_workers = w1
    w2 = Worker(32, 'Igor', 'Beetroot', boss_2)
    #adding worker to a Boss
    boss_2.my_workers = w2
    print('*' * 20)

    print({item.id: item.name for item in boss_2.my_workers})

    print('*'*20)
    print(f'The worker {w1.name}  has boss: {w1.my_boss.boss_info}')
    #reassigning boss value
    w1.my_boss = boss_1
    print(f'The worker {w1.name}  has boss: {w1.my_boss.boss_info}')



if __name__ == '__main__':
    main()

#ВАЖНО:
# По уму надо было сделать перекрестные методы в классах
# 1. при замене босса у работника, автоматов в инстансе босса обновлять работника в списке
# 2. при добавлении  работника в инстансе босса, автоматом обновлять босса в экземпляре работника