import random
import datetime
from PR_LAB_2.AppProtocol import *

def checkhash(atm):
    try:
        with open('hashlog.txt', 'r+') as fh:
            if fh:
                a =fh.read()
                if a != atm.logfile and a != '':
                    return False
            return True
    except:
        with open('hashlog.txt','w+') as fh:
            return True
def log(atm):
    with open(atm.logfile, 'a+') as fh:
        fh.write('ATM: ' + atm.id + ' Date: ' + str(
            datetime.datetime.now()) + 'Action: ' + atm.state + ' Status: ' + atm.nextAction + '\n')
    # with open('hashlog.txt', 'w+') as hf:
    #         hf.write(str(fh.read()))
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
    id = '1111111111111'

    logfile = 'logfile.txt'
    def doNextAction(self,nextAction):
        if nextAction in self.stateTransition[self.state]:
            self.state = self.stateTransition[self.state][nextAction]
            nextAction=''
            if(self.state == 'Reading Card'):
                cardInfo = '123_321' #input('The card id: ')
                self.app_protocol.method = 'check'
                self.app_protocol.parameters = 'isValidCard ' + cardInfo
                self.nextAction = self.app_protocol.send()['parameters']
                print('CARD VALIDATION' + self.nextAction)
                log(self)
                self.doNextAction(self.nextAction) # options[0]  Success / Invalid
                return
            if(self.state == 'Reading Pin'):
                pin = input('Insert your pin')
                self.app_protocol.method = 'check'
                self.app_protocol.parameters = 'isValidPIN ' + pin
                nextAction = self.app_protocol.send()['parameters'] # 'Valid Pin' / Invalid Pin
                log(self)
                # with open(self.logfile, 'a+') as fh:
                #     fh.write('ATM: '+ self.id + ' Date: ' +str(datetime.datetime.now()) + 'Action: ' + self.state + ' Status: '+ nextAction + '\n')
                self.doNextAction(nextAction)
                return
            if(self.state =='Choosing Transaction'):
                transaction = input('Insert your next operation and arguments separated by SPACE')
                self.app_protocol.method = 'operation'
                self.app_protocol.parameters = transaction
                if transaction == 'Cancel':
                    with open(self.logfile, 'a+') as fh:
                        log(self)
                        # fh.write('ATM: ' + self.id + ' Date: ' + str(
                        #     datetime.datetime.now()) + 'State: ' + self.state + ' Action: Cancel\n')
                    self.doNextAction('Cancel')
                self.nextAction = self.app_protocol.send()['parameters']
                print(self.nextAction)
                log(self)
                # with open(self.logfile, 'a+') as fh:
                #     fh.write('ATM: '+ self.id + ' Date: ' +str(datetime.datetime.now()) + 'Action: ' + self.state + ' Response: '+ response + '\n')
                self.doNextAction('Transaction choosed')
                return
            if (self.state == 'Transaction Performed'):
                nextAction = input('Insert "Another" or "Finish"')
                log(self)
                # with open(self.logfile, 'a+') as fh:
                #     fh.write('ATM: '+ self.id + ' Date: ' +str(datetime.datetime.now()) + 'State: ' + self.state + ' Action: '+ nextAction + '\n')
                self.doNextAction(nextAction)
                return
            if (self.state == 'Eject Card'):
                print('Card Ejected. Thank you for using our services!')
                log(self)
                # with open(self.logfile, 'a+') as fh:
                #     fh.write('ATM: '+ self.id + ' Date: ' +str(datetime.datetime.now()) + 'State: ' + self.state + ' Action: Card Ejected\n')
                self.doNextAction('Eject')
                return


atm = CLient()
while True:
    # if not checkhash(atm):
    #     break
    action = input('Insert the card ( "Insert Card" )') #Insert Card
    atm.doNextAction(action)
# print('Hashes are not equal')



