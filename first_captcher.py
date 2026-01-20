#import this - Zen Python

def first_letter_upper_case():
    name = 'dom paz'
    print(name.title())

def full_upper_case():
    name = 'dom paz'
    print(name.upper())

def full_lower_case():
    name = 'DOM PAZ'
    print(name.lower())

def full_name():
    first_name = 'dominik'
    last_name = 'pazurek'
    full_name = f"{first_name.title()} {last_name.title()}"
    print(full_name)

def  three_1():
    name = ['dominik', 'michalina', 'kamil']
    for n in name:
        print(f"Cześć, {n.title()}!")


def three_4():
    goscie = ['dominik', 'michalina', 'kamil']
    for i in goscie:
        print(F"Zapraszam Cię na obiad, {i.title()}.")

    # --------- 3.5
    cantBe = goscie.pop(1)
    print(f"{cantBe.title()} niestety nie może przyjść.\n\tZapraszam kogoś innego.")
    goscie.insert(1, 'anna')
    goscie.append('adam')
    print(f'Zapraszam Cię na obiad, {goscie[1].title()} i {goscie[-1].title()}.')

    # --------- 3.6
    print('Znalazłem większy stół, więc zapraszam więcej gości.')
    goscie.insert(0, 'jan')
    goscie.insert(2, 'ewa')
    goscie.append('piotr')
    for i in goscie:
        print(F"Zapraszam Cię na obiad, {i.title()}.")
    print(len(goscie))
    
    # --------- 3.7
    cantBe2 = goscie.pop(1), goscie.pop(2), goscie.pop(-1), goscie.pop(-2), goscie.pop(-3)
    print(f'Niestety mogę zaprosić tylko dwóch gości. Przepraszam {cantBe2}')
    for i in goscie:
        print(F"Zapraszam Cię na obiad, {i.title()}.")

    del goscie[0]
    del goscie[0]
    print(goscie)
    
def three_8():
   place = ['tokyo',
            'paris',
            'new york',
            'sydney',
            'rome'
            ]    
   print(place)
   print(sorted(place))
   print(place)
   print(sorted(place, reverse=True))
   print(place)
   place.reverse()
   print(place)
   place.sort()
   print(place)
   place.sort(reverse=True)
   print(place)


   
def three_10():
    cars = ['bmw', 'audi', 'porsche', 'apple']
    rivers = ['rudka', 'odra']
    city = ['tokyo', ' newyork', 'singapure ']
    
    for i in city:
        print(f"\ncars: {i.title().strip()}")
    
    rivers.append('wisla')
    print(rivers)
    
    del cars[-1]
    cars.append('toyota')
    print(cars)
       
    print(sorted(rivers))
    print(len(city))
    
def six_1():
    people = {
        'first': 'Dominik', 
        'last': 'Pazurek',
        'age': '23',
        'city': 'gliwice'
              }
    
    print(people)
    
    numbers = {
        'michalina': '8',
        'dominik': '10'
        }
    
    print(f'Ulubionym numerem {numbers['dominik']}')
    print(f'Ulubionym numerem {numbers['michalina']}')
    
    glosariusz = {
        'dictionary': 'cos w stylu listy dynamicznej ale ma key-value',
        'tuple': 'lista której nie da się modyfikować',
        'not / in': 'czy ta zmeina znajduje się/czy nie w liście'
    }
    
    for key, value in  glosariusz.items():
        print(key + ': ' + value)
    
    
def six_4():
    
    glosariusz = {
        'dictionary': 'cos w stylu listy dynamicznej ale ma key-value',
        'tuple': 'lista której nie da się modyfikować',
        'not / in': 'czy ta zmeina znajduje się/czy nie w liście'
    }
    
    for key, value in  glosariusz.items():
        print(key + ': ' + value)
        
    glosariusz['PEP8'] = 'jest to ustalony rodzaj formatowania kody w python'
    
    rzeki = {
        'wisla': 'warszawa',
        'odra': 'raciborz',
        'rudka': 'kuznia'
        }
    
    for k, v in rzeki.items():
        print(k.title() + ' przepływa przez ' + v.title())
        
    for k in rzeki.keys():
        print(k.lower())

    for v in rzeki.values():
        print(v.upper())
    
    ankieta = {
        'dominik': 'Python',
        'michalina': 'C',
        'kamil': 'Rust'
    }
    
    nie_wzieły_ankiety = {
        'dominik', 'adam'
    }
    
    for name in nie_wzieły_ankiety:
        if name in ankieta:
            print(f'Dziękuje za ankiete {name.title()}')
        else:
            print(f'Prosze o wziecie udzialu {name.title()}')
            

def six_7():
        people1 = {
        'first': 'Dominik', 
        'last': 'Pazurek',
        'age': '23',
        'city': 'gliwice'
        }
        
        people2 = {
        'first': 'Michalina', 
        'last': 'Knieja',
        'age': '22',
        'city': 'gliwice'
        }
        
        people3 = {
        'first': 'Kamil', 
        'last': 'Pazurek',
        'age': '15',
        'city': 'kuźnia'
        }
        
        people = [people1, people2, people3]
        
        for user in people:
            print(user)
            
        places = {
            'dominik': ['gl', 'sk', 'rck'],
            'michalina': ['sk', 'mk', 'ny'],
            'kamil': ['rck', 'tk', 'sp']
        }
        
        for place in places.items():
            print(place)
            
        citys = {
            'tokyo': {
                'where': 'Asia',
                'valute': 'yen'
            },
            
            'warsaw': {
                'where': 'Europe',
                'valute': 'pln'
            }
        }
        
        for city, info in citys.items():
            print(city.title())
            if info['valute'] == 'pln':
                print(info['valute'].upper())
            else:
                print('Ang')
            print(f'Country in: {info['where']}')

def seven_1():
    marka = input('Jaki Pan potrzebuje marki samochodu: ')
    print(f'Sprawdzam czy jest {marka}')
    
def seven_2():
    number = input('na ile osób stoilik: ')
    number = int(number)
    
    if number >= 8:
        print('Trzbea poczekac na większy stolik')
    else:
        print('Prosze wejść')

def seven_3():
    number = input('Podaj dowolną liczbę: ')
    number = int(number)
    
    if number % 10 == 0:
        print('To jest wielokrtonsc 10')
    else:
        print('To nie jest wielokrotność 10')
    
def seven_4():
    lista_dodatkow = []
    dodatki = ""
    
    while dodatki != 'koniec':
        dodatki = input('Jakie dodatki na pizze? ')
        if dodatki == 'koniec':
            break
        lista_dodatkow.append(dodatki)
        print(*lista_dodatkow)

def seven_5():
    active = True
    
    while active != False:
        age = input('Ile masz la: ')
        age = int(age)
        
        if age <= 3:
            print('Za darmo')
        elif age in range(3, 12):
            print('10zł bilet')
        elif age == 888:
            active = False
        elif age >= 12:
            print('15zl')
        else:
            print('Zły foramt')
            
def seven_8():
    sandwich_orders = ['Kanpka', 'Croissant', 'Bagietka', 'Sandwich']
    finished_sandwich = []
    
    while sandwich_orders:
        curret_sandwich = sandwich_orders.pop()
        
        print(f'{curret_sandwich} jest gotowa')
        finished_sandwich.append(curret_sandwich)
    
    print(f'Gotowe: {finished_sandwich}')

def seven_9():
    sandwich = ['Kanapka', 'Croissant', 'Kanapka', 
                'Bagietka', 'Sandwich', 'Kanapka']
    i = 0
    print(sandwich)
    while 'Kanapka' in sandwich:
        i += 1
        sandwich.remove('Kanapka')
        print(f'Usnieto x{i}')
        
    print(sandwich)
    
def seven_10():
    responses = {}
    polling_active = True
    
    while polling_active:
        name = input('\nJak masz na imie ')
        response = input('Gdzie chciał/a byś poleciec na wakajce ')
        
        responses[name] = response
        
        repeat = input('Ktoś jescze tak/nie?')
        if repeat == 'nie':
            polling_active = False
            
    print('\n---Wyniki---')
    for name, resposne in responses.items():
        print(f'{name} chciałby poleciec {resposne}')
    

def eight_2(title):
    print(f'Ulubiona książka: {title}')

# eight_2('Python')