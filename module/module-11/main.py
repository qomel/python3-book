

def eleven_1(city, country, population=None):
    """Wyświetlania Państwo, Miasto"""
    if population:
        location_city = f"{country}, {city} - populacja {population}"
    else:
        location_city = f"{country}, {city}"
    return location_city

def eleven_2():
    class Employee:
        
        def __init__(self, name, last, year_salary):
            self.name = name
            self.last = last
            self.year_salary = year_salary
            
        def give_raise(self, ammount=5000):
            self.year_salary += ammount

    return Employee
