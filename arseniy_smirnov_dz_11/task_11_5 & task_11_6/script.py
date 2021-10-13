from OfficeWarehouse import OfficeWarehouse
from OfficeEquipment import Printer, Xerox, Scaner

if __name__ == '__main__':
    try:

        pr_1 = Printer(1, 'EPSON', 213, 'красныый')
        pr_2 = Printer(1, 'HP', 512, ['черный', 'желтый'])
        xrx = Xerox(0, 'HP', 214, 'многострочный')
        warehouse_1 = OfficeWarehouse(1, 'Арсений')
        warehouse_1.add_equipment([pr_1, pr_2, xrx])
        warehouse_2 = OfficeWarehouse(2, 'Дмитрий')

        print(f'Кол-во оргтехники на первом складе: {warehouse_1.get_count_equipment()}')
        print('Переносим все на второй склад')
        warehouse_1.broadcast_equipment(warehouse_2)
        print(f'Кол-во оргтехники на первом складе: {warehouse_1.get_count_equipment()}')
        print(f'Кол-во оргтехники на первом складе: {warehouse_2.get_count_equipment()}')
        print()
        print(warehouse_2)
    except Exception as e:
        print(e)