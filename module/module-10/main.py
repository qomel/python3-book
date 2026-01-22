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
ten_3()