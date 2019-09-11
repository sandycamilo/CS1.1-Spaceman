import random
letters_guessed = []


def load_word():
    '''
    A function that reads a text file of words and randomly selects one to use as the secret word
        from the list.
    Returns: 
           string: The secret word to be used in the spaceman guessing game
    '''
    f = open('words.txt', 'r')
    words_list = f.readlines()
    f.close()
    
    words_list = words_list[0].split(' ') #comment this line out if you use a words.txt file with each word on a new line
    secret_word = random.choice(words_list)
    return secret_word

def is_word_guessed(secret_word, letters_guessed):
    '''
    A function that checks if all the letters of the secret word have been guessed.
    Args:
        secret_word (string): the random word the user is trying to guess.
        letters_guessed (list of strings): list of letters that have been guessed so far.
    Returns: 
        bool: True only if all the letters of secret_word are in letters_guessed, False otherwise
    '''
    # TODO: Loop through the letters in the secret_word and check if a letter is not in lettersGuessed
    for letters in secret_word:
        if letters in letters_guessed:
            return True
        else:
            return False 


def get_guessed_word(secret_word, letters_guessed):
    '''
    A function that is used to get a string showing the letters guessed so far in the secret word and underscores for letters that have not been guessed yet.
    Args: 
        secret_word (string): the random word the user is trying to guess.
        letters_guessed (list of strings): list of letters that have been guessed so far.
    Returns: 
        string: letters and underscores.  For letters in the word that the user has guessed correctly, the string should contain the letter at the correct position.  For letters in the word that the user has not yet guessed, shown an _ (underscore) instead.
    '''

    #TODO: Loop through the letters in secret word and build a string that shows the letters that have been guessed correctly so far that are saved in letters_guessed and underscores for the letters that have not been guessed yet
    secret_word_list = list(secret_word)
    ans_list = ['_ ']*len(secret_word)
    index = 0
    for letters in secret_word_list:
        if letters in letters_guessed:
            ans_list[index] = letters
        index += 1
    return print(''.join(ans_list))



def is_guess_in_word(guess, secret_word):
    '''
    A function to check if the guessed letter is in the secret word
    Args:
        guess (string): The letter the player guessed this round
        secret_word (string): The secret word
    Returns:
        bool: True if the guess is in the secret_word, False otherwise
    '''
    #TODO: check if the letter guess is in the secret word
    
    if guess in secret_word:
        return True
    else:
        return False
    
    # import string
    # letters_not_guessed = string.ascii_letters
    # letters_not_guessed_list = list(letters_not_guessed)
    # for i in letters_not_guessed_list:
    #     if i in letters_guessed:
    #         letters_not_guessed_list.remove(i)
    # return ''.join(letters_not_guessed_list)




def spaceman(secret_word):
    '''
    A function that controls the game of spaceman. Will start spaceman in the command line.
    Args:
      secret_word (string): the secret word to guess.
    '''
    print('Welcome aboard!')
    print("Let's play!")

    number_guesses = 7
    letters_guessed = []

    print (secret_word)


    while (number_guesses > 0) and (is_word_guessed(secret_word, letters_guessed) == False):
        print('You have ', str(number_guesses), 'guesses left.')
        get_guessed_word(secret_word,letters_guessed)

        # print('Available letters: ', get_available_letters(letters_guessed))
        guess = (input('Please guess a letter: '))

        if not (guess.isalpha and len(guess) == 1):
            print (":(")
            #guess = (input('Try again: '))

        elif (guess in letters_guessed):
            print("Oops, you have already used this letter.")
            #guess = (input('Another letter:'))

        else:

            letters_guessed += guess

            if is_guess_in_word(guess, secret_word):
                print("yay")
                get_guessed_word(secret_word,letters_guessed)

            else:
                number_guesses = number_guesses - 1
                print('oh no, try again!')
                get_guessed_word(secret_word,letters_guessed)


    if is_word_guessed(secret_word, letters_guessed) == True:
        print ("Congratulations, you're a star")
    else: print ("You ran out of tries. You are still a star though ;) ")


        

    #TODO: show the player information about the game according to the project spec

    #TODO: Ask the player to guess one letter per round and check that it is only one letter

    #TODO: Check if the guessed letter is in the secret or not and give the player feedback

    #TODO: show the guessed word so far

    #TODO: check if the game has been won or lost



#These function calls that will start the game
secret_word = load_word()
spaceman(secret_word)