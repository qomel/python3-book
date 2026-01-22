from user import User

class Admin(User):
    """Sprawdzenie admina"""
    
    def __init__(self, first_name, last_name, date_of_birth, user_name):
        super().__init__(first_name, last_name, date_of_birth, user_name)

        self.privileges = Privileges()
    
        
class Privileges():
    """Wyświetlenie praw jako admin"""
        
    def __init__(self, privileges = []):
        self.privileges = privileges
    
    def show_privileges(self):
        if self.privileges:
            for privilege in self.privileges:
                print(privilege) 
        else:
            print('User dont have privileges')        
    