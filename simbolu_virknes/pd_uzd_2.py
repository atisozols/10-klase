data = "fly me to the moon"
chunks = data.split()

if len(chunks) > 0:
    measure = len(chunks[len(chunks) - 1])
    print(measure)
else:
    print(0)




data = "fly me to the moon"
chunks = data.split()
track = 0

for piece in chunks:
    track = len(piece)

if track > 0:
    print(track)
else:
    print(0)
