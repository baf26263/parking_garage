class Garage():

    def __init__(self):
        self.tickets_available = 50
        self.max_capacity = 50
        self.currentTicket = {}

    def takeTicket(self):
        self.tickets_available -= 1
        self.max_capacity -= 1

    def payForParking(self):
        payment = print('Please pay the flat rate of $10')
        if payment != '':
            print('Thank you for your payment! You have 15 minutes to leave the garage or an additional payment will be needed to leave.')
            self.tickets_available += 1
            self.current_ticket['paid'] = True
    
    def leaveGarage(self):
        payment = print('Please make a payment to leave.')
        if payment != '':
            print('Thank You, have a nice day!')
        self.tickets_available += 1
        self.max_capacity += 1

    def ticketsLeft(self):
        print(self.tickets_available)

    def spotsLeft(self):
        print(self.max_capacity)

parking = Garage()

def run():
    while True:
        response = input('Please enter: take ticket, pay for parking, leave garage, how many tickets left, how many spots left, or quit: ')
        if response.lower() == 'quit':
            print('Come back when you are ready to enter/leave')
            break
        elif response.lower() == 'how many tickets left':
            parking.ticketsLeft()
        elif response.lower() == 'how many spots left':
            parking.spotsLeft()
        elif response.lower() == 'take ticket':
            parking.takeTicket()
        elif response.lower() == 'pay for parking':
            parking.payForParking()
        elif response.lower() == 'leave garage':
            parking.leaveGarage()
            break
        else:
            print('\nPlease enter one of the options listed.')

run()