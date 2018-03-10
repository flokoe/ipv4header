#!/usr/bin/python3

class Header:
    'IPv4 header with all fields'

    fieldsDec = {'version': 4, 'ihl': None, 'tos': 24, 'totalLength': None, 'kennung': 0, 'flags': None, 'fragmentOffset': 0, 'ttl': 32, 'proto': 0, 'chksum': 0, 'sourceip': None, 'destip': None}
    fieldsBin = {}

    # def __init__(self, flags, sourceip, destip):
    #     self.fieldsDec['flags'] = flags
    #     self.fieldsDec['sourceip'] = sourceip
    #     self.fieldsDec['destip'] = destip