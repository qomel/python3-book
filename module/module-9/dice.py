"""Moduł symulujący rzut kostką."""

from random import randint


class Dice():
    """Klasa reprezentująca kostkę do gry.
    
    Attributes:
        sides (int): Liczba ścian kostki.
    """
    
    def __init__(self, sides=6):
        """Inicjalizuje kostkę z podaną liczbą ścian.
        
        Args:
            sides (int): Liczba ścian kostki. Domyślnie 6.
        """
        self.sides = sides
        
    def roll_dice(self):
        """ Wykonuje 10 rzutów kostką i wyświetla wyniki.
            Każdy rzut generuje losową liczbę od 1 do liczby ścian kostki.
        """
        for i in range(10):
            roll = randint(1, self.sides)
            print(roll)

