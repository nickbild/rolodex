import math


input = "I LOVE WIN DO YOU TOO"


letters = {
    " ": 193,
    "A": 225,
    "B": 226,
    "C": 227,
    "D": 228,
    "E": 229,
    "F": 230,
    "G": 231,
    "H": 232,
    "I": 233,
    "J": 234,
    "K": 235,
    "L": 236,
    "M": 237,
    "N": 238,
    "O": 239,
    "P": 240,
    "Q": 241,
    "R": 242,
    "S": 243,
    "T": 244,
    "U": 245,
    "V": 246,
    "W": 247,
    "X": 248,
    "Y": 249,
    "Z": 250
}

def encode_block(block):
    d_binary = format(letters[block[3]], "08b")
    
    o1 = letters[block[0]]
    if d_binary[0:4] == "1110":
        o1 = o1 - 64
    elif d_binary[0:4] == "1100":
        o1 = o1 - 192

    o2 = letters[block[1]]
    if d_binary[3:6] == "110" or d_binary[3:6] == "010":
        o2 = o2 - 64
    if d_binary[3:6] == "101" or d_binary[3:6] == "001":
        o2 = o2 - 128
    if d_binary[3:6] == "100" or d_binary[3:6] == "000":
        o2 = o2 - 192

    o3 = letters[block[2]]
    if d_binary[6:8] == "10":
        o3 = o3 - 64
    if d_binary[6:8] == "01":
        o3 = o3 - 128
    if d_binary[6:8] == "00":
        o3 = o3 - 192

    return o1, o2, o3


input_len = math.floor(len(input) / 4)
leftover = len(input) % 4
output = []

for i in range(input_len):
    block = input[i * 4:i * 4 + 4]
    o1, o2, o3 = encode_block(block)
    output.append(o1)
    output.append(o2)
    output.append(o3)

if leftover > 0:
    for i in range(leftover):
        block = input[input_len * 4 + i]
        output.append(letters[block])

print(output)
