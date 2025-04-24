import serial


def hex_bytes_to_binary_string(hex_bytes):
  return ''.join(format(byte, '08b') for byte in hex_bytes)


ser = serial.Serial('/dev/ttyUSB0', 600, bytesize=serial.EIGHTBITS, parity=serial.PARITY_NONE,
                    stopbits=serial.STOPBITS_ONE, timeout=None, xonxoff=False, rtscts=False, dsrdtr=False)

ser.flushInput()
ser.flushOutput()

val = bytearray([53, 2, 81, 82, 19, 85, 150, 23, 25, 208, 1, 129, 180, 104, 243, 1, 233, 193, 97, 1, 37, 243, 180, 254, 254, 249])
ser.write(val)
