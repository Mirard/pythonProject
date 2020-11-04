import Lesson8.task456 as t

my_Scan1 = t.Scanner("Scan1", 0.1, True, "", False, True)
my_Scan2 = t.Scanner("Scan2", 1.2, False, "Division1", True, True)
my_Scan3 = t.Scanner("Scan1", 2.1, True, "", False, True)
my_Xerox1 = t.Xerox("Xerox1", 1.1, False, "Division2", False, True)
my_Xerox2 = t.Xerox("Xerox2", 1.2, False, "Division1", True, False)
my_Xerox3 = t.Xerox("Xerox3", 5.1, True, "", False, True)
my_Xerox4 = t.Xerox("Xerox4", 2.2, False, "Division1", True, False)
my_Print1 = t.Printer("Print1", 1.1, False, "Division1", False, True)
my_Print2 = t.Printer("Print2", 2.2, False, "Division2", True, False)
my_Print3 = t.Printer("Print3", 5.1, False, "Division3", False, True)
my_Print4 = t.Printer("Print4", 0.1, True, "", False, True)

my_scan_list = [my_Scan1, my_Scan2, my_Scan3]
my_print_list = [my_Print1, my_Print2, my_Print3, my_Print4]
my_xer_list = [my_Xerox1, my_Xerox2, my_Xerox3, my_Xerox4]

my_Warehouse = t.OfficeEquipmentWarehouse(10, 8, 10)
my_Warehouse.store(my_print_list, my_xer_list, my_scan_list)

print("Default list of equipment: ")
for el in my_scan_list:
    el.print_info()

for el in my_print_list:
    el.print_info()

for el in my_xer_list:
    el.print_info()

print("First model of Printer: ", my_Warehouse.printer_equipments[0].model)
print("First model of Xerox: ", my_Warehouse.xerox_equipments[0].model)
print("First model of Scanner: ", my_Warehouse.scanner_equipments[0].model)
print("Printer info: ", my_Warehouse.equipment_count(my_print_list))
print("Xerox info: ", my_Warehouse.equipment_count(my_xer_list))
print("Scanner info: ", my_Warehouse.equipment_count(my_scan_list))
