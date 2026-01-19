# Visi mainīgie satur simbolus vienādā skaitā

# text = "abacbc"
# seen = ""
# for symbol in text:
#     if symbol not in seen:
#         seen += symbol

# count_ref = text.count(seen[0])
# valid = True

# for symbol in seen:
#     if text.count(symbol) != count_ref:
#         valid = False
#         break

# if valid:
#     print("Yes")
# else:
#     print("No")


data = "abacbc"
group = ""
for item in data:
    if item not in group:
        group += item

reference = data.count(group[0])
check = True

for item in group:
    if data.count(item) != reference:
        check = False
        break

if check:
    print("Yes")
else:
    print("No")


# modified

text = "abacbc"
seen = ""
for symbol in text:
    if symbol not in seen:
        seen += symbol

count_ref = text.count(seen[0])
differences = 0

for symbol in seen:
    if text.count(symbol) != count_ref:
        differences += 1

if differences <= 1:
    print("Yes")
else:
    print("No")


data = "abacbc"
group = ""
for item in data:
    if item not in group:
        group += item

count1 = data.count(group[0])
differences = 0

for item in group:
    if data.count(item) != count1:
        differences += 1

if differences <= 1:
    print("Yes")
else:
    print("No")

