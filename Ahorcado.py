from nis import match
from operator import le
import random
import os
from re import T

HANGMAN_MESSAGE_LOSEWIN=['''
 #     # ####### #     #     #       #######  #####  ####### 
  #   #  #     # #     #     #       #     # #     # #       
   # #   #     # #     #     #       #     # #       #       
    #    #     # #     #     #       #     #  #####  #####   
    #    #     # #     #     #       #     #       # #       
    #    #     # #     #     #       #     # #     # #       
    #    #######  #####      ####### #######  #####  ####### ''','''
    
db    db  .d88b.  db    db         db   d8b   db d888888b d8b   db     
`8b  d8' .8P  Y8. 88    88         88   I8I   88   `88'   888o  88     
 `8bd8'  88    88 88    88         88   I8I   88    88    88V8o 88     
   88    88    88 88    88         Y8   I8I   88    88    88 V8o88     
   88    `8b  d8' 88b  d88         `8b d8'8b d8'   .88.   88  V888     
   YP     `Y88P'  ~Y8888P'          `8b8' `8d8'  Y888888P VP   V8P ''']

HANGMAN_PICS = ['''   
    +---+
    |   |
        |
        |
        |
        |
    =========''', '''  
    +---+
    |   |
    O   |
        |
        |
        |
    =========''', ''' 
    +---+
    |   |
    O   |
    |   |
        |
        |
    =========''', '''  
    +---+
    |   |
    O   |
   /|   |
        |
        |
    =========''', '''  
    +---+
    |   |
    O   |
   /|\  |
        |
        |
    =========''', '''  
    +---+
    |   |
    O   |
   /|\  |
   /    |
        |
    =========''', '''  
    +---+
    |   |
    O   |
   /|\  |
   / \  |
        |
    =========''']

def enter_word():
    while True:
        try:
            letter = input("Ingresa una letra: ").strip().upper()
            assert letter.isalpha()
            try:
                assert len(letter)==1
                return letter
            except:
                print ("Solo se puede ingresar una letra")
        except:
                print("Solo puedes ingresar letras")


def processString5(txt):
    transTable = txt.maketrans("ÁÉÍÓÚ", "AEIOU")
    txt = txt.translate(transTable)
    return txt


def impresion(list,lifes):
    if lifes==6:
        print(list[0])
    if lifes==5:
        print(list[1])
    if lifes==4:
        print(list[2])
    if lifes==3:
        print(list[3])
    if lifes==2:
        print(list[4])
    if lifes==1:
        print(list[5])
    if lifes==0:
        print(list[6])


def read_data(filepath="./archivos/data.txt"):
    words = []
    try:    
        with open(filepath, "r", encoding="utf-8") as f:
            for line in f:
                words.append(line.strip().upper())
        return words
    except: 
        print("No se pudo abrir el archivo.")


def run():
    data = read_data(filepath="./archivos/data.txt")
    chosen_word1 = (random.choice(data))
    chosen_word = processString5(chosen_word1)
    chosen_word_list = [letter for letter in chosen_word]
    chosen_word_list_underscores = ["_"] * len(chosen_word_list)
    letter_index_dict = {}
    letter_uses = []
    life = 6
    
    for idx, letter in enumerate(chosen_word):
        if not letter_index_dict.get(letter): 
            letter_index_dict[letter] = []
        letter_index_dict[letter].append(idx)
    
    while True:
        os.system("clear") 
        if life<1:
            print(HANGMAN_MESSAGE_LOSEWIN[0])
            impresion(HANGMAN_PICS,life)
            print(f'            ¡ La palabra era: {chosen_word} !')
            break

        print("¡Adivina la palabra!")
        print("¡La palabra contiene "+str(len(chosen_word_list)) +" letras!")
        for element in chosen_word_list_underscores:
            print(element + " ", end="")
        print("\n")

        impresion(HANGMAN_PICS,life)
        
        print("Letras usadas " + str(letter_uses))
        print("\n")
        
        letter = enter_word()
        print("Resultado " + str(letter))
        letter_uses.append(letter)
        
        if letter in chosen_word_list:
            for idx in letter_index_dict[letter]:
                chosen_word_list_underscores[idx] = letter
        else:
            life -= 1

        if "_" not in chosen_word_list_underscores:
            os.system("clear") 
            print(HANGMAN_MESSAGE_LOSEWIN[1])
            print("\n")
            print(f'               ¡ La palabra era: {chosen_word} !')
            print("\n")
            break

if __name__ == '__main__':
    run()