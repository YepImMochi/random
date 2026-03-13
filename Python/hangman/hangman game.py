#projects
#hangman

import random

words = ('orange','dream','apple','grape')

art = {0 : ('')
       , 1 : (' o ')
       , 2 : (' o ',
              ' | ')
       , 3 : (' o ',
              '/| ')
       , 4 : (' o ',
              '/|\\')
       , 5 : (' o ',
              '/|\\',
              '/  ')
       , 6 : (' o ',
              '/|\\',
              '/ \\')}

def display(wrong):
    print('**************************')
    for line in art[wrong]:
        print(line)
    print('**************************')

def dis_hint(hint):
    print(' '.join(hint))
def dis_answer(answer):
    print(' '.join(answer))
def main():
    answer = random.choice(words)
    hint = ['_']*len(answer)
    wrong = 0
    guessed = set()
    running = True
    while running:
        display(wrong)
        dis_hint(hint)
        guess = input('Guess a letter: ').lower()

        if len(guess) != 1:
            print('invalid')
            continue

        if guess in answer:
            for i in range(len(answer)):
                if guess == answer[i]:
                    hint[i] = guess
                    if guess in guessed:
                        print('already guessed')
                        continue
                    guessed.add(guess)
        else :
            wrong = wrong + 1
            if wrong == 6:
                display(wrong)
                print('YOU LOSE!')
                running = False
            continue

        if len(guessed) == len(answer):
            print('YOU WIN!')
            running = False

if __name__ == '__main__':
    main()