import serial


def hex_bytes_to_binary_string(hex_bytes):
  return ''.join(format(byte, '08b') for byte in hex_bytes)


ser = serial.Serial('/dev/ttyUSB0', 600, bytesize=serial.EIGHTBITS, parity=serial.PARITY_NONE,
                    stopbits=serial.STOPBITS_ONE, timeout=None, xonxoff=False, rtscts=False, dsrdtr=False)

ser.flushInput()
ser.flushOutput()

while True:
  data_raw = ser.read()
  # print(data_raw)
  print(int.from_bytes(data_raw, "little"))
