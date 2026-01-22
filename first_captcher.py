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

def eight_3():
    # Wyświetla rozmiar oraz tekst koszulki
    def make_shirt(rozmair, tekst):
        print(f'Zamówiłeś koszulke {rozmair.upper()} z tekstem: {tekst}')
        
    make_shirt(rozmair = 'L', tekst = 'Super L L L')


def eight_4():
    def make_shirt(rozmiar = 'L', tekst = 'Uwielbiam Python'):
        print(f'Zamówiłeś koszulke {rozmiar.upper()} z tekstem: {tekst}')
    
    make_shirt('L')
    make_shirt('m')
    make_shirt('m', 'elo elo')

def eight_5():
    def describe_city(city, country='kraju'):
        print(f'{city} leży w {country}')
    
    describe_city('Warszawa', 'Polska')
    describe_city('Gdzieś')
    describe_city('','elo')
        
def eight_6():
    """Wyświetla 'miasto, kraj' """
    def city_country(city, countery):
        cityCountry = f"{city}, {countery}"
        return cityCountry
    
    city = city_country('Warsz', 'Polska')
    print(city)

def eight_7():
    def make_albums(title ,band="", artist="", many=None):
        
        album = {'title': title}
        if band:
            album['band'] = band
        if artist:
            album['artist'] = artist
        if many:
            album['how many'] = many
        return album
    musican = make_albums('Okoń', 'Karpiki', 'Wędkarz')
    musican2 = make_albums('Mrowik', 'Chujki')
    musican3 = make_albums('Alku', '', 'Mordka')
    musican4 = make_albums('Alku', '', 'Mordka', 5)
    
    print(musican3)
    
    
def eight_8():
    
    def make_albums(title ,band="", artist="", many=None):
        
        album = {'title': title}
        if band:
            album['band'] = band
        if artist:
            album['artist'] = artist
        if many:
            album['how many'] = many
        return album
    
    while True:
        print('\nProsze podać nazwe albumu, zespół lub artyste,' 
              ' można dodać ilość utworów')
        print('Wpisz "q", aby zatrzymać program w dowonlnym momencie')
        
        title = input('Tytuł albumu: ')
        if title == 'q':
            break
        
        band = input('Nazwa zespołu (jeśli nie ma kliknij ENTER): ')
        if band == 'q':
            break
        
        artist = input('Jak nazywa się artysta (jeśli nie ma kliknij ENTER):')
        if artist == 'q':
            break
        
        many = input('Ile jest utworów (pomiń klikająć ENTER): ')
        if many == 'q':
            break
        
        album = make_albums(title, band, artist, many)
        print(album)
        
def eight_9():
    
    def show_messages(messages):
        """Wyświetelnie komunikatów"""
        for message in messages:
            print(f'{message}')
            
    messages = ['elo', 'siema', 'co tam?']
    show_messages(messages)

def eight_10():
    
    def send_message(messages):
        """Wysyłanie wiadmości"""
        while messages:
            current_message = messages.pop()
            print(current_message)
            sent_messages.append(current_message)
            
    messages = ['elo', 'siema', 'co tam?']
    sent_messages = []
    
    send_message(messages)
    print(f'lista wysłanych: {sent_messages}')

def eight_11():
    
    def send_message(messages):
        """Wysyłanie wiadmości"""
        while messages[:]:
            current_message = messages.pop()
            print(current_message)
            sent_messages.append(current_message)
            
    messages = ['elo', 'siema', 'co tam?']
    sent_messages = []
    # lista archi jest pełna ponieważ zostałą do funkcji wrzuocna kopia
    send_message(messages[:])
    print(f'lista wysłanych: {sent_messages}')
    print(f'lista archi: {messages}')

def eight_12():
    
    def sandwich(*toppings):
        print('\nW twojej kanpace będzie znajdować się: ')
        for topping in toppings:
            print(f'- {topping.lower()}')
            
    sandwich('Sałata', 'Ser', 'Szynka')
    sandwich('Szynka', 'pomidor', 'kiełbasa')
    
def eight_13():
    
    def build_profile(first, last, **user_info):
        """Budowa słownika zaweirającego wszelkie informacje o użytkowniku"""
        user_info['first_name'] = first
        user_info['last_name'] = last
        return user_info
    
    user_profile = build_profile('dominik', 'pazurek',
                                 location = 'Poland',
                                 field = 'software enginner')
    print(user_profile)
    
def eight_14():
    
    def make_car(brand, model, **car_info):
        car_info['marka'] = brand
        car_info['model'] = model
        return car_info
    
    cars = make_car('Subaru', 'Impreza',
                   color = 'blue',
                   engine = '2.0')
    
    print(cars)

def nine_1():
    
    class Restaurant:
        
        def __init__(self, restaurant_name, cuisine_type):
            self.restaurant_name = restaurant_name
            self.cuisine_type = cuisine_type
            
        def describer_restaurant(self):
            print(f'Restuaracja: {self.restaurant_name}\nW stylu: {self.cuisine_type}')
            
        def open_restaurant(self):
            print(f'Restauracja: {self.restaurant_name} otwiera się 10 godzinei')
            
    rest1 = Restaurant('Alohomora', 'Old')
    rest2 = Restaurant('Oklahoma', 'Foodtruck')
    
    print(f'Super jest: {rest1.restaurant_name}')
    rest1.describer_restaurant()
    
    print(f'Mają styl: {rest2.cuisine_type}')
    rest2.open_restaurant()

def nine_3():
    
    class User:
        """Prezentacja prostego profilu uzytkownika"""
        
        def __init__(self, first_name, last_name, date_of_birth, user_name):
            self.first_name = first_name
            self.last_name = last_name
            self.date_of_birth = date_of_birth
            self.user_name = user_name
            
        def describe_user(self):
            full_name = f'{self.first_name} {self.last_name}'
            print(f'\n---OPIS UŻYTKOWNIKA---'
                  f'\n{full_name} | {self.user_name}'
                  f'\nUrodzony: {self.date_of_birth}')
            
        def greet_user(self):
            print(f'\nWitaj {self.user_name}')
            
    user1 = User('Dominik', 'Pazurek', '10.03.2002', 'qomel')
    user1.describe_user()
    user1.greet_user()
    
    user2 = User('Michalina', 'Knieja', '12.06.2003', 'misia')
    user2.describe_user()
    user2.greet_user()
    
def nine_4():
    
    class Restaurant:
        
        def __init__(self, restaurant_name, cuisine_type):
            self.restaurant_name = restaurant_name
            self.cuisine_type = cuisine_type
            self.number_served = 0
            
        def describer_restaurant(self):
            print(f'Restuaracja: {self.restaurant_name}\nW stylu: {self.cuisine_type}')
            print(f'Akutalnie obsłużoncyh: {self.number_served}')
        def open_restaurant(self):
            print(f'Restauracja: {self.restaurant_name} otwiera się 10 godzinei')

        def set_number_served(self, served):
            """Przypisanie wartosci do obsłużoncyh"""
            self.number_served = served
        
        def increment_number_served(self, total):
            """Inkrementacja obsłużoncyh klinetów"""
            self.number_served += total
            
    rest1 = Restaurant('Alohomora', 'Old')
    rest2 = Restaurant('Oklahoma', 'Foodtruck')
    
    print(f'Super jest: {rest1.restaurant_name}')
    rest1.describer_restaurant()
    
    print(f'Mają styl: {rest2.cuisine_type}')
    rest2.open_restaurant()
    
    rest2.set_number_served(23)
    rest2.describer_restaurant()
    rest2.increment_number_served(10)
    rest2.describer_restaurant()
    
def nine_5():
    
    class User:
        """Prezentacja prostego profilu uzytkownika"""
        
        def __init__(self, first_name, last_name, date_of_birth, user_name):
            self.first_name = first_name
            self.last_name = last_name
            self.date_of_birth = date_of_birth
            self.user_name = user_name
            self.login_attempts = 0
            
        def describe_user(self):
            full_name = f'{self.first_name} {self.last_name}'
            print(f'\n---OPIS UŻYTKOWNIKA---'
                  f'\n{full_name} | {self.user_name}'
                  f'\nUrodzony: {self.date_of_birth}')
            
        def greet_user(self):
            print(f'\nWitaj {self.user_name}')
            
        def increment_attempts(self):
            """Inkrementacja prób logowania"""
            self.login_attempts += 1
        
        def reset_attempts(self):
            """Reset prób logowań"""
            self.login_attempts = 0
        
        def show_attempts(self):
            """Show a number of login attempts"""
            print(f'{self.login_attempts}')
        
    user1 = User('Dominik', 'Pazurek', '10.03.2002', 'qomel')
    user1.describe_user()
    user1.greet_user()
    
    user2 = User('Michalina', 'Knieja', '12.06.2003', 'mknieja')
    user2.describe_user()
    user2.greet_user()
    
    user2.increment_attempts()
    user2.increment_attempts()
    user2.show_attempts()
    user2.reset_attempts()
    user2.show_attempts()
    
def nine_6():
    
    class Restaurant:
        
        def __init__(self, restaurant_name, cuisine_type):
            self.restaurant_name = restaurant_name
            self.cuisine_type = cuisine_type
            self.number_served = 0
            
        def describer_restaurant(self):
            print(f'Restuaracja: {self.restaurant_name}\nW stylu: {self.cuisine_type}')
            print(f'Akutalnie obsłużoncyh: {self.number_served}')
            
        def open_restaurant(self):
            print(f'Restauracja: {self.restaurant_name} otwiera się 10 godzinei')

        def set_number_served(self, served):
            """Przypisanie wartosci do obsłużoncyh"""
            self.number_served = served
        
        def increment_number_served(self, total):
            """Inkrementacja obsłużoncyh klinetów"""
            self.number_served += total
    
    class IceCreamStand(Restaurant):
        
        def __init__(self, restaurant_name, cuisine_type):
            super().__init__(restaurant_name, cuisine_type)
            self.flavors = []
        
        def show_icecream(self):
            for flavor in self.flavors:
                print(flavor)
        
    rest1 = Restaurant('Alohomora', 'Old')
    rest2 = Restaurant('Oklahoma', 'Foodtruck')
    
    print(f'Super jest: {rest1.restaurant_name}')
    rest1.describer_restaurant()
    
    print(f'Mają styl: {rest2.cuisine_type}')
    rest2.open_restaurant()
    
    rest3 = IceCreamStand('Lodowu Edek', 'Bar')
    rest3.describer_restaurant()
    rest3.flavors = ['vanilla', 'chocolate']
    rest3.show_icecream()
    
def nine_7():
    
    class User:
        """Prezentacja prostego profilu uzytkownika"""
        
        def __init__(self, first_name, last_name, date_of_birth, user_name):
            self.first_name = first_name
            self.last_name = last_name
            self.date_of_birth = date_of_birth
            self.user_name = user_name
            self.login_attempts = 0
            
        def describe_user(self):
            full_name = f'{self.first_name} {self.last_name}'
            print(f'\n---OPIS UŻYTKOWNIKA---'
                  f'\n{full_name} | {self.user_name}'
                  f'\nUrodzony: {self.date_of_birth}')
            
        def greet_user(self):
            print(f'\nWitaj {self.user_name}')
            
        def increment_attempts(self):
            """Inkrementacja prób logowania"""
            self.login_attempts += 1
        
        def reset_attempts(self):
            """Reset prób logowań"""
            self.login_attempts = 0
        
        def show_attempts(self):
            """Show a number of login attempts"""
            print(f'{self.login_attempts}')
        
    class Admin(User):
        
        def __init__(self, first_name, last_name, date_of_birth, user_name):
            super().__init__(first_name, last_name, date_of_birth, user_name)

            self.privileges = Privileges()
            
    class Privileges():
        
        def __init__(self, privileges = []):
            self.privileges = privileges
        
        def show_privileges(self):
            if self.privileges:
                for privilege in self.privileges:
                    print(privilege) 
            else:
                print('User dont have privileges')        
        
    user1 = User('Dominik', 'Pazurek', '10.03.2002', 'qomel')
    user1.describe_user()
    user1.greet_user()
    
    user2 = User('Michalina', 'Knieja', '12.06.2003', 'mknieja')
    user2.describe_user()
    user2.greet_user()
    
    user3 = Admin('Kamil', 'Pazurek', '22.09.2010', 'kapek')
    user3.describe_user()

    user3_privileges = [
        'ban',
        'unban'
    ]
    user3.privileges.privileges = user3_privileges
    user3.privileges.show_privileges()
    
def nine_9():
    
    class Car:
        """A simple attempt to represent a car."""

        def __init__(self, make, model, year):
            """Initialize attributes to describe a car."""
            self.make = make
            self.model = model
            self.year = year
            self.odometer_reading = 0

        def get_descriptive_name(self):
            """Return a neatly formatted descriptive name."""
            long_name = f"{self.year} {self.make} {self.model}"
            return long_name.title()

        def read_odometer(self):
            """Print a statement showing the car's mileage."""
            print(f"This car has {self.odometer_reading} miles on it.")

        def update_odometer(self, mileage):
            """Set the odometer reading to the given value."""
            if mileage >= self.odometer_reading:
                self.odometer_reading = mileage
            else:
                print("You can't roll back an odometer!")

        def increment_odometer(self, miles):
            """Add the given amount to the odometer reading."""
            self.odometer_reading += miles


    class Battery:
        """A simple attempt to model a battery for an electric car."""

        def __init__(self, battery_size=40):
            """Initialize the battery's attributes."""
            self.battery_size = battery_size

        def describe_battery(self):
            """Print a statement describing the battery size."""
            print(f"This car has a {self.battery_size}-kWh battery.")

        def get_range(self):
            """Print a statement about the range this battery provides."""
            if self.battery_size == 40:
                range = 150
            elif self.battery_size == 65:
                range = 225

            print(f"This car can go about {range} miles on a full charge.")

        def upgrade_battery(self):
            if self.battery_size == 40:
                print('Changing accumulator on better one')
                self.battery_size = 65
            else:
                print('You had the best accumulator in car')
                
    class ElectricCar(Car):
        """Represent aspects of a car, specific to electric vehicles."""

        def __init__(self, make, model, year):
            """
            Initialize attributes of the parent class.
            Then initialize attributes specific to an electric car.
            """
            super().__init__(make, model, year)
            self.battery = Battery()


    my_leaf = ElectricCar('nissan', 'leaf', 2024)
    print(my_leaf.get_descriptive_name())
    my_leaf.battery.describe_battery()
    my_leaf.battery.get_range()
    
    my_leaf.battery.upgrade_battery()
    my_leaf.battery.get_range()


