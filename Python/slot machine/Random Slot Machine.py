#first actual project ever : slot machine
#another thing is I'm not familiar with these gambling stuff, so I might some stuff abt them wrong, sry if I did
#advice and feedback is absolutely welcomed
import random

symbols = ['🍒','🍋','🍊']

def spin_row():
    while True:
        spin = input('do you wanna spin?: ')
        if spin == 'y':
            return [random.choice(symbols) for _ in range(3)]
        elif spin == 'n':
            print('I see . see you later then')
            return None
        else :
            print('please enter y or n')

def print_row(row):
    print(' '.join(row))
def payout(row,bet):
    if row[0]==row[1]==row[2]=='🍒':
        print('congrats you won 2x your bet')
        return bet*2
    elif row[0] == row[1] == row[2] == '🍋':
        print('congrats you won 3x your bet')
        return bet * 3
    elif row[0] == row[1] == row[2] == '🍊':
        print('congrats you won 5x your bet')
        return bet * 5
    else:
        print('oof you lost all your bet')
        return 0


def main():
    balance = 1000
    print('welcome to the slots machine')
    print('symbols include : 🍒 🍋 🍊')

    while balance > 0:
        print(f'current balance is ${balance:.2f}')

        bet = input('place your bet: ')
        if bet.isdigit():
            bet = int(bet)
            if bet <= balance and bet > 0:
                balance -= bet
                print(f'successfully placed your bet of ${bet}')
                row = spin_row()
                if row is None:
                    break
                else:
                    print('spinning...\n')
                    print_row(row)

                    get_payout = payout(row, bet)

                    balance += get_payout
            else :
                print('failed bet')
        else :
            print('please place an actual bet')



if __name__ == '__main__':
    main()