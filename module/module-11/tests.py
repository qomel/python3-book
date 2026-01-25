from main import eleven_1, eleven_2

def test_location_city():
    """Czy dane wyświetalją się poprawnie"""
    location_city = eleven_1('Santiago', 'Chile')
    assert location_city == 'Chile, Santiago'

def test_location_city_population():
    """Czy dane wyświetalją się poprawnie"""
    location_city = eleven_1('Santiago', 'Chile', 5000 )
    assert location_city == 'Chile, Santiago - populacja 5000'

def test_give_deafult_rise():
    Employee = eleven_2()
    employee = Employee('Dominik', 'Pazurek', 55_000)
    employee.give_raise()
    assert employee.year_salary == 60_000
    
def test_give_custom_raise():
    Employee = eleven_2()
    employee = Employee('Dominik', 'Pazurek', 60_000)
    employee.give_raise(10000)
    assert employee.year_salary == 70_000  