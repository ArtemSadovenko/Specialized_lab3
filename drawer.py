import art
import termcolor
from art import *
from termcolor import *

def user_input():
    try:
        fonts = art_param.XLARGE_WIZARD_FONT
        text = str(input("Enter text: "))
        print("Enter font from: ")
        print(fonts)
        font = (input())
        if font not in fonts:
            raise ValueError
        color = input("Enter color: ")
        if color not in termcolor.COLORS:
            raise ValueError
        size = int(input("Enter size modifier: "))
        char = input("Enter char(type ' ' to skip): ")
    except ValueError:
        font = 'dotmatrix'
        text = "test"
        color = 'red'
        size = 1
        char = ' '

    return text, font, color, size, char

def draw(text, font, color, size, char):
    art = text2art(text, font)
    with open("text.txt", 'w') as file:
        file.write(art)
        
    res = ''

    with open('text.txt', 'r') as f:
        for line in f:
            output = "".join([size * c for c in line.strip()])
            
            for _ in range(size):
                res = res+output+'\n'

    if(char != ' '):
        modif = ''
        for letter in res:
            if letter == ' ' or letter == '\n':
                modif += letter
            else:
                modif += char
        res = modif

    return colored(res, color)

def __main__():
    text, font, color, size, char = user_input()
    res = draw(text, font, color, size, char)
    print(res)
    isSave = input("Save the art? (y/n)")
    if(isSave == 'y'):
        with open("text_out.txt", 'w') as f:
            f.write(res)


if __name__ == "__main__":
    __main__()