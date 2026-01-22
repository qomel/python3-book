from restaurant import Restaurant
from user import Admin, Privileges

def nine_10():
    rest1 = Restaurant('Makłowicz', 'Oldfashion')
    rest1.describer_restaurant()

def nine_11():
    admin1 = Admin('Kamil', 'Pazurek', '22.09.2010', 'Kapek')
    
    admin1.privileges.privileges = ['ban', 'unban']
    admin1.privileges.show_privileges()
    admin1.describe_user()

nine_11()