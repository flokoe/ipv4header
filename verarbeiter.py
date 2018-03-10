#!/usr/bin/python3

from header import Header

class Verarbeiter:
    'Verarbeitung von Input und Output'

    header1 = Header()
    inputVars = {'flags': 'flags', 'sourceip': 'source IP', 'destip': 'destination IP'}

    def userInput(self):
        for var in self.inputVars:
            print('Please provide ' + self.inputVars[var])
            self.header1.fieldsDec[var] = input()
            print('')

    def printAll(self):
        outputStr = ''

        for var2 in self.header1.fieldsDec:
            outputStr += str(self.header1.fieldsDec[var2]) + '-'

        print('Output:')
        print(outputStr)

    def calcHeaderFields(self):
        pass

if __name__ == '__main__':
    app = Verarbeiter()

    # Fühlt sich nicht richtig an, wie besser?
    app.userInput()
    app.calcHeaderFields()
    app.printAll()