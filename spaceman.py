import random
number_guesses = 5
letters_guessed = []



def load_word():
    f = open('words.txt', 'r')
    words_list = f.readlines()
    f.close()
    words_list = words_list[0].split(' ')
    secret_word = random.choice(words_list)
    return secret_word


def is_word_guessed(secret_word, letters_guessed):
    for i in secret_word: 
        if i not in letters_guessed:
            return False
    return True



def get_guessed_word(secret_word, letters_guessed):
    secret_word_list = list(secret_word)
    ans_list = ['_ ']*len(secret_word)
    index = 0
    for i in secret_word_list:
        if i in letters_guessed:
            ans_list[index] = i
        index += 1
    return(''.join(ans_list))



def is_guess_in_word(guess, secret_word):
    import string
    letters_not_guessed = string.ascii_letters
    letters_not_guessed_list = list(letters_not_guessed)
    for i in letters_not_guessed_list:
        if i in letters_guessed:
            letters_not_guessed_list.remove(i)
    return ''.join(letters_not_guessed_list)



def spaceman(secret_word):
  

    print('Welcome to the game, Hangman!')
    print('I am thinking of a word that is ',str(len(secret_word)), 'letters long.')
    print('-------------')

while (number_guesses > 0) and (is_guess_in_word(secret_word, letters_guessed) == False):
    print('You have ', str(number_guesses), 'guesses left.')
    print('Available letters: ', get_available_letters(letters_guessed))
    guess = (input('Please guess a letter: '))
    guesslower = guess.lower


secret_word = load_word()
spaceman(secret_word)
