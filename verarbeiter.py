#!/usr/bin/python3

from header import Header

class Verarbeiter:
    'Verarbeitung von Input und Output'

    # Create header obj
    header1 = Header()

    def userInput(self):
        inputVars = {'flags': 'flags', 'sip': 'source IP', 'dip': 'destination IP'}

        for var in inputVars:
            print('Please provide ' + inputVars[var])
            if var == 'flags':
                inpu = input()
                self.header1.flags = inpu
                self.header1.flagsBin = inpu
            else:
                inpu2 = input()
                setattr(self.header1, var, inpu2)
            print('')

    def dec2bin(self):
        fields = ['sip', 'dip']

        for index in fields:
            if index == 'sip':
                binList = self.header1.sip.split('.')
            else:
                binList = self.header1.dip.split('.')
            binNum = ''

            for index2 in binList:
                binNum += bin(int(index2))[2:].zfill(8)
            
            if index == 'sip':
                self.header1.sipBin = binNum
            else:
                self.header1.dipBin = binNum

    def calcIHL(self):
        binLength = 0
        fields = ('versionBin', 'tosBin', 'kennungBin', 'flagsBin', 'fragmentOffsetBin', 'ttlBin', 'protoBin', 'chksumBin', 'sipBin', 'dipBin')

        for index in range(len(fields)):
            binLength += len(getattr(self.header1, fields[index]))

        ihlDec = (binLength + 24) // 32
        self.header1.ihl = ihlDec
        self.header1.ihlBin = bin(ihlDec)[2:].zfill(4)

    def calcTotalLenght(self):
        binLength = 0
        fields = ('versionBin', 'tosBin', 'kennungBin', 'flagsBin', 'fragmentOffsetBin', 'ttlBin', 'protoBin', 'chksumBin', 'sipBin', 'dipBin')

        for index in range(len(fields)):
            binLength += len(getattr(self.header1, fields[index]))

        totalLengthDec = (binLength + 24) // 8
        self.header1.totalLength = totalLengthDec
        self.header1.totalLengthBin = bin(totalLengthDec)[2:].zfill(16)

    def printAll(self):
        outputStr = ''
        outputStr2 = ''
        fields = ('version', 'ihl', 'tos', 'totalLength', 'kennung', 'flags', 'fragmentOffset', 'ttl', 'proto', 'chksum', 'sip', 'dip')
        fieldsBin = ('versionBin', 'ihlBin', 'tosBin', 'totalLengthBin', 'kennungBin', 'flagsBin', 'fragmentOffsetBin', 'ttlBin', 'protoBin', 'chksumBin', 'sipBin', 'dipBin')

        for field in fields:
            if field != 'dip':
                outputStr += str(getattr(self.header1, field)) + '-'
            else:
                outputStr += str(getattr(self.header1, field))

        for field2 in fieldsBin:
            if field2 != 'dipBin':
                outputStr2 += str(getattr(self.header1, field2)) + '-'
            else:
                outputStr2 += str(getattr(self.header1, field2))

        print('Output:')
        print(outputStr)
        print('')
        print(outputStr2)

if __name__ == '__main__':
    app = Verarbeiter()

    app.userInput()
    app.dec2bin()
    app.calcIHL()
    app.calcTotalLenght()
    app.printAll()
