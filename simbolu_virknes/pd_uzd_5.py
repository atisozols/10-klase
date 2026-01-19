data = "abccbaacz"
tracker = ""

for symbol in data:
    if symbol in tracker:
        print(symbol)
        break
    tracker += symbol