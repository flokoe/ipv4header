#!/usr/bin/python3

class IPHeader:
    'header base'

    sip = None
    dip = None

    def __init__(self, version):
        self.version = version

class IPv4Header(IPHeader):
    'IPv4 header with all fields'

    # Decimal fields
    ihl = '5'
    tos = None
    totalLength = '20'
    kennung = None
    flags = None
    fragmentOffset = None
    ttl = None
    proto = None
    chksum = '0'

    # Binary fields
    versionBin = None
    ihlBin = None
    tosBin = '00011000'
    totalLengthBin = None
    kennungBin = '0000000000000000'
    flagsBin = None
    fragmentOffsetBin = '0000000000000'
    ttlBin = '00100000'
    protoBin = '00000000'
    chksumBin = '0000000000000000'
    sipBin = None
    dipBin = None

class IPv6Header(IPHeader):
    'IPv6 header and its fields'

    # Decimal fields
    trafficClass = None
    flowLabel = None
    payloadLength = None
    nextHeader = None
    hopLimit = None
