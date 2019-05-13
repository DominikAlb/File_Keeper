import wave

def func():
    song = wave.open("Krzysiu.wav", mode='rb')
    frame_bytes = bytearray(list(song.readframes(song.getnframes())))
    jpg = open('pic.jpg', 'rb')
    image_len = jpg.read()
    delta = 'END'
    bits  = []
    bits2 = []
    for i in delta:
        [bits.append(i) for i in bin(ord(i)).lstrip('0b').rjust(8, '0')]
    for i in image_len:
        [bits2.append(i) for i in bin(i).lstrip('0b').rjust(8, '0')]
    bits2.extend(bits)
    for i, bit in enumerate(bits2):
        frame_bytes[i] = (frame_bytes[i] & 254) | int(bit, 2)
    frame_modified = bytes(frame_bytes)
    with wave.open('song_embedded.wav', 'wb') as fd:
        fd.setparams(song.getparams())
        fd.writeframes(frame_modified)
    song.close()

func()