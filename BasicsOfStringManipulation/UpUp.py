st = list(input())
ans = ''
word = ''
for s in st:
    if s.isalpha() or s == '[':
        word += s
    else:
        if len(word) != 0:
            if len(word) != 1:
                word = word[0].upper()+word[1:]
            else:
                word = word[0].upper()
        ans += word
        word = ''
        ans += s
if len(word) != 0:
    if len(word) != 1:
        word = word[0].upper()+word[1:]
    else:
        word = word[0].upper()
ans += word
print(ans)
