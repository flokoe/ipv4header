#!/usr/bin/python3

from headers import IPv4Header
from headers import IPv6Header
import re

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
        output = outputBin = ''
        output += str(getattr(header, 'version')) + '-'
        outputBin += bin(getattr(header, 'version'))[2:].zfill(4) + ' '

        # dont print hyphen at the end
        for field in fields:
            if field == 'dip':
                output += str(getattr(header, field))
            else:
                output += str(getattr(header, field)) + '-'

        if getattr(header, 'version') == 4:
            # get binary for each fields (ipv4)
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
            # get binary for each fields (ipv6)
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

        print('\nOutput:\n' + output + '\n\n' + outputBin)

    def printBin(self, binSplit):
        asciiOutput = ''
        if binSplit[0] == '0100' or binSplit[0] == '0110':
            # for each binary field
            for split in binSplit:
                # ignore flags field
                if split == '000':
                    asciiOutput += split + '-'
                # get ipv4 in ascii
                elif len(split) == 32:
                    ipDec = ''
                    # get 8 bit fields of 32 bit string
                    ipBin = re.findall('........', split)
                    for octet in ipBin:
                        # dont add dot at last element
                        if octet == ipBin[-1]:
                            ipDec += str(int(octet, 2))
                        else:
                            ipDec += str(int(octet, 2)) + '.'

                    # dont add hyphen at last element
                    if split == binSplit[-1]:
                        asciiOutput += ipDec
                    else:
                        asciiOutput += ipDec + '-'
                # get ipv6 in ascii
                elif len(split) == 128:
                    ipDec = ''
                    # get 8 bit fields of 32 bit string
                    ipBin = re.findall('................', split)
                    for hextet in ipBin:
                        # dont add dot at last element
                        if hextet == ipBin[-1]:
                            ipDec += hex(int(hextet, 2))[2:].zfill(4)
                        else:
                            ipDec += hex(int(hextet, 2))[2:].zfill(4) + '.'

                    # dont add hyphen at last element
                    if split == binSplit[-1]:
                        asciiOutput += ipDec
                    else:
                        asciiOutput += ipDec + '-'
                else:
                    asciiOutput += str(int(split, 2)) + '-'
        
            return asciiOutput
        else:
            return 'Please provide correct version.'

    def start(self):
        headerChoice = input('Please chose your header version (e.g. 4 or 6) or provide binary input [6]: ')
        if headerChoice == '' or headerChoice == '6':
            self.ipv6header1 = IPv6Header(6)
            self.userInput(self.ipv6header1, self.ipv6fields, self.ipv6defaults)
            self.printAll(self.ipv6header1, self.ipv6fields)
        elif headerChoice == '4':
            self.ipv4header1 = IPv4Header(4)
            self.userInput(self.ipv4header1, self.ipv4fields, self.ipv4defaults)
            self.printAll(self.ipv4header1, self.ipv4fields)
        elif re.search(r'[01 ]+', headerChoice):
            binarySplit = headerChoice.split(' ')
            print('\nOutput:')
            print(self.printBin(binarySplit))
        else:
            print('Please provide a correct version or binary input.')

if __name__ == '__main__':
    app = Verarbeiter()

    app.start()
