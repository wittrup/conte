import sys
from fds_const import commands as FMCC
from crcmod.predefined import mkCrcFun
crc = mkCrcFun('crc-16')


def query_yes_no(question, default="yes"):
    """Ask a yes/no question via raw_input() and return their answer.

    "question" is a string that is presented to the user.
    "default" is the presumed answer if the user just hits <Enter>.
        It must be "yes" (the default), "no" or None (meaning
        an answer is required of the user).

    The "answer" return value is True for "yes" or False for "no".
    """
    valid = {"yes": True, "y": True, "ye": True,
             "no": False, "n": False}
    if default is None:
        prompt = " [y/n] "
    elif default == "yes":
        prompt = " [Y/n] "
    elif default == "no":
        prompt = " [y/N] "
    else:
        raise ValueError("invalid default answer: '%s'" % default)

    while True:
        sys.stdout.write(question + prompt)
        choice = input().lower()
        if default is not None and choice == '':
            return valid[default]
        elif choice in valid:
            return valid[choice]
        else:
            sys.stdout.write("Please respond with 'yes' or 'no' "
                             "(or 'y' or 'n').\n")

num2cmd = {}
for cmd in FMCC:
    cn = crc(bytes(cmd, 'ascii'))
    if cn not in num2cmd:
        num2cmd[cn] = cmd
    else:
        print('CRC COLLISION', cmd, cn, num2cmd[cn])
        if not hasattr(sys.modules[__name__], 'continue_on_collision'): # Pseudo code, if not asked before
            if not query_yes_no('continue?', "no"):                         # then ask
                break                                                   # if said no, then

cmd2num = dict((v, k) for k, v in num2cmd.items())

print('num2cmd =', num2cmd)
print('cmd2num =', cmd2num)