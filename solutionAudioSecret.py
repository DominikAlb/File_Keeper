
import wave
def func():
    song = wave.open("song_embedded.wav", mode='rb')
    frame_bytes = bytearray(list(song.readframes(song.getnframes())))
    #...
    song.close()
func()