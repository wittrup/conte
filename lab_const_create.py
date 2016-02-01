def cCodeNumberToC1C2(CodeNumber):
    C1 = ((CodeNumber % 790) // 10) + 48
    C2 = ((CodeNumber % 790) % 10) + 48 + 10 * (CodeNumber // 790)
    return chr(C1), chr(C2)

code2c1c2 = {}
c1c22code = {}
for code in range(6230):
    C1,C2 = cCodeNumberToC1C2(code)
    c1c2 = C1 + C2
    if c1c2 not in c1c22code:
        c1c22code[c1c2] = code
    else:
        print('collision', code, c1c2)
        break
    if code not in code2c1c2:
        code2c1c2[code] = c1c2
    else:
        print('code collision', code, c1c2)
        break

print('code2c1c2 =', code2c1c2)
print('c1c22code =', c1c22code)