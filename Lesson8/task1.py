class UserData:

    @classmethod
    def user_date_to_int(cls, string: str):
        num_list = [int(string.split('-')[0]), int(string.split('-')[1]), int(string.split('-')[2])]
        return num_list

    @staticmethod
    def is_correct(string: str):
        y = UserData.user_date_to_int(string)[2]
        m = UserData.user_date_to_int(string)[1]
        d = UserData.user_date_to_int(string)[0]
        if y % 4 == 0:
            print("\nIt's leap year")
            if m == 4 or m == 6 or m == 9 or m == 11:
                print("Month is correct")
                if 0 < d <= 30:
                    print("Day is correct")
                    return "Date is correct"
                else:
                    print("Day is not correct")
                    return "Date is not correct because of day"
            elif m == 2:
                print("Month is correct")
                if 0 < d <= 29:
                    print("Day is correct")
                    return "Date is correct"
                else:
                    print("Day is not correct")
                    return "Date is not correct because of day"
            elif m == 1 or m == 3 or m == 5 or m == 7 or m == 8 or m == 10 or m == 12:
                print("Month is correct")
                if 0 < d <= 31:
                    print("Day is correct")
                    return "Date is correct"
                else:
                    print("Day is not correct")
                    return "Date is not correct because of day"
            elif (m < 0 or m > 12) and 0 < d <= 31:
                print("Month is not correct")
                return "Date is not correct because of month"
            else:
                print("Month and Day are not correct")
                return "Date is not correct because of month and day"
        else:
            print("\nIt's not leap year")
            if m == 4 or m == 6 or m == 9 or m == 11:
                print("Month is correct")
                if 0 < d <= 30:
                    print("Day is correct")
                    return "Date is correct"
                else:
                    print("Day is not correct")
                    return "Date is not correct because of day"
            elif m == 2:
                print("Month is correct")
                if 0 < d <= 28:
                    print("Day is correct")
                    return "Date is correct"
                else:
                    print("Day is not correct")
                    return "Date is not correct because of day"
            elif m == 1 or m == 3 or m == 5 or m == 7 or m == 8 or m == 10 or m == 12:
                print("Month is correct")
                if 0 < d <= 31:
                    print("Day is correct")
                    return "Date is correct"
                else:
                    print("Day is not correct")
                    return "Date is not correct because of day"
            elif (m < 0 or m > 12) and 0 < d <= 31:
                print("Month is not correct")
                return "Date is not correct because of month"
            else:
                print("Month and Day are not correct")
                return "Date is not correct because of month and day"


print("Date N1 00-00-0000: ", UserData.is_correct("00-00-0000"))
print("Date N2 29-02-2020: ", UserData.is_correct("29-02-2020"))
print("Date N3 30-02-2020: ", UserData.is_correct("30-02-2020"))
print("Date N4 29-02-2021: ", UserData.is_correct("29-02-2021"))
print("Date N5 30-04-1999: ", UserData.is_correct("30-04-1999"))
print("Date N6 31-04-1999: ", UserData.is_correct("31-04-1999"))
print("Date N7 31-12-2000: ", UserData.is_correct("31-12-2000"))
print("Date N8 32-12-2000: ", UserData.is_correct("32-12-2000"))
print("Date N9 10-13-2000: ", UserData.is_correct("10-13-2000"))
