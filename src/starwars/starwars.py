import time
import os
from colorama import Fore, init

init(autoreset=True)

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def star_wars_intro():
    intro_text = [
        f"{Fore.BLUE}A long time ago in a galaxy far,",
        f"{Fore.BLUE}far away....",
        "",
        f"{Fore.YELLOW}                  ________________.  ___     .______          ",
        f"{Fore.YELLOW}                 /                | /   \\    |   _  \\         ",
        f"{Fore.YELLOW}                |   (-----|  |----`/  ^  \\   |  |_)  |        ",
        f"{Fore.YELLOW}                 \\   \\    |  |    /  /_\\  \\  |      /         ",
        f"{Fore.YELLOW}            .-----)   |   |  |   /  _____  \\ |  |\\  \\-------. ",
        f"{Fore.YELLOW}            |________/    |__|  /__/     \\__\\| _| ` .________| ",
        f"{Fore.YELLOW}             ____    __    ____  ___     .______    ________. ",
        f"{Fore.YELLOW}             \\   \\  /  \\  /   / /   \\    |   _  \\  /        | ",
        f"{Fore.YELLOW}              \\   \\/    \\/   / /  ^  \\   |  |_)  ||   (-----`  ",
        f"{Fore.YELLOW}               \\            / /  /_\\  \\  |      /  \\   \\      ",
        f"{Fore.YELLOW}                \\    /\\    / /  _____  \\ |  |\\  \\---)   |     ",
        f"{Fore.YELLOW}                 \\__/  \\__/ /__/     \\__\\|__| `._______/       ",
        "",
        f"{Fore.GREEN}Episode IV",
        f"{Fore.GREEN}A NEW HOPE",
        "",
        f"{Fore.WHITE}It is a period of civil war.",
        f"{Fore.WHITE}Rebel spaceships, striking",
        f"{Fore.WHITE}from a hidden base, have won",
        f"{Fore.WHITE}their first victory against",
        f"{Fore.WHITE}the evil Galactic Empire.",
        "",
        f"{Fore.WHITE}During the battle, Rebel spies",
        f"{Fore.WHITE}managed to steal secret plans",
        f"{Fore.WHITE}to the Empire's ultimate weapon,",
        f"{Fore.WHITE}the DEATH STAR, an armored",
        f"{Fore.WHITE}space station with enough power",
        f"{Fore.WHITE}to destroy an entire planet.",
    ]

    for line in intro_text:
        print(line.center(80))
        time.sleep(1)

def main():
    clear_console()
    star_wars_intro()

if __name__ == "__main__":
    main()
