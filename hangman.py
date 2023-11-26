import random
from words import words
import string

def get_random_words(words):
    word = random.choice(words['data'])
    while '-' in word or ' ' in word:
        word = random.choice(words['data'])
    
    return word.upper()

def hangman():
    word = get_random_words(words)
    word_letters = set(word)
    alphabets = set(string.ascii_uppercase)
    used_letters = set()
    
    lives = 6
    
    while len(word_letters) > 0 and lives > 0 :
        print ('You have',lives,'lives left and you have used these letters : ',(' ').join(used_letters))
        
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print('Current Word : ',(' ').join(word_list) )

        user_letter = input("Guess a letter : ",).upper()
        if user_letter in alphabets - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            else:  
                lives -= 1
        
        elif user_letter in used_letters:
            print('Already used this letter')
        
        else:
            print('Invalid Character')
        
    if lives == 0:
        print("You died, The word is",word)
    else:
        print("You've guessed the word correctly",word)
    

hangman()
