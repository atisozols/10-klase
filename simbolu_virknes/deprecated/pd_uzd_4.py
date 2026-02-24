sequence = "abbcbde"
target_position = 2
chosen = ""
tracker = 0

for char in sequence:
    if sequence.count(char) == 1:
        tracker += 1
        if tracker == target_position:
            chosen = char
            break

print(chosen)