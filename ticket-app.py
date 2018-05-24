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
    print('')
    if tickets_remaining == 1:
        print('There are currently only one ticket on sale!')
    else:
        print('There are currently {} tickets on sale!'.format(tickets_remaining))

def ticket_app(tickets_remaining, TICKET_PRICE):

    if check_availability():
        user_name = greet_user()
        print('')
        print('Welcome to the Tickets App, {}!'.format(user_name))
        check_number(tickets_remaining)

    print('')
    print('Thank you for using Tickets App! We hope to see you again!')
    print('')

ticket_app(tickets_remaining, TICKET_PRICE)
