#!/usr/bin/python3

from header import Header

class Verarbeiter:
    'Verarbeitung von Input und Output'

    inputVars = {'flags': None, 'source ip': None, 'dest ip': None}
    sourceIp = ''
    destIp = ''

    def userInput(self):
        for var in self.inputVars:
            print('Please provide ' + var)
            self.inputVars[var] = input()
            print('')

        self.sourceIp = self.inputVars['source ip']
        self.destIp = self.inputVars['dest ip']

        self.header1 = Header(self.inputVars['flags'])

    def printAll(self):
        props = ('version', 'ihl', 'tos', 'totalLength', 'kennung', 'flags', 'fragmentOffset', 'ttl', 'proto', 'chksum')
        outputStr = ''

        for index in range(len(props)):
            if hasattr(self.header1, props[index]):
                outputStr += str(getattr(self.header1, props[index])) + '-'

        outputStr += self.sourceIp + '-' + self.destIp
        print('Outpu:')
        print(outputStr)

    def calcHeaderFields(self):
        pass

if __name__ == '__main__':
    app = Verarbeiter()

    app.userInput()
    app.calcHeaderFields()
    app.printAll()