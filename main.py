from random import randrange
import os
from typing import IO
# comprehension 
def getRandomWord():
    try:
        names = []
        with open('./archivos/data.txt', 'r', encoding='utf-8') as f: 
            names = [name.replace('\n','') for name in f]
            randname = names[randrange(len(names))]
        return randname
    except IOError:
        print(IOError)
        return 0
    
def show(lives,letters,name):
    os.system('cls')
    print('Adivina la palabra!')
    print('vidas: ',lives)
    if len(letters) > 0:
        flag = True
        for l in name:
            for j in range(len(letters)):
                if l == letters[j]:
                    print(l,end=' ')
                    flag= False
                    break
            if flag:
                print('_',end=' ')
            flag = True
    else:
        for i in name:
            print('_', end=' ')
    print()
def hangman():
    pass

def main ():
    name = getRandomWord().upper()
    amountLetter = len(name)
    lives = 10
    letters=[]
    complete = False
    
    while (lives > 0):
        show(lives,letters,name)
        try:
            lett = input('Ingresa una letra: ')
            if len(lett) > 1 and (not lett.isalpha()):
                raise ValueError('Se tiene que ingresar solo una letra')
            
            if lett in name:
                letters.append(lett)
                if len(letters) == len(name):
                    show(lives,letters,name)
                    complete = True
                    break
            else:
                lives = lives - 1

            

        except ValueError as ve:
            print(ve)

    if complete:
        print('Ganaste! Haz adivinado!')
    else:
        print('HANGMAN')

if __name__ == "__main__" :
    main()