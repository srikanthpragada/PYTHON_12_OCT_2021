st = "how do you do"

chars = {}

for idx, ch in enumerate(st):
    if ch in chars:
        chars[ch].append(str(idx))
    else:
        chars[ch] = [str(idx)]

for ch, lst in sorted(chars.items()):
    print(ch, ",".join(lst))
