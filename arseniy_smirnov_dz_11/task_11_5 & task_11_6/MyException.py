class EquipmentError(Exception):
    def __init__(self, txt):
        self.txt = txt


class WarehouseError(Exception):
    def __init__(self, txt):
        self.txt = txt
