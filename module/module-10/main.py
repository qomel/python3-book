from pathlib import Path
import json
def ten_1():
    path = Path('text.txt')
    contents = path.read_text()
    print(contents)

    lines = contents.splitlines()
    contents_str = ''
    
    for line in lines:
        contents_str += line
        
    print(contents_str)
    print(len(contents_str))
    
def ten_2():
    path = Path('text.txt')
    contents = path.read_text()
    contents = contents.replace('XD', 'Lorem')
    print(contents)

def ten_3():
    path = Path('text.txt')
    contents = path.read_text()
    contents_str = ''
    for line in contents.splitlines():
        contents_str += line
    
    print(contents_str)
    print(len(contents_str))
    
def ten_4():
    contents = input('Jak masz na imie: ')
    
    path = Path('guest.txt')
    path.write_text(contents)

def ten_5():
    path = Path('guest_book.txt')
    
    msg = 'Podaj imie: '
    msg += 'q do wyjścia'
    
    guest_name = []
     
    while True:
        name = input(msg)
        if name == 'q':
            break
        
        print(f'Witaj {name}')
        guest_name.append(name)
    
    file_string = ''

    for name in guest_name:
        file_string += f'{name} \n'
        
    path.write_text(file_string)

def ten_6():
    number_x = input('Podaj pierwszą liczbę: ')
    number_y = input('Podaj drugą liczbę: ')
    
    try:
        sum = int(number_x) + int(number_y)
    except ValueError:
        print('Podałeś znaki zamiast liczb')
    else:
        print(sum)

def ten_7():
    while True:
        number_x = input('Podaj pierwszą liczbę: ')
        if number_x == 'q':
            break
        
        number_y = input('Podaj drugą liczbę: ')
        if number_y == 'q':
            break
        
        try:
            sum = int(number_x) + int(number_y)
        except ValueError:
            print('Podałeś znaki zamiast liczb')
        else:
            print(sum)

def ten_8():
    """ 
    Wyświetlanie informacji z pliów z łapaniem błędów 
    przy braku pliku i wyświetlaniem którego nie ma
    """
    filenames = ['cats.txt', 'dogs.txt']
    
    for filename in filenames:
        path = Path(filename)
        
        try:
            msg = path.read_text(encoding='utf-8')
            print(msg)   
        
        except FileNotFoundError:
            print(f'Nie ma pliku {filename}')          

def ten_9():
    """ 
    Wyświetlanie informacji z pliów z łapaniem błędów 
    przy braku pliku i wyświetlaniem którego nie ma
    """
    filenames = ['cats.txt', 'dogs.txt']
    
    for filename in filenames:
        path = Path(filename)
        
        try:
            msg = path.read_text(encoding='utf-8')
            print(msg)   
        
        except FileNotFoundError:
            pass

def ten_10():
    """Wyświetlanie ile razy pojawiło się słowo w pliku"""
    path = Path('book.txt')
    book = path.read_text(encoding='utf-8')
    
    count = book.count('I')
    print(count)
    
def ten_11():
    def first():
        path = Path('fav_number.json')
        
        fav_number = input('Podaj ulubioną liczbę: ')
        contents = json.dumps(fav_number)
        path.write_text(contents)

    def second():
        path = Path('fav_number.json')
        contents = path.read_text()
        fav_number = json.loads(contents)
        print(f'Twoja ulubiona liczba to: {fav_number}')
    
    first()
    second()

def ten_12():
    path = Path('fav_number.json')
    
    if path.exists():
        contents = path.read_text()
        fav_number = json.loads(contents)
        print(f'Twoja ulubiona liczba  to: {fav_number}')
    else:
        fav_number = input('Podaj swoją ulubioną liczbe: ')
        contents = json.dumps(fav_number)
        path.write_text(contents)
    
def ten_13():

    
    path = Path('username.json')
    if path.exists():
        contents = path.read_text()
        user_dict = json.loads(contents)
        username = user_dict['username']
        last_name = user_dict['last_name']
        print(f'Witam ponownie {username} {last_name}')
    else:        
        username = input('Jak masz na imie? ')
        last_name = input('Jak masz na nazwisko? ')
        
        user_dict = {
            'username': username,
            'last_name': last_name
        }
        contents = json.dumps(user_dict)
        path.write_text(contents)
        print('Twoje imie zostało zapisane')
        
def ten_14():
    def get_stored_user_info(path):
        if path.exists():
            contents = path.read_text()
            user_dict = json.loads(contents)
            return user_dict
        else:
            return None

    def get_new_user_info(path):
        """Get information from a new user."""
        username = input("What is your name? ")
        game = input("What's your favorite game? ")
        animal = input("What's your favorite animal? ")

        user_dict = {
            'username': username,
            'game': game,
            'animal': animal,
        }

        contents = json.dumps(user_dict)
        path.write_text(contents)
        return user_dict

    def greet_user():
        """Greet the user by name, and state what we know about them."""
        path = Path('user_info.json')
        user_dict = get_stored_user_info(path)
        question = input('Jak masz na imie? ')
        
        if user_dict and user_dict['username'] == question:
                print(f"Welcome back, {user_dict['username']}!")
                print(f"Hope you've been playing some {user_dict['game']}. ")
                print(f"Have you seen a {user_dict['animal']} recently?")
        else:
            user_dict = get_new_user_info(path)
            msg = f"We'll remember you when you return, {user_dict['username']}!"
            print(msg)

    greet_user()

ten_14()