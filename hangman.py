# Problem Set 2, hangman.py

import random
import string

WORDLIST_FILENAME = "words.txt"


def load_words():
    print("Loading word list from file...")
    inFile = open(WORDLIST_FILENAME, 'r')
    line = inFile.readline()
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def choose_word(wordlist):
    return random.choice(wordlist)

wordlist = load_words()


# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program


def is_word_guessed(secret_word, letters_guessed):
    
    ls = list(secret_word)
    if letters_guessed == []:
        return False
    else:
        for i in letters_guessed:
            not_found = True
            for j in ls:
                if j==i:
                    not_found = False
                    break
            if not_found:
                return False
        return True

def get_guessed_word(secret_word, letters_guessed):
    
    ls = list(secret_word)
    lx = []
    lx.extend(['_ ']*len(ls))
    for i in range(len(ls)):
        for j in range(len(letters_guessed)):
            if ls[i] == letters_guessed[j]:
                lx[i]=ls[i]
    s = (''.join(lx))
    return s

def get_available_letters(letters_guessed):
    l1 = list(string.ascii_lowercase)
    l2 = l1[:]
    for i in range(len(l2)):
        for j in range(len(letters_guessed)):
            if l2[i] == letters_guessed[j]:
                l1.remove(l2[i])
                break
    s = ''.join(l1)
    return s
    
    

def hangman(secret_word):
    w = secret_word
    unique = []
    for char in w[::]:
        if char not in unique:
            unique.append(char)
    print('Welcome to Hangman!')
    print('I am thinking of a word that is' , len(w), 'letters long.')
    lg = []
    lg2 = []
    lg3 = []
    print(get_guessed_word(w,lg))
    guessl = 6
    warns = 3
    print('You have', warns,'warnings left.')
    print('_________________________________')
    while guessl >= 0 :
        if len(lg)==len(list(w)):
            print('Congratulations, you won! ')
            print('Your total score is:', guessl*len(unique))
            break
        print('You have',guessl,' guesses left.')
        print(get_available_letters(lg))
        print('____________________________________')
        x = str(input('Please guess a letter:'))
        y = str.lower(x)
        lg.append(y)
        lg2.append(y)
        if y in lg3:
            lg.pop()
            print('You have input the same letter again!')
            if warns == 0:
                print('You have zero warnings left. You will now lose a guess!')
                guessl -= 1
            else:
                warns -= 1
                print('You have', warns,'warnings left:', get_guessed_word(w,lg2))
        elif len(list(y)) >1:
            lg.pop()
            print('You have input more than one letter!')
            if warns == 0:
                print('You have zero warnings left. You will now lose a guess!')
                guessl -= 1
            else:
                warns -= 1
                print('You have', warns,'warnings left:', get_guessed_word(w,lg2))
        elif str.isalpha(x) == False:
            lg.pop()
            print(' Oops! That is not a valid letter.')
            if warns == 0:
                print('You have zero warnings left. You will now lose a guess!')
                guessl -= 1
            else:
                warns -= 1
                print('You have', warns,'warnings left:',get_guessed_word(w,lg2))
        
        elif is_word_guessed(w,lg) == True:
            print('Good guess!', get_guessed_word(w,lg2))
            
        elif is_word_guessed(w,lg) == False:
            if guessl == 1:
                print('Sorry, you ran out of guesses. The word was', w)
                break
            else:
                guessl -= 1
                lg.pop()
                print('Oops. That letter is not in my list.',get_guessed_word(w,lg2))
        lg3.append(y)



# =============================================================================
# HANGMAN WITH HINTS
# =============================================================================



def match_with_gaps(my_word, other_word):
    same = False
    if list(my_word) == []:
        return False
        
    else:
        v = my_word.replace(' ','')
        s = list(v)
        o = list(other_word)
        if len(s) == len(o):
            for i in range(len(s)):
                if s[i] != '_': 
                    if s[i]==o[i]:
                        same = True
                    else:
                        return False
                        break
                else:
                    u = o[i]
                    for j in range(len(s)):
                        if s[j]==u:
                            return False
                            break
    if same:
        return True
    else:
        return False


def show_possible_matches(my_word):
    w = []
    for g in wordlist:
        if match_with_gaps(my_word,g) == True:
            w.append(g)
    if w == [] or list(my_word) == []:
        return 'No matches found.'
    else:
        return w


def hangman_with_hints(secret_word):

    w = secret_word
    unique = []
    for char in w[::]:
        if char not in unique:
            unique.append(char)
    print('Welcome to Hangman!')
    print('I am thinking of a word that is' , len(w), 'letters long.')
    lg = []
    lg2 = []
    lg3 = []
    print(get_guessed_word(w,lg))
    guessl = 6
    warns = 3
    print('You have', warns,'warnings left.')
    print('_________________________________')
    while guessl >= 0 :
        if get_guessed_word(w,lg2) == w:
            print('Congratulations, you won! ')
            print('Your total score is:', guessl*len(unique))
            break
        print('You have',guessl,' guesses left.')
        print(get_available_letters(lg))
        print('____________________________________')
        x = str(input('Please guess a letter:'))
        y = str.lower(x)
        lg.append(y)
        lg2.append(y)
        if y in lg3 and y != '*':
            lg.pop()
            print('You have input the same letter again!')
            if warns == 0:
                print('You have zero warnings left. You will now lose a guess!')
                guessl -= 1
            else:
                warns -= 1
                print('You have', warns,'warnings left:', get_guessed_word(w,lg2))
        elif y == '*':
            lg.pop()
            k = get_guessed_word(w,lg2)
            print('Possible matches are,',show_possible_matches(k))
        elif len(list(y)) >1:
            lg.pop()
            print('You have input more than one letter!')
            if warns == 0:
                print('You have zero warnings left. You will now lose a guess!')
                guessl -= 1
            else:
                warns -= 1
                print('You have', warns,'warnings left:', get_guessed_word(w,lg2))
        elif str.isalpha(x) == False:
            lg.pop()
            print(' Oops! That is not a valid letter.')
            if warns == 0:
                print('You have zero warnings left. You will now lose a guess!')
                guessl -= 1
            else:
                warns -= 1
                print('You have', warns,'warnings left:',get_guessed_word(w,lg2))
        
        elif is_word_guessed(w,lg) == True:
            print('Good guess!', get_guessed_word(w,lg2))
            
        elif is_word_guessed(w,lg) == False:
            if guessl == 1:
                print('Sorry, you ran out of guesses. The word was', w)
                break
            else:
                guessl -= 1
                lg.pop()
                print('Oops. That letter is not in my list.',get_guessed_word(w,lg2))
        lg3.append(y)




if __name__ == "__main__":
    ##WITHOUT HINTS
#    secret_word = choose_word(wordlist)
#    hangman(secret_word)
    
    
        ##with hints
#    
#    secret_word = choose_word(wordlist)
#    hangman_with_hints(secret_word)


