text1 = "dog"
text2 = "cat"

if len(text1) != len(text2):
    print(False)
else:
    valid = True

    for symbol in text1:
        if text1.count(symbol) != text2.count(symbol):
            valid = False
            break

    print(valid)