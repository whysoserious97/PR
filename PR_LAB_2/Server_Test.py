import json

from PR_LAB_2.AppProtocol import App_Protocol


class Server:
    app_protocol = App_Protocol(("127.0.0.1", 20001), 'server')

    def handleOpperation(self,msg):
                                            # msg structure :  '{"method": "select", "parameters": "isValid The card id: "}'
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

    def isValidCard(self,card_info):
        if card_info == '123_321':
            return 'Success'
        else:
            return 'Invalid'
    def getAmount(self):
        return '$ 1 000 000'
    def isValidPIN(self, pin):
        if pin == '1111':
            return 'Success'
        else:
            return 'Invalid'

serverSide = Server()
while True:
    print('Server_Test')
    msg = serverSide.app_protocol.recieve()
    print('Recived msg')
    response = serverSide.handleOpperation(msg)
    print('SERVER RESPONSE',response)
    serverSide.app_protocol.method = 'response'
    serverSide.app_protocol.parameters = response
    serverSide.app_protocol.send()
    serverSide.app_protocol.method = None
    serverSide.app_protocol.parameters = None