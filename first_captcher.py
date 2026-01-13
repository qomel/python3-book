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
    
def four_13():
    bufet = ('ciasto', 'obiad', 'sniadanie', 'kolacja', 'podwieczorek')
    for i in bufet:
        print(i)
    # bufet[1] = 'jedzenie'
    
    bufet = ('\nzamknietę',)
    for i in bufet:
        print(i)

def cars_py5():
    cars = ['audi',
            'bmw',
            'honda',
            'kiv',
            'reanulte',
            'porsche'
            ]
    
    for car in cars:
        if car == 'bmw':
            print(car.upper())
        else:
            print(car.title())
    
    
cars_py5()

 