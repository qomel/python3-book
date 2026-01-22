from restaurant import Restaurant
from user import User
from admin import Admin, Privileges
from dice import Dice

from random import choice

def nine_10():
    rest1 = Restaurant('Makłowicz', 'Oldfashion')
    rest1.describer_restaurant()

def nine_11():
    admin1 = Admin('Kamil', 'Pazurek', '22.09.2010', 'Kapek')
    
    admin1.privileges.privileges = ['ban', 'unban']
    admin1.privileges.show_privileges()
    admin1.describe_user()

def nine_12():
    admin = Admin('Kamil', 'Pazurek', '22.09.2010', 'Kapek')
    
    admin.privileges.privileges = ['ban', 'unabn']
    admin.privileges.show_privileges()
    
def nine_13():
    my_dice = Dice(10)
    my_dice.roll_dice()
    
def nine_14():
    numbers = [
        1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 
        'A', 'B', 'C', 'D', 'E'
        ]
    
    lucky_numbers = []
    my_ticket = []
    
    print('Jeśli masz któryś z tych indexów wygrałeś loterie')
    
    for i in range(4):
        num = choice(numbers)
        lucky_numbers.append(num)
    
    y = 0   
    while True:
        my_ticket = [choice(numbers) for _ in range(4)]
        y += 1
        if my_ticket == lucky_numbers:
            break

    
    print(f'{y} tyle razy musiałbyś zagrać żeby wygrać')
    print(*lucky_numbers)

nine_14()