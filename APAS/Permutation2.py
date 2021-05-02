class Solution:
    def permuteUnique(self, nums):
        aux = {}

        def resolve(a=nums, step=0):
            if step == len(a):
                if tuple(a) not in aux:
                    aux[tuple(a)] = True
            for i in range(step, len(a)):
                copy = list(a)
                copy[i], copy[step] = copy[step], copy[i]
                resolve(copy, step+1)
        resolve()
        return list(aux.keys())
