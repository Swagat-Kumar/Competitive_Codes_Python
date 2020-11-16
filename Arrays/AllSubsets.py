class Solution:
    def subsets(self, nums):
        listA = []

        def visit(current=0, aux=[]):
            if current == len(nums):
                listA.append(aux)
                return
            copy = list(aux)
            copy.append(nums[current])
            scopy = list(aux)
            visit(current+1, copy)
            visit(current+1, scopy)
        visit()
        return listA
