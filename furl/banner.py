"""
    Creating a logo using PyFiglet
    Maryoux
"""
from colorama import Style
from pyfiglet import Figlet

def display_banner():
    """Function used to call pyfiglet to create a 'Furl' text"""
    custom_fig = Figlet(font='slant')
    print(custom_fig.renderText('furl') + Style.RESET_ALL)
    print("\tv1.0.2")
    print("\tMaryoux\n\n")
