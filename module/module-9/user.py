"""Wyświetlanie szczegółów użytkownika"""


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
        
