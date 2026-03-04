import random

with open('input.txt', 'r', encoding='utf-8') as f:
    s = f.read()

spaces = ['\u00A0', '\u1680', '\u2000', '\u2001', '\u2002', '\u2003', '\u2004', '\u2005', '\u2006', '\u2007', '\u2008', '\u2009', '\u200A', '\u202F', '\u205F', '\u3000']
output = ''.join(random.choice(spaces) if c == ' ' else c for c in s)

with open('output.txt', 'w', encoding='utf-8') as f:
    f.write(output)