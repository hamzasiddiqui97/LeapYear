##(b) If list ticket is equal to list lottery, print 'You won!'; else print
##'Better luck next time...'

ticket = input('Enter list by comma separated value (ie:[12,34]): ')
ticket = list(ticket.split(','))
print(ticket)
## saved value for lottery
lottery = '1235544'
## checking if input value is equal to lottery or not

for i in ticket:
    if i == lottery:
        print('You Won!')
