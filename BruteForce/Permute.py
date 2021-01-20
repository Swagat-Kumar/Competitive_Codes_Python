aux = []


def permute(arr, n, step=0):
    if step == n:
        if arr not in aux:
            aux.append(arr)
        print(arr)
    for i in range(step, n):
        copy = list(arr)
        copy[i], copy[step] = copy[step], copy[i]
        permute(copy, n, step+1)


permute([1, 2, 3, 4, 5, 6], 6)
print(len(aux))
