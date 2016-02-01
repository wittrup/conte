"""capfella - command parser for faulhaber lenze lecom A/B
"""

import re
from lab_const import c1c22code
from fds_const import cmd2num

pattern = r'(\x04?)(\d{1,3})\x02?([A-Za-z]+|[\x30-\x7F]{2})([HSO]?)([-\d\.\-A-Za-z]*)[\x03\x05]?([\x00-\xFF]?)'
keys = ['Lenze', 'Node', 'Code', 'Format', 'Argument', 'BCC']

def lenzeformat(value, fmt):
    if value is None:
        return value
    elif fmt is 'O':
        pass
    elif fmt is 'H':
        return int(value, 16)
    elif fmt is not 'S':
        return float(value)
    else:
        return value

def decode(line):
    match = re.match(pattern, line, re.I | re.U)
    if hasattr(match, 'group'):
        values = list(match.groups())
        values[0] = values[0] == '\x04'
        values = [None if s is '' else s for s in values]
        if values[0]: # Lenze
            values[2] = c1c22code[values[2]]
            values[4] = lenzeformat(values[4], values[3])

        else:
            values[2] = cmd2num[values[2]]
            values[4] = int(values[4]) if values[4] != None else None
        return values[0:3] + values[4:]

tests = ['99SO3', '1TEM', '128SWS2', '2U3000', '4HOSP5', '\x0409<>\x05', '\x041234\x05', '\x0412\x02<>214748.3647\x05B',
         '\x0412\x02<>-214748.3647\x05B', '\x0434\x0201H1AF\x05B', '\x0434\x0201Stei\x05B', '\x0434\x020195.2\x05B']

for test in tests:
    print(decode(test))

# class Capfella():
#     def __init__(self):