from pathlib import Path

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

ten_5()