#!/usr/bin/python3

class Header:
    'IPv4 header with all fields'

    # Decimal fields
    version = 4
    ihl = None
    tos = 24
    totalLength = None
    kennung = 0
    flags = None
    fragmentOffset = 0
    ttl = 32
    proto = 0
    chksum = 0
    sip = None
    dip = None

    # Binary fields
    versionBin = '0100'
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
