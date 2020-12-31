a = input()
b = input()
printed = False
if len(a) != len(b):
    print("NO")
    printed = True
if(a == b):
    printed = True
    print("YES")
else:
    for i in range(len(a)-1, -1, -1):
        a_extract = a[i]
        b_extract = b[i]
        extract = ''
        if(a_extract < b_extract):
            amount = ord(b_extract)-ord(a_extract)
            extract = ''.join(chr(ord(letter)+amount) for letter in a[:i+1])
            a = extract+a[i+1:]
        else:
            if (a_extract > b_extract):
                print("NO")
                printed = True
                break
if(not printed):
    if(a != b):
        print("NO")
    else:
        print("YES")
