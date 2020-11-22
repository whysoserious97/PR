import random
from PR_LAB_2.AppProtocol import *
class CLient:
    stateTransition = {}
    stateTransition['Reading Card'] = {'Success':'Reading Pin','Invalid':'Eject Card'}
    stateTransition['Reading Pin'] = {'Success':'Choosing Transaction','Invalid':'Eject Card'}
    stateTransition['Choosing Transaction'] = {'Transaction choosed':'Transaction Performed','Cancel':'Eject Card'}
    stateTransition['Transaction Performed'] = {'Another':'Choosing Transaction','Finish':'Eject Card'}
    stateTransition['Eject Card'] = {'Eject':'Idle'}
    stateTransition['Idle'] = {'Insert Card':'Reading Card'}
    message = ''
    state = 'Idle'
    app_protocol = App_Protocol(("127.0.0.1", 20001),'client')


    def doNextAction(self,nextAction):
        if nextAction in self.stateTransition[self.state]:
            self.state = self.stateTransition[self.state][nextAction]
            nextAction=''
            if(self.state == 'Reading Card'):
                cardInfo = '123_321' #input('The card id: ')
                self.app_protocol.method = 'check'
                self.app_protocol.parameters = 'isValidCard ' + cardInfo
                status = self.app_protocol.send()['parameters']
                print('CARD VALIDATION' + status)

                self.doNextAction(status) # options[0]  Success / Invalid
                return
            if(self.state == 'Reading Pin'):
                pin = input('Insert your pin')
                self.app_protocol.method = 'check'
                self.app_protocol.parameters = 'isValidPIN ' + pin
                nextAction = self.app_protocol.send()['parameters'] # 'Valid Pin' / Invalid Pin
                self.doNextAction(nextAction)
                return
            if(self.state =='Choosing Transaction'):
                transaction = input('Insert your next operation and arguments separated by SPACE')
                self.app_protocol.method = 'operation'
                self.app_protocol.parameters = transaction
                if transaction == 'Cancel':
                    self.doNextAction('Cancel')
                response = self.app_protocol.send()['parameters']
                print(response)
                self.doNextAction('Transaction choosed')
                return
            if (self.state == 'Transaction Performed'):
                nextAction = input('Insert "Another" or "Finish"')
                self.doNextAction(nextAction)
                return
            if (self.state == 'Eject Card'):
                print('Card Ejected. Thank you for using our services!')
                self.doNextAction('Eject')
                return


atm = CLient()
while True:
    action = input('Insert the card ( "Insert Card" )') #Insert Card
    atm.doNextAction(action)



