class Computer:
    def __init__(self, cpu, memory):
        self.__cpu = cpu
        self.__memory = memory

    def set_cpu(self, cpu):
        self.__cpu = cpu

    def get_cpu(self):
        return self.__cpu

    def set_memory(self, memory):
        self.__memory = memory

    def get_memory(self):
        return self.__memory

    def make_computations(self):
        result = self.__cpu + self.__memory
        return result

    def __str__(self):
        return f'Компьютер с процессором {self.__cpu}, памятью {self.__memory} GB'

    def __eq__(self, other):
        return self.__memory == other.__memory

    def __ne__(self, other):
        return self.__memory != other.__memory

    def __lt__(self, other):
        return self.__memory < other.__memory

    def __le__(self, other):
        return self.__memory <= other.__memory

    def __gt__(self, other):
        return self.__memory > other.__memory

    def __ge__(self, other):
        return self.__memory >= other.__memory

class Phone:
    def __init__(self, sim_cards_list):
        self.__sim_cards_list = sim_cards_list

    def set_sim_cards_list(self, sim_cards_list):
        self.__sim_cards_list = sim_cards_list

    def get_sim_cards_list(self):
        return self.__sim_cards_list


    def call(self, sim_card_number, call_to_number):
        if len(call_to_number) == 13:
            print(f'Идет звонок на номер {call_to_number} с сим-карты {sim_card_number + 1} ')

    def __str__(self):
        return f'доступны следующие сим-карты {self.get_sim_cards_list()}'

class Smartphone(Computer, Phone):
    def __init__(self, cpu, memory, sim_cards_list):
        Computer.__init__(self, cpu, memory)
        Phone.__init__(self, sim_cards_list)

    def use_gps(self, location):
        print(f'Идет построение маршрута до {location}')

    def __str__(self):
        return (f'Смартфон с процессором {self.get_cpu()}, памятью {self.get_memory()} GB '
                f'и сим-картами {self.get_sim_cards_list()}')

comp = Computer(7,512)
tel = Phone(['O!', 'Beeline', 'Megacom'])
smart1 = Smartphone(5, 128, ['O!', 'Megacom'])
smart2 = Smartphone(4, 64, ['Beeline', 'Megacom'])

print(comp.__str__())
print(tel.__str__())
print(smart1.__str__())
print(smart2.__str__())

print(comp.make_computations())

print(comp > smart1)
print(smart2 == smart1)
print(smart1 != comp)

print(smart1.call(1, '+996508991108'))
smart2.use_gps('Issyk-Kul')







