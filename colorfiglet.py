from pyfiglet import figlet_format
from colorama import init
from termcolor import colored

init()


def print_art(msg, color):
    valid_colors = ("black", "red", "green", "yellow", "blue", "magenta", "cyan", "white", "light_grey","dark_grey", "light_red", "light_green", "light_yellow", "light_blue", "light_magenta", "light_cyan")

    if color not in valid_colors:
        color = "green"

    ascii_art = figlet_format(msg)
    colored_ascii = colored(ascii_art, color=color)
    print(colored_ascii)


msg = input("What would you like to print? \n")
coloranswer = input("What color?\n")
color = coloranswer.lower()
print_art(msg, color)
