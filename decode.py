import math


input = [244, 40, 233, 1, 41, 115, 161, 65, 116, 243, 244]


letters = {
    193 : " ",
    225 : "A",
    226 : "B",
    227 : "C",
    228 : "D",
    229 : "E",
    230 : "F",
    231 : "G",
    232 : "H",
    233 : "I",
    234 : "J",
    235 : "K",
    236 : "L",
    237 : "M",
    238 : "N",
    239 : "O",
    240 : "P",
    241 : "Q",
    242 : "R",
    243 : "S",
    244 : "T",
    245 : "U",
    246 : "V",
    247 : "W",
    248 : "X",
    249 : "Y",
    250 : "Z"    
}

def decode_block(block):
    o1_binary = format(block[0], "08b")
    o2_binary = format(block[1], "08b")
    o3_binary = format(block[2], "08b")

    a = block[0]
    if o1_binary[0:3] == "101":
        a = a + 64
        d = "1110"
    elif o1_binary[0:3] == "000" or o1_binary[0:3] == "001":
        a = a + 192
        d = "1100"
    else:
        d = "1111"

    b = block[1]
    if o2_binary[0:3] == "101":
        b = b + 64
        d += "10"
    elif o2_binary[0:3] == "011" or o2_binary[0:3] == "010":
        b = b + 128
        d += "01"
    elif o2_binary[0:3] == "001" or o2_binary[0:3] == "000":
        b = b + 192
        d += "00"
    else:
        d += "11"
  
    c = block[2]
    if o3_binary[0:3] == "101":
        c = c + 64
        d += "10"
    elif o3_binary[0:3] == "011" or o3_binary[0:3] == "010":
        c = c + 128
        d += "01"
    elif o3_binary[0:3] == "001" or o3_binary[0:3] == "000":
        c = c + 192
        d += "00"
    else:
        d += "11"

    d = int(d, 2)
    if d == 255:
        d = 0

    return a, b, c, d


input_len = math.floor(len(input) / 3)
leftover = len(input) % 3
output = []

# Decode blocks of 3 bytes.
for i in range(input_len):
    block = input[i * 3:i * 3 + 3]
    a, b, c, d = decode_block(block)
    output.append(a)
    output.append(b)
    output.append(c)
    output.append(d)

# Decode any remainder.
if leftover > 0:
    for i in range(leftover):
        block = input[input_len * 3 + i]
        output.append(block)

# Print the decoded output.
for l in output:
    if l == 0:
        continue
    print(letters[l], end="")
print()
