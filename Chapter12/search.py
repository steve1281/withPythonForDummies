__author__ = 'steve1281'

Colors = ["Red","Orange","Yellow","Green","Blue",]
ColorSelect = ""

while str.upper(ColorSelect) != "QUIT":
    ColorSelect = input("Please enter a color name: ")
    if (Colors.count(ColorSelect) >= 1):
        print("The color exists in the list!")
    elif (str.upper(ColorSelect) != "QUIT"):
        print("The color ",ColorSelect," does not exist in the list.")

