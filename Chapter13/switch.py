__author__ = 'steve1281'

def PrintBlue():
    print('You chose blue!\r\n')


def PrintRed():
    print('You chose red!\r\n')


def PrintOrange():
    print('You chose orange!\r\n')


def PrintYellow():
    print('You chose yellow!\r\n')


ColorSelect = {
    0: PrintBlue,
    1: PrintRed,
    2: PrintOrange,
    3: PrintYellow,
}

Selection = 0

while (Selection != 4):
    print("0. Blue")
    print("1. Red")
    print("2. Orange")
    print("3. Yellow")
    print("4. Quit")

    Selection = int(input("Select a color option: "))

    if (Selection >= 0) and (Selection < 4):
        ColorSelect[Selection]()


