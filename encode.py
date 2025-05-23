import math


input = "1234567890 , THIS IS A TEST."


letters = {
    " ": 193,
    "'": 199,
    ",": 204,
    ".": 206,
    "0": 208,
    "1": 209,
    "2": 210,
    "3": 211,
    "4": 212,
    "5": 213,
    "6": 214,
    "7": 215,
    "8": 216,
    "9": 217,
    "?": 223,
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


def calculate_checksum(packet_bytes):
    """
    Given a packet as a list of integers (0–255), returns the checksum byte.
    Packet format is assumed to be:
      [53, 2, payload..., 254, 254]
    """
    if len(packet_bytes) < 5:
        raise ValueError("packet too short")
    if packet_bytes[0] != 53 or packet_bytes[1] != 2:
        raise ValueError("invalid header")
    if packet_bytes[-1] != 254 or packet_bytes[-2] != 254:
        raise ValueError("invalid trailer")

    # strip off header (2 bytes) and trailer (2 bytes of 254)
    payload = packet_bytes[2:-2]

    S = sum(payload)
    # two's-complement mod 256, then add the constant 4
    checksum = (-S + 4) & 0xFF
    
    return checksum


def encode_block(block):
    d_binary = format(letters[block[3]], "08b")
    
    o1 = letters[block[0]]
    if d_binary[0:4] == "1110":
        o1 = o1 - 64
    elif d_binary[0:4] == "1101":
        o1 = o1 - 128
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

# Process the input in blocks of 4 characters.
for i in range(input_len):
    block = input[i * 4:i * 4 + 4]
    o1, o2, o3 = encode_block(block)
    output.append(o1)
    output.append(o2)
    output.append(o3)

# Handle the leftover characters.
if leftover > 0:
    for i in range(leftover):
        block = input[input_len * 4 + i]
        output.append(letters[block])

# Print just the encoded data.
print(output)

# Add the rest of the packet.
full_output = output.copy()
full_output.insert(0, 2)
full_output.insert(0, 53)
full_output.append(254)
full_output.append(254)
full_output.append(calculate_checksum(full_output))

print("Full output: ", full_output)
