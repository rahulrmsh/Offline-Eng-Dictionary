import json
import difflib
from difflib  import get_close_matches
import os

data = json.load(open("Dictionary - App 1/data.json"))

def closeMatchKey(wordKey):
    if(len(get_close_matches(wordKey, data.keys(), n = 1, cutoff = 0.6)) == 0 ):
        return 0
    closeMatch = get_close_matches(wordKey, data.keys(), n = 1, cutoff = 0.6)
    return closeMatch[0]

def printDefinition(wordKey):
    os.system('cls' if os.name == 'nt' else 'clear')
    print("\nWORD ENTERED : ",wordKey)
    for keys in data[wordKey]:
        print("\t*",keys)
    print("\n")
    
def wordInput():
    os.system('cls' if os.name == 'nt' else 'clear')
    wordKey = input("\nENTER WORD : ")
    print("-"*(13+len(wordKey)))
    wordKey = wordKey.lower()
    return  wordKey

def checkKey ( wordKey ):
    while(True):
        if(wordKey.isalpha()):
            if( wordKey in data):
                printDefinition(wordKey)
                break
            else : 
                print("\nINPUT WORD NOT RECOGNIZED")
                print('-'*25)
                closestKey = closeMatchKey(wordKey)
                if(closestKey == 0):
                    print("\n\n")
                    wordKey = wordInput()
                else:
                    print("DID YOU MEAN : ",closestKey)
                    response = input("Enter (Y/n) : ")
                    if(response.lower() == 'y'):
                        wordKey = closestKey
                    else:
                        wordKey = wordInput()
        else:
            print("\nINPUT WORD NOT RECOGNIZED")
            print('-'*25)
            tryKey = input("DO YOU WISH TO TRY AGAIN (Y/n) : ")
            if(tryKey.lower() == 'y'):
                wordKey = wordInput()
            else:
                break

wordKey = wordInput()
checkKey(wordKey)