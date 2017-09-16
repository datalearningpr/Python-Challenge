

# test about base64 and wave

import base64, wave

message = open("data.txt", "rb").read()
indian = open('indian.wav', 'wb').write(base64.decodestring(message))


india = wave.open('indian.wav', 'r')
india_frames = india.readframes(india.getnframes())
india_swap = wave.open('indian_swap.wav', 'w')

# use oringinal settings
india_swap.setnchannels(india.getnchannels())
india_swap.setframerate(india.getframerate())
india_swap.setsampwidth(india.getsampwidth())

india_swap_frames = []
for i in range(0, len(india_frames), 2):

    india_swap_frames.append(india_frames[i+1])
    india_swap_frames.append(india_frames[i])

# frames are bytes!!!
india_swap_frames = bytes((india_swap_frames))
india_swap.writeframes(india_swap_frames)
india_swap.close()
india.close()





