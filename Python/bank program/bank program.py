#projects

balance = 0

def show_balance():
    print('balance =', balance)
def deposit():
    amount = input('how much do you wish to deposit?: ')
    global balance
    while True:
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                print('deposit successful')
                balance = balance + amount
                break
            else :
                print('deposit failed')
                amount = input('how much do you wish to deposit?: ')
        else :
            print('deposit failed')
            amount = input('how much do you wish to deposit?: ')

def withdraw():
    wtdw = input('do you wish to withdraw?: ')
    global balance
    while True:
        if wtdw == 'y':
            wth = input('how much do you wish to withdraw?: ')
            if wth.isdigit():
                wth = int(wth)
                if wth > 0 and wth <= balance:
                    balance = balance - wth
                    print('withdraw successful')
                    print('balance =', balance)
                    break
                else :
                    print('withdraw failed')
            else :
                print('withdraw failed')
        elif wtdw == 'n':
            print('very well')
            break
        else :
            print('please enter valid choice')
            wtdw = input('do you wish to withdraw?: ')


print('bank program')
print('1. deposit')
print('2. show balance')
print('3. withdraw')
print('4. exit')
while True:
    choice = input('what do you wish to do?: ')
    if choice == '1':
        deposit()
        continue
    elif choice == '2':
        show_balance()
        continue
    elif choice == '3':
        withdraw()
        continue
    elif choice == '4':
        print('goodbye')
        break
    else :
        print('please enter valid choice')
        continue
