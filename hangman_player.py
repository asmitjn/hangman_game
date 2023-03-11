import hangman_creator

hangman = hangman_creator.Hangman('/media/asmitjn/Important Data/Python files/Myfirstpythonproject/hangman_wordlist.txt')
hangman.choose_the_word()
hangman.fill_the_word_status()

while True:
    hangman.get_word_status()
    hangman.guess_the_letter()

    if(hangman.attempts_remaining==0):
        print('Out of attempts. Game Over!\n The word was {}'.format(hangman.chosen_word))
        break

    elif(hangman.chosen_word==''.join(hangman.word_status)):
        print('Hurray! You have won the game.')
        break