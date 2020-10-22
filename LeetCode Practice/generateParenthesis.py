
def generateParenthesis(n: int):
    if n <= 0:
        return
    listA = []

    def generate(s, o, c, n):
        if c == n and o == n:
            listA.append(s)
        else:
            if o > c:
                generate(s+')', o, c+1, n)
            if o < n:
                generate(s+'(', o+1, c, n)
    generate('', 0, 0, n)
    return listA


print(generateParenthesis(int(input())))
