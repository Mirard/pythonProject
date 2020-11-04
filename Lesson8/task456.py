# task 4
class OfficeEquipment:
    model: str
    price: float
    in_warehouse: bool
    division_name: str

    def __init__(self, model, price, in_warehouse, division_name):
        self.model = model
        self.price = price
        self.in_warehouse = in_warehouse
        self.division_name = division_name

    # task 5
    def to_warehouse(self):
        self.division_name = ""
        self.in_warehouse = True

    # task 5
    def to_division(self, division: str):
        self.in_warehouse = False
        self.division_name = division


# task 4
class Printer(OfficeEquipment):
    is_color: bool
    two_sided: bool

    def __init__(self, model, price, in_warehouse=True, division_name="", is_color=False, two_sided=False):
        super().__init__(model, price, in_warehouse, division_name)
        self.is_color = is_color
        self.two_sided = two_sided

    def print_info(self):
        print(f"\nModel: {self.model}; Price: {self.price}; Is in Warehouse: {self.in_warehouse}; "
              f"Is in Division: {self.division_name}; Is two-sided: {self.two_sided}; "
              f"Is colored: {self.is_color}")


# task 4
class Xerox(OfficeEquipment):
    is_color: bool
    return_to_email: bool

    def __init__(self, model, price, in_warehouse=True, division_name="", is_color=False, return_to_email=False):
        super().__init__(model, price, in_warehouse, division_name)
        self.is_color = is_color
        self.return_to_email = return_to_email

    def print_info(self):
        print(f"\nModel: {self.model}; Price: {self.price}; Is in Warehouse: {self.in_warehouse}; "
              f"Is in Division: {self.division_name}; Is colored: {self.is_color}; "
              f"Can be sent to email: {self.return_to_email}")


# task 4
class Scanner(OfficeEquipment):
    two_sided: bool
    no_list_protection: bool

    def __init__(self, model, price, in_warehouse=True, division_name="", two_sided=False, no_list_protection=False):
        super().__init__(model, price, in_warehouse, division_name)
        self.two_sided = two_sided
        self.no_list_protection = no_list_protection

    def print_info(self):
        print(f"\nModel: {self.model}; Price: {self.price}; Is in Warehouse: {self.in_warehouse}; "
              f"Is in Division: {self.division_name}; Is two-sided: {self.two_sided}; "
              f"Is list protection: {self.no_list_protection}")


# task 4
class OfficeEquipmentWarehouse:
    printer_max_count: int
    xerox_max_count: int
    scanner_max_count: int
    printer_equipments: list = []
    xerox_equipments: list = []
    scanner_equipments: list = []

    def __init__(self, printer_max_count=0, xerox_max_count=0, scanner_max_count=0):
        self.printer_max_count = printer_max_count
        self.xerox_max_count = xerox_max_count
        self.scanner_max_count = scanner_max_count

    def store(self, printer_equipments: list, xerox_equipments: list, scanner_equipments: list):
        self.printer_equipments.extend(printer_equipments)
        self.xerox_equipments.extend(xerox_equipments)
        self.scanner_equipments.extend(scanner_equipments)

    # task 5
    @staticmethod
    def equipment_count(equipment: list):
        if len(equipment) != 0:
            in_warehouse_count = 0
            el_type = type(equipment[0])
            division_list = []
            for el in equipment:
                if el.in_warehouse:
                    in_warehouse_count += 1
                else:
                    division_list.append(el.division_name)
            unique_division_list = []
            for division in division_list:
                if unique_division_list.count(division) == 0:
                    unique_division_list.append(division)
            division_statistic = []
            for division in unique_division_list:
                division_statistic.append((division, division_list.count(division)))
            result_dict = {"Equipment_type": el_type, "In_Warehouse": in_warehouse_count,
                           "In_Division": {len(equipment) - in_warehouse_count}, "Per_Division": division_statistic}
            return result_dict
        else:
            return "\nList of equipment is empty"
