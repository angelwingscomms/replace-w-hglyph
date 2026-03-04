mapping = {
    "a": "а",
    "c": "с",
    "d": "ԁ",
    "e": "е",
    "g": "ց",
    "h": "һ",
    "i": "і",
    "j": "ј",
    # "k": "κ",
    "n": "ո",
    "o": "о",
    "p": "р",
    "q": "ԛ",
    "s": "ѕ",
    "u": "ս",
    "v": "ν",
    "x": "х",
    "y": "у",
    "A": "А",
    "B": "В",
    "C": "С",
    "D": "Ꭰ",
    "E": "Е",
    "F": "Ϝ",
    "G": "Ԍ",
    "I": "І",
    "J": "Ј",
    "K": "Κ",
    "L": "Լ",
    "M": "М",
    "N": "Ν",
    "O": "О",
    "P": "Р",
    "Q": "Ԛ",
    # "R": "Ꭱ",
    "S": "Ѕ",
    "T": "Τ",
    "U": "Ս",
    "V": "Ѵ",
    # "W": "Ѡ",
    "X": "Х",
    "Z": "Ζ",
}

with open("input.txt", "r", encoding="utf-8") as f:
    text = f.read()

output = "".join(mapping.get(c, c) for c in text)

with open("output.txt", "w", encoding="utf-8") as f:
    f.write(output)
