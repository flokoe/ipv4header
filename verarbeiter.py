#!/usr/bin/python3

from headers import IPv4Header
from headers import IPv6Header

class Verarbeiter:
    'Verarbeitung von Input und Output'

    ipv4fields = {'ihl': 'ihl', 'tos': 'type of service', 'totalLength': 'totalLength', 'kennung': 'kennung', 'flags': 'flags', 'fragmentOffset': 'fragment offset', 'ttl': 'time to live', 'proto': 'protocol', 'chksum': 'chksum', 'sip': 'source IP', 'dip': 'destination IP'}
    ipv6fields = {'trafficClass': 'traffic class', 'flowLabel': 'flow label', 'payloadLength': 'payload length', 'nextHeader': 'next header', 'hopLimit': 'hop limit', 'sip': 'source IP', 'dip': 'destination IP'}

    ignoreList = ['ihl', 'totalLength', 'chksum']

    ipv6defaults = {'trafficClass': '24', 'flowLabel': '42', 'payloadLength': '0', 'nextHeader': '0', 'hopLimit': '32', 'sip': '2001:0db8:0000:08d3:0000:8a2e:0070:7344', 'dip': '2001:0db8:85a3:08d3:1319:8a2e:0370:7344'}
    ipv4defaults = {'tos': '24', 'kennung': '0', 'flags': '000', 'fragmentOffset': '0', 'ttl': '32', 'proto': '0', 'sip': '195.168.1.102', 'dip': '223.168.1.102'}

    def userInput(self, header, fields, defaults):
        for field in fields:
            # ignore specific fileds because they are always the same in an empty header
            if field not in self.ignoreList:
                eingabe = input('Please provide ' + fields[field] + ' [' + defaults[field] + ']: ')
                if eingabe == '':
                    setattr(header, field, defaults[field])
                else:
                    setattr(header, field, eingabe)

    def printAll(self, header, fields):
        output = ''
        outputBin = ''
        output += str(getattr(header, 'version')) + '-'
        outputBin += bin(getattr(header, 'version'))[2:].zfill(4) + ' '

        for field in fields:
            if field == 'dip':
                output += str(getattr(header, field))
            else:
                output += str(getattr(header, field)) + '-'

        if getattr(header, 'version') == 4:
            for field in fields:
                if field == 'ihl':
                    outputBin += bin(int(getattr(header, field)))[2:].zfill(4)
                elif field in ['tos', 'ttl', 'proto']:
                    outputBin += bin(int(getattr(header, field)))[2:].zfill(8)
                elif field in ['totalLength', 'kennung', 'chksum']:
                    outputBin += bin(int(getattr(header, field)))[2:].zfill(16)
                elif field == 'flags':
                    outputBin += getattr(header, field)
                elif field == 'fragmentOffset':
                    outputBin += bin(int(getattr(header, field)))[2:].zfill(13)
                elif field == 'sip' or field == 'dip':
                    v4IPBin = ''
                    v4IPSplit = getattr(header, field).split('.')
                    for split in v4IPSplit:
                        v4IPBin += bin(int(split))[2:].zfill(8)

                    outputBin += v4IPBin

                outputBin += ' '
        else:
            for field in fields:
                if field in ['trafficClass', 'nextHeader', 'hopLimit']:
                    outputBin += bin(int(getattr(header, field)))[2:].zfill(8)
                elif field == 'flowLabel':
                    outputBin += bin(int(getattr(header, field)))[2:].zfill(20)
                elif field == 'payloadLength':
                    outputBin += bin(int(getattr(header, field)))[2:].zfill(16)
                elif field == 'dip' or field == 'sip':
                    v6IPBin = ''
                    v6IPSplit = getattr(header, field).split(':')
                    for split in v6IPSplit:
                        v6IPBin += bin(int(split, 16))[2:].zfill(16)

                    outputBin += v6IPBin
            
                outputBin += ' '

        print('')
        print('Output:')
        print(output)
        print('')
        print(outputBin)

    def start(self):
        headerChoice = input('Please chose your header version (e.g. 4 or 6)[6]: ')
        if headerChoice == '' or headerChoice == '6':
            self.ipv6header1 = IPv6Header(6)
            self.userInput(self.ipv6header1, self.ipv6fields, self.ipv6defaults)
            self.printAll(self.ipv6header1, self.ipv6fields)
        elif headerChoice == '4':
            self.ipv4header1 = IPv4Header(4)
            self.userInput(self.ipv4header1, self.ipv4fields, self.ipv4defaults)
            self.printAll(self.ipv4header1, self.ipv4fields)
        else:
            print('Please provide a correct version.')

if __name__ == '__main__':
    app = Verarbeiter()

    app.start()
