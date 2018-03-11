#!/usr/bin/python3

class Header:
    'IPv4 header with all fields'

    fieldsDec = {'version': 4, 'ihl': None, 'tos': 24, 'totalLength': None, 'kennung': 0, 'flags': None, 'fragmentOffset': 0, 'ttl': 32, 'proto': 0, 'chksum': 0, 'sourceip': None, 'destip': None}

    fieldsBin = {'version': '0100', 'ihl': '????', 'tos': '0110', 'totalLength': '????????????????', 'kennung': '0000000000000000', 'flags': '???', 'fragmentOffset': '0000000000000', 'ttl': '00100000', 'proto': '00000000', 'chksum': '0000000000000000', 'sourceip': None, 'destip': None}

    # def __init__(self, flags, sourceip, destip):
    #     self.fieldsDec['flags'] = flags
    #     self.fieldsDec['sourceip'] = sourceip
    #     self.fieldsDec['destip'] = destip