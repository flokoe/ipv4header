#!/usr/bin/python3

class Header:
    'IPv4 header with all fields'

    version = 4
    tos = 0
    kennung = 0
    fragmentOffset = 0
    ttl = 64
    proto = 0

    def __init__(self, flags):
        self.flags = flags