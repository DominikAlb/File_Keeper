import wave
def func(Filename, Destination):
    song = wave.open(Filename, mode='rb')
    frame_bytes = bytearray(list(song.readframes(song.getnframes())))
    extracted = [frame_bytes[i] & 1 for i in range(len(frame_bytes))]
    buffer = []
    for i in range(0, len(extracted)-8, 8):
        chars = "".join([str(extracted[j + i]) for j in range(8)])
        s = chr(int(chars, 2))
        nextS = chr(int("".join([str(extracted[j + i + 8]) for j in range(8)]), 2))
        nextSS = chr(int("".join([str(extracted[j + i + 16]) for j in range(8)]), 2))
        if s == 'E' and nextS == 'N' and nextSS == 'D':
            break
        else:
            number = hex(int(chars, 2))[2:]
            if len(number) == 1:
                number = '0' + number
            buffer.extend(bytes.fromhex(number))
    image = open(Destination, 'wb')
    image.write(bytes(buffer))
    image.close()
    song.close()
