import random
class CLient:
    stateTransition = {}
    stateTransition['Reading Card'] = {'Success':'Reading Pin','Invalid':'Eject Card'}
    stateTransition['Reading Pin'] = {'Valid Pin':'Choosing Transaction','Invalid':'Eject Card'}
    stateTransition['Choosing Transaction'] = {'Transaction choosed':'Transaction Performed','Cancel':'Eject Card'}
    stateTransition['Transaction Performed'] = {'Another':'Choosing Transaction','Finish':'Eject Card'}
    stateTransition['Eject Card'] = {'Eject':'Idle'}
    stateTransition['Idle'] = {'Insert Card':'Reading Card'}
    message = ''
    isInserted = False
    isValid = False
    state = 'Idle'

    def doNextAction(self,nextAction):
        if nextAction in self.stateTransition[self.state]:
            self.state = self.stateTransition[self.state][nextAction]
            nextAction=''
            if(self.state == 'Reading Card'):
                options = list(self.stateTransition[self.state].keys())
                option = random.choice(options)
                print('Card Status' + option)
                self.doNextAction(options[0])
                return
            if(self.state == 'Reading Pin'):
                pin = '123' # input('Insert your pin')
                nextAction = 'Valid Pin'#Server.send(pin)
                self.doNextAction(nextAction)
                return
            if(self.state =='Choosing Transaction'):
                transaction = 'a' # input('Insert your next transaction')
                status = 'Success' # Server.send(transaction)
                print(status)
                self.doNextAction('Transaction choosed')
                return
            if (self.state == 'Transaction Performed'):
                nextAction = input('Insert "Another" or "Finish"')
                self.doNextAction(nextAction)
                return
            if (self.state == 'Eject Card'):
                print('Card Ejected')
                self.doNextAction('Eject')
                return

    def insertCard(self):
        self.isInserted = True
        self.state =  'Reading card'

    def validateCard(self):
        self.isValid= True

class Server:
    message = ''


atm = CLient()
while True:
    action = input() #Insert Card
    atm.doNextAction(action)



