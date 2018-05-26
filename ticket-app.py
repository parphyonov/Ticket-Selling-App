import os

os.system('clear')

TICKET_PRICE = 10

tickets_remaining = 100

def greet_user():
    user_name = input('Greetings from Tickets App. What is your name? ')
    return user_name

def check_availability():
    if tickets_remaining == 0:
        print('We\'re sorry. The tickets for this performance are completely sold out!')
        print('Give us another try in a couple of days, and maybe some tickets will be returned to become available to you!')
        print('')
        return False
    else:
        return True

def check_number(tickets_remaining):
    if tickets_remaining == 1:
        return 'ticket'
    else:
        return 'tickets'

def apply_ticket_request(tickets_remaining, TICKET_PRICE, user_name):
    while True:
        print('')
        try:
            request = int(input('How many tickets you would like to buy? '))
        except ValueError:
            print('')
            print('It looks like you provided something non-numerical. Please, provide a number under {} and above 0.'.format(tickets_remaining))
            should_exit = input('Or enter EXIT to leave the app: ')
            if should_exit.lower() == 'exit':
                break
            else:
                continue
        else:
            if request > tickets_remaining:
                print('')
                print('We are unable to accommodate your request. We are under the amount of tickets you have requested. We currently have {} {}.'.format(tickets_remaining, check_number(tickets_remaining)))
            elif request == 0:
                print('')
                print('We would be happy to be able to sell nothing with our margin, but unfortunately you need to inquire at least one ticket.')
            elif request < 0:
                print('')
                print('There cannot be a negative amount of tickets. Maybe, in parallel universe... But surely, next time.')
            else:
                print('')
                print('You are about to purchase {} {}.'.format(request, check_number(request)))
                print('It is going to cost you {} usd.'.format(request * TICKET_PRICE))
                print('')
                confirmation_of_purchase = input('Would you like to confirm? (Y/n) ')
                if confirmation_of_purchase.lower() != 'y':
                    continue
                else:
                    print('')
                    print('Thank you very much for your purchase, {}. See you at the performance!'.format(user_name))
                    return tickets_remaining - request

def ticket_app(tickets_remaining, TICKET_PRICE):

    if check_availability():
        user_name = greet_user()
        print('')
        print('Welcome to Tickets App, {}!'.format(user_name))
        print('')
        if tickets_remaining == 1:
            print('There are currently only one ticket on sale!')
        else:
            print('There are currently {} tickets on sale!'.format(tickets_remaining))

        tickets_remaining = apply_ticket_request(tickets_remaining, TICKET_PRICE, user_name)

    print('')
    print('Thank you for using Tickets App, {}! We hope to see you again!'.format(user_name))
    print('')

ticket_app(tickets_remaining, TICKET_PRICE)
