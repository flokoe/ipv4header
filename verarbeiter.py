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
        print('')
        outputStr = ''
        for var3 in self.header1.fieldsBin:
            outputStr += str(self.header1.fieldsBin[var3]) + '-'
        print(outputStr)

    def Dec2Bin(self):
        sourceip= self.header1.fieldsDec['sourceip'].split('.')
        destip= self.header1.fieldsDec['destip'].split('.')
        sourceIPBin = ''
        destIPBin = ''

        for index in range(len(sourceip)):
            sourceIPBin += bin(int(sourceip[index]))[2:].zfill(8)
            print(sourceIPBin)

        for index in range(len(destip)):
            destIPBin += bin(int(destip[index]))
            print(destIPBin)

        self.header1.fieldsBin['sourceip'] = sourceIPBin
        self.header1.fieldsBin['destip'] = destIPBin

    def calcIHL(self):
        bitLength = 0

        for field in self.header1.fieldsBin:
            bitLength += len(self.header1.fieldsBin[field])

        print('bits: ' + str(bitLength))
        ihlDec = bitLength // 32
        print('ihl dec: ' + str(ihlDec))

        self.header1.fieldsDec['ihl'] = ihlDec

    def calcTotalLength(self):
        bitLength = 0

        for field in self.header1.fieldsBin:
            bitLength += len(self.header1.fieldsBin[field])

        print(bitLength)
        totalLengthDec = bitLength // 8
        print(totalLengthDec)

        self.header1.fieldsDec['totalLength'] = totalLengthDec

    def calcHeaderFields(self):
        self.Dec2Bin()
        self.calcIHL()
        self.calcTotalLength()

if __name__ == '__main__':
    app = Verarbeiter()

    # Fühlt sich nicht richtig an, wie besser?
    app.userInput()
    app.calcHeaderFields()
    app.printAll()