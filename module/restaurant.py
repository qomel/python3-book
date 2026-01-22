"""Wyświetlenie informacji na temat restauracji"""

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