import json

from PR_LAB_2.AppProtocol import App_Protocol


class Server:
    app_protocol = App_Protocol(("127.0.0.1", 20001), 'server')

    def handleOpperation(self,request):
        #return 'Handled'                                   # msg structure :  '{"method": "select", "parameters": "isValid The card id: "}'
        request = json.loads(msg)
        method = request['method']
        parameters = request['parameters'].split(' ')
        if method == 'check':
            if parameters[0] == 'isValidCard':
                return self.isValidCard(parameters[1])
            elif parameters[0] == 'isValidPIN':
                return self.isValidPIN(parameters[1])
        elif method == 'operation':
            if parameters[0] == 'amount':
                return self.getAmount()
            elif parameters[0] == 'transfer':
                return self.transfer(parameters[1],parameters[2])

    def isValidCard(self,card_info):
        if card_info == '123_321':
            return 'Success'
        else:
            return 'Invalid'
    def getAmount(self):
        return '$ 1 000 000'

    def transfer(self,destination,amount):
        return 'Transfered to ' + destination + ' $' + amount

    def isValidPIN(self, pin):
        if pin == '1111':
            return 'Success'
        else:
            return 'Invalid'

serverSide = Server()
msg = serverSide.app_protocol.recieve()
#msg = json.loads(msg)
while True:
    response = serverSide.handleOpperation(msg)
    serverSide.app_protocol.method = 'response'
    serverSide.app_protocol.parameters = response
    msg=serverSide.app_protocol.send()
    msg = json.dumps(msg)
    serverSide.app_protocol.method = None
    serverSide.app_protocol.parameters = None